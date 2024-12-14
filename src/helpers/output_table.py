import io
from datetime import datetime

import numpy as np
import pandas as pd
import pandera as pa
from sqlalchemy import Boolean
from sqlalchemy import create_engine
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import inspect
from sqlalchemy import Integer
from sqlalchemy import String
from ulid import ULID

from src import settings
from src.helpers.aws.s3 import S3
from src.helpers.logger import SetupLogger

_log = SetupLogger('src.helpers.output_table')


def send_to_db(df, model, chunk_size=10000):
    # TODO ao invés de usar pandas simples, implementar função de upsert mais elaborada
    execution_id = str(ULID())
    table_name = model.__tablename__
    _log.info(f'RUNNING SAVE ON DB | {table_name} | {execution_id}')
    engine = create_engine(settings.DB_URI)

    inspector = inspect(engine)
    if table_name not in inspector.get_table_names():
        raise ValueError(f"Tabela '{table_name}' não existe no banco de dados")

    _log.info(f'GETTING TABLE COLS | {table_name} | {execution_id}')
    existing_columns = inspector.get_columns(table_name)
    existing_column_names = [col['name'] for col in existing_columns]

    _log.info(f'REINDEXING DATAFRAME | {table_name}')
    df.reindex(columns=[existing_column_names])
    df = df[existing_column_names]

    _log.info(f"output_table_upsert | new run | {execution_id}")
    _log.info(f"output_table_upsert |data contract | {execution_id}")
    df = check_data_contract(df.copy(), model, execution_id)
    if df.empty:
        msg = "output_table_upsert | DC failed on all rows.. check discord DC trhead and s3 dataset'"
        _log.error(msg)
        raise ValueError(msg)

    _log.info(f'SENDING TO DB IN CHUNKS | {table_name} | {execution_id}')

    for start in range(0, len(df), chunk_size):
        chunk = df.iloc[start : start + chunk_size]
        chunk.to_sql(
            name=table_name,
            con=engine,
            if_exists='replace',
            index=False,
            method='multi',
        )
        _log.info(f'CHUNK SENT | {execution_id} | {table_name} - Rows {start} to {start + chunk_size - 1}')

    _log.info(f'DONE | {table_name} | {execution_id}')


def check_data_contract(df, model, execution_id):
    # TODO implementar função que envia notificação para software de comunicação da empresa (ex. Discord, Slack, etc)
    table_name = model.__tablename__
    _log.info(f"check_data_contract | {execution_id} |  {table_name} | begin")

    if not hasattr(model, 'get_dc_schema'):
        try:
            callable(getattr(model, 'get_dc_schema'))
        except Exception as e:
            _log.info(
                f"check_data_contract | {execution_id} |  {table_name} | class does have get_schema but is not callable --> {str(e)}",
            )
            return df
        _log.info(f"check_data_contract | {execution_id} |  {table_name} | class does not have pandera yet")
        return df

    sqlalchemy_to_pandas = {
        Float: np.float64,
        DateTime: 'datetime64[ns]',
        Date: 'datetime64[ns]',
        String: str,
        Integer: int,
        Boolean: bool,
    }
    _log.info(f"check_data_contract | {execution_id} |  {table_name} | transforming dict_type")
    dict_type = {c.name: sqlalchemy_to_pandas[type(c.type)] for c in model.__table__.columns.values()}
    df_val = df.astype(dict_type)
    _log.info(f"check_data_contract | {execution_id} |  {table_name} | getting schema")
    schema = model.get_dc_schema()
    try:
        _log.info(f"check_data_contract | {execution_id} |  {table_name} | validating data")
        validated_df = schema.validate(df_val, lazy=True)
        return validated_df
    except pa.errors.SchemaErrors as e:
        df_errors = e.failure_cases
        nunique_rows_errrors = df_errors['index'].nunique()
        _log.error(f"check_data_contract | {execution_id} |  {table_name} | errors have been found on data contract")
        _log.error(
            f"check_data_contract | {execution_id} |  {table_name} | {nunique_rows_errrors:_} rows out of {df.shape[0]:_} ( {nunique_rows_errrors / df.shape[0]:.1%} ) have failed on data contract",
        )

        df_sc_column_error_gb = pd.DataFrame()
        df_sc_dfs_error_gb = pd.DataFrame()

        _log.info(f"check_data_contract | {execution_id} |  {table_name} | getting schema_context=='Column'")
        df_sc_column = df_errors.query("schema_context=='Column'")
        if not df_sc_column.empty:
            df_sc_column['error'] = df_sc_column['column'] + ' / ' + df_sc_column['check'] + ' / failure case (' + df_sc_column['failure_case'].astype(str) + ')'
            df_sc_column_error_gb = df_sc_column.groupby('index').agg(
                {'error': lambda x: ', '.join(list(x)), 'column': 'count'},
            )
            df_sc_column_error_gb.columns = ['errors_column', 'errors_column_count']

        _log.info(f"check_data_contract | {execution_id} |  {table_name} | getting schema_context=='DataFrameSchema'")
        df_sc_dfs = df_errors.query("schema_context=='DataFrameSchema'")
        if not df_sc_dfs.empty:
            df_sc_dfs_error_gb = df_sc_dfs.groupby('index').agg(
                {'check': lambda x: ', '.join(set(x)), 'index': 'nunique'},
            )
            df_sc_dfs_error_gb.columns = ['errors_dataframeschema', 'errors_dataframeschema_count']
        _log.info(f"check_data_contract | {execution_id} |  {table_name} | creating combo excel")

        df_index_errors = pd.concat([df_sc_column_error_gb, df_sc_dfs_error_gb], axis=1)

        list_indexes = df_errors['index'].tolist()
        df_erros_to_send = df.loc[df.index.isin(list_indexes)]
        df_to_send = pd.concat([df_index_errors, df_erros_to_send], axis=1)
        if not df_to_send.empty:
            _log.info(f"check_data_contract | {execution_id} |  {table_name} | sending excel erros to s3")
            s3_client = S3()
            path = f"data_contract/{datetime.now().strftime('%Y_%m_%d')}/{table_name}/{execution_id}_{table_name}_error_data_contract.xlsx"
            file_bytesio_df_to_send = io.BytesIO()
            _log.info(f"check_data_contract | {execution_id} |  {table_name} | creating excel")
            df_to_send.to_excel(file_bytesio_df_to_send, freeze_panes=(1, 0), index=False)
            _log.info(f"check_data_contract | {execution_id} |  {table_name} | sending excel to S3: '{path}'")
            s3_client.write_file(data=file_bytesio_df_to_send, path=path)
        _log.info(f"check_data_contract | {execution_id} |  {table_name} | creating pass")
        df_pass = df.loc[~df.index.isin(list_indexes)]

        _log.info(f"Data contract validation failed: {nunique_rows_errrors:_} rows out of {df.shape[0]:_} ({nunique_rows_errrors / df.shape[0]:.1%}) failed.")

    _log.info(f"check_data_contract | {execution_id} |  entering {df.shape[0]:_} exiting {df_pass.shape[0]:_}")
    _log.info(f"check_data_contract | {execution_id} |  removing {df.shape[0] - df_pass.shape[0]:_} rows")

    return df_pass

from sqlalchemy import create_engine
from sqlalchemy import inspect

from src import settings
from src.helpers.logger import SetupLogger

_log = SetupLogger('src.helpers.output_table')


def send_to_db(df, table_name, chunk_size=10000):
    # TODO ao invés de usar pandas simples, implementar função de upsert mais elaborada
    _log.info(f'RUNNING SAVE ON DB | {table_name}')
    engine = create_engine(settings.DB_URI)

    inspector = inspect(engine)
    if table_name not in inspector.get_table_names():
        raise ValueError(f"Tabela '{table_name}' não existe no banco de dados")

    _log.info(f'GETTING TABLE COLS | {table_name}')
    existing_columns = inspector.get_columns(table_name)
    existing_column_names = [col['name'] for col in existing_columns]

    _log.info(f'REINDEXING DATAFRAME | {table_name}')
    df.reindex(columns=[existing_column_names])
    df = df[existing_column_names]

    _log.info(f'SENDING TO DB IN CHUNKS | {table_name}')

    for start in range(0, len(df), chunk_size):
        chunk = df.iloc[start : start + chunk_size]
        chunk.to_sql(
            name=table_name,
            con=engine,
            if_exists='replace',
            index=False,
            method='multi',
        )
        _log.info(f'CHUNK SENT | {table_name} - Rows {start} to {start + chunk_size - 1}')

    _log.info(f'DONE | {table_name}')

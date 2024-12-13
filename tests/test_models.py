from src.database.database import session, set_session
from src.database.utils import get_all_models
from sqlalchemy.sql import sqltypes

from sqlalchemy.sql import text

def test_models_all_tables_have_been_migrate():
    """
    Check if all table are migrated checkin on from db-mobilidade.models.__init__
    :return:
    """
    dict_models = get_all_models()

    set_session()
    all_tables_on_db = session().execute(text("select table_name from INFORMATION_SCHEMA.tables")).fetchall()
    all_tables_on_db = [tbl[0] for tbl in all_tables_on_db if tbl[0] != 'alembic_version']

    for table_schema_name, model in dict_models.items():
        assert len(
            model.__tablename__) <= 63, f"'{model.__tablename__=}' is more then 63 char -- {len(model.__tablename__)}.... check table name on .py file"

    for name_model, model in dict_models.items():
        assert model.__tablename__ in all_tables_on_db


def test_models_all_tables_have_been_migrate_and_column_matches():
    """
    Check if all table are migrated checkin on from db-mobilidade.models.__init__
    :return:
    """
    dict_models = get_all_models()

    set_session()

    for table_schema_name, model in dict_models.items():
        cols_model = [column.key for column in model.__table__.columns]
        for col in cols_model:
            # this will raise an error if col does not exists on table
            session().execute(text(f"select {col} from {model.__table_args__['schema']}.{model.__tablename__}")).fetchall()


def test_models_all_columns_has_max_chars():
    """
    Check if all table are migrated checkin on from db-mobilidade.models.__init__
    :return:
    """
    dict_models = get_all_models()

    set_session()

    for name_model, model in dict_models.items():
        cols_model = [column.key for column in model.__table__.columns]
        for col in cols_model:
            # this will raise an error if col does not exists on table
            assert len(col) <= 63, f"'{col}' is more then 63 char -- {len(col)}.... check table name on .py file"


def test_models_all_tables_have_been_migrate_dtype_columns():
    """
    Check if all table are migrated checkin on from db-mobilidade.models.__init__
    :return:
    """

    types_sql = {
        'date': sqltypes.Date(),
        'datetime': sqltypes.DateTime(),
        'timestamp without time zone': sqltypes.DateTime(),
        'string': sqltypes.String(),
        'character varying': sqltypes.String(),
        'float': sqltypes.Float(),
        'double precision': sqltypes.Float(),
        'integer': sqltypes.Integer(),
        'bool': sqltypes.Boolean(),
        'boolean': sqltypes.Boolean(),
        'text': sqltypes.Text(),
    }

    dict_models = get_all_models()

    set_session()

    for table_schema_name, model in dict_models.items():
        cols_model = [(column.key, column.type) for column in model.__table__.columns]

        for col in cols_model:
            # this will raise an error if col does not exists on table
            query = f""" SELECT DATA_TYPE
                        FROM INFORMATION_SCHEMA.COLUMNS
                        WHERE TABLE_NAME = '{model.__tablename__}'
                        and column_name = '{col[0]}'"""
            dtype_db = session().execute(text(query)).fetchall()[0][0]
            dtype_db = types_sql[dtype_db]

            assert type(col[1]) == type(dtype_db)

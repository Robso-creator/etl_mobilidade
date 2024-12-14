from contextlib import contextmanager

from sqlalchemy import create_engine

from src import settings
from src.helpers.logger import SetupLogger

_log = SetupLogger('etl_mobilidade.src.helpers.connect_postgres')


@contextmanager
def connect_postgres(db_source='db_mobilidade'):
    _dict_db_uri = {
        'db_mobilidade': settings.DB_URI,
    }
    if db_source not in list(_dict_db_uri.keys()):
        raise ValueError(f"db_source: '{db_source}' not defiend -- allowed dbs -> {sorted(list(_dict_db_uri.keys()))}")

    uri = _dict_db_uri[db_source]
    if not uri:
        raise ValueError(f"db_source: '{db_source}' have DB_URI variable set to null")

    engine = create_engine(uri)
    try:
        _log.info(f"openning connection for {db_source}")
        yield engine
    finally:
        _log.info(f"closing connection for {db_source}")
        engine.dispose()

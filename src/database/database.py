from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from analytics_db_models import settings

_dbsession = None
_engine = None
_sqlalchemy_url = None


def set_session(sqlalchemy_url=settings.DB_URI_ANALYTICS, engine=None):
    global _dbsession, _engine, _sqlalchemy_url

    _engine = _engine or engine or create_engine(sqlalchemy_url)
    _dbsession = scoped_session(sessionmaker(bind=_engine))
    return _dbsession


def commit_session(exception=None):
    if exception:
        _dbsession.rollback()
    else:
        _dbsession.commit()
    _dbsession.remove()
    if hasattr(_engine, 'dispose'):
        _engine.dispose()


def rollback_session():
    _dbsession.rollback()
    _dbsession.remove()
    if hasattr(_engine, 'dispose'):
        _engine.dispose()


def session():
    return _dbsession


@contextmanager
def connect_database(uri_string, env=None):
    global _dbsession, _engine, _sqlalchemy_url

    set_session()
    connection = 'testing'

    if _dbsession:
        connection = session().connection()

    try:
        yield connection
    finally:
        if _dbsession:
            _dbsession.remove()
            if hasattr(_engine, 'dispose'):
                _engine.dispose()

            _dbsession = None
            _engine = None
            _sqlalchemy_url = None


def execute_query(command, uri_string='redshift.url'):
    global _dbsession, _engine, _sqlalchemy_url
    set_session()

    session().execute(command)
    session().commit()

    _dbsession.remove()
    if hasattr(_engine, 'dispose'):
        _engine.dispose()

    _dbsession = None
    _engine = None
    _sqlalchemy_url = None


def copy_local_csv(filename, table_name, uri_string='redshift.url'):
    global _dbsession, _engine
    set_session()

    cursor = _engine.raw_connection().cursor()

    sql = f"COPY {table_name} FROM STDIN DELIMITER ';' CSV; COMMIT;"
    with open(filename) as f:
        cursor.copy_expert(sql, f)

    _dbsession.remove()
    if hasattr(_engine, 'dispose'):
        _engine.dispose()

    _dbsession = None
    _engine = None
    _sqlalchemy_url = None

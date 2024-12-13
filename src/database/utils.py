import inspect
import uuid
from datetime import datetime

import pytz


def get_all_models():
    from src.database import models

    # Get all packages from models.__init__
    model_dict = dict()
    members = inspect.getmembers(models)
    all_models = [member[1] for member in members if inspect.isclass(member[1]) and member[0] != 'Base']
    for model in all_models:
        table_name = model().__tablename__
        table_schema = model().__table_args__['schema']
        _key = f'{table_schema}.{table_name}'
        model_dict[_key] = model

    return model_dict


def mount_config_dict(table, version=False, stream=False):
    table_name = table.__tablename__
    table_schema = table.__table_args__['schema']

    if stream:
        config = {
            'stream': True,
            'columns': table.columns,
        }

        return config

    today = get_current_local_time()
    today_str = today.strftime('%Y%m%d')

    config = dict()

    config['redshift'] = {
        'table_name': table_name,
        'table_schema': table_schema,
        'index': table.keys,
        'pks': [c.name for c in table.__table__.columns if c.primary_key],
    }

    base_path = f'bases/schema_{table_schema}/base_{table_name}'
    config['s3'] = {
        'paths': {
            'current': f'{base_path}/base_{table_name}.csv',
            'history': f'{base_path}/historico/{today_str}_base_{table_name}.csv',
            'temp': f'{base_path}/historico/temp_base_{table_name}.csv',
        },
    }

    if version:
        config['s3']['paths']['version'] = f'bases/{table_name}/version/temp_{table_name}.csv'
        config['redshift']['version'] = version

    return config


def get_current_local_time():
    return datetime.now(pytz.timezone('America/Sao_Paulo')).replace(tzinfo=None)


def generate_revision():
    val = int(uuid.uuid4()) % 100000000000000
    return hex(val)[2:-1]


def get_indexes(table):
    """
    Return all columns and indexes for a given table
    :param table: (sqlalchemy.sql.schema.Table) table object
    :return: list of columns and keys
    """
    columns = [c.name for c in table.columns]

    keys = list()
    for i in table.indexes:
        for c in i.columns:
            keys.append(c.name)

    return columns, keys

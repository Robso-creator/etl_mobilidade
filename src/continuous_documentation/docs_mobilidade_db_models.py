import os
import sys

from src.continuous_documentation.data_types import dict_sqltypes_2_humans
from src.database.utils import get_all_models
from src.helpers.logger import SetupLogger

_log = SetupLogger('src.continuous_documentation.docs_mobilidade_db_models')

sys.path.append(os.getcwd())


def doc_analytics_db_models():
    _log.info('getting all models')
    all_models = get_all_models()
    _log.info('\tdone')
    dict_data_catalog = {}
    _log.info('creating dict to catalog')
    for table_schema_name, _table_obj in all_models.items():
        _table_name = _table_obj().__tablename__
        list_columns_pk = [col.name for col in _table_obj().__table__.columns if col.primary_key]
        str_columns_pk = ', '.join(list_columns_pk)
        str_columns_pk = f'__colunas que tornam uma linha única__: {str_columns_pk}\n\n'

        str_table_specification = _table_obj().__table__.comment + str_columns_pk
        dict_data_catalog[_table_name] = {
            'table_specification': str_table_specification,
            'columns': {},
        }
        for _column in _table_obj().__table__.columns:
            dict_data_catalog[_table_name]['columns'][_column.name] = {
                'type': dict_sqltypes_2_humans.get(_column.type.__class__, 'Unknown'),
                'comment': _column.comment or '',
                'pk': bool(_column.primary_key),
                'index': bool(_column.index),
            }

    _log.info('\tdone!')

    # make dict on alfabetic order
    dict_data_catalog = dict(sorted(dict_data_catalog.items()))
    file_path = os.path.join(os.getcwd(), 'docs', 'data_catalog.md')
    _log.info('generating docs')
    with open(file_path, 'w') as f:
        f.write('# Catalogação de dados do banco de ETL Mobilidade\n\n')
        f.write(
            f'Hoje temos __{len(dict_data_catalog.keys())} tabelas__ construídas no banco de dados. A seguir mais detalhes de cada tabela por ordem alfabética: \n\n',
        )
        counter = 1
        for table_name, _dict_data_catalog in dict_data_catalog.items():
            f.write(f'## {counter}) __{table_name}__ \n')
            f.write(f"{_dict_data_catalog['table_specification']}\n")
            f.write('\n| Coluna | Tipo | Comentário | Chave Primária | Índice | \n')
            f.write('| --- | --- | --- |--- |--- |\n')
            for column_name, v in _dict_data_catalog['columns'].items():
                column_type = _dict_data_catalog['columns'][column_name]['type']
                column_comment = _dict_data_catalog['columns'][column_name]['comment']
                column_pk = 'Sim' if _dict_data_catalog['columns'][column_name]['pk'] else 'Não'
                column_index = 'Sim' if _dict_data_catalog['columns'][column_name]['index'] else 'Não'
                f.write(f'| __{column_name}__ | {column_type} | {column_comment} | {column_pk} |{column_index} |\n')
            f.write('\n\n')
            counter += 1
    _log.info('\t doc generated')


if __name__ == '__main__':
    doc_analytics_db_models()

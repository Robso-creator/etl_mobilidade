def doc_analytics_db_models():
    import os

    import sys

    sys.path.append(os.getcwd())

    from analytics_db_models.models.base import SCHEMA_PRINCIPAL

    from analytics_db_models.scripts.data_catalog.data_types import dict_sqltypes_2_humans
    from analytics_db_models.utils import get_all_models

    print('getting all models')
    all_models = get_all_models()
    print('\tdone')
    dict_data_catalog = {}
    list_exclude_from_data_catalog = ['people']
    print('creating dict to catalog')
    for table_schema_name, _table_obj in all_models.items():
        _table_name = _table_obj().__tablename__
        if _table_obj().__table_args__['schema'] != SCHEMA_PRINCIPAL:
            print(
                f"skipping table='{_table_name}' on generate docs -- only allowed schema='{SCHEMA_PRINCIPAL}' -- table_schema='{_table_obj().__table_args__['schema']}'",
            )
            continue
        for _table_startswith in list_exclude_from_data_catalog:
            if _table_name.startswith(_table_startswith):
                print(f"skipping table '{_table_name}' on generate docs -- table on {list_exclude_from_data_catalog=} ")
                continue
            if _table_obj.__table_args__.get('schema', 'public') != 'public':
                print(
                    f"skiping table '{_table_name}' on generate docs because they are not on public schema: {_table_obj.__table_args__.get('schema', 'public')}",
                )
                continue

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

    print('\tdone!')

    # make dict on alfabetic order
    dict_data_catalog = dict(sorted(dict_data_catalog.items()))
    file_path = os.path.join(os.getcwd(), 'docs', 'data_catalog.md')
    print('generating docs')
    with open(file_path, 'w') as f:
        f.write('# Catalogação de dados do banco de Analytics\n\n')
        f.write(
            'A idéia desse documento é expor para a Liber como está estruturado o banco de dados de analytics para difundir a cultura _Data-Driven_ da empresa. \n\n',
        )
        f.write(
            f'Hoje temos __{len(dict_data_catalog.keys())} tabelas__ construídas no banco de dados de Anlatyics. Mostraremos a seguir mais detalhes de cada tabela por ordem alfabética. \n\n',
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
    print('\t doc generated')


if __name__ == '__main__':
    doc_analytics_db_models()

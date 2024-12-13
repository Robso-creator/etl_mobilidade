import pandas as pd

from src.helpers.aws.s3 import S3
from src.helpers.logger import SetupLogger

_log = SetupLogger('etl_mobilidade.src.transformer.gold.relacao_dos_veiculos_envolvidos_nos_acidentes_de_transito_com_vitima')


def main():
    s3_client = S3()
    folder = 'relacao-dos-veiculos-envolvidos-nos-acidentes-de-transito-com-vitima'
    list_file_path, list_file_name, _ = s3_client.list_files(prefix=f'bronze/{folder}')

    df_list = []
    for i, file_path in enumerate(list_file_path):
        if list_file_name[i].endswith('.csv') and list_file_name[i].startswith('si'):
            _df = s3_client.read_to_df(f'bronze/{folder}/{list_file_name[i]}')
            _df.columns = _df.columns.str.lower()
            df_list.append(_df)

    _log.info('Concatenating dataframes')
    df_final = pd.concat(df_list, ignore_index=True)
    del df_list

    _log.info('Treating data')
    df_final['numero_boletim'] = df_final['numero_boletim'].fillna(df_final['no_boletim'])
    df_final['sequencial_veiculo'] = df_final['sequencial_veiculo'].fillna(df_final['seq_veic'])
    df_final['codigo_categoria'] = df_final['codigo_categoria'].fillna(df_final['cod_categ'])
    df_final['codigo_especie'] = df_final['codigo_especie'].fillna(df_final['cod_especie'])
    df_final['descricao_situacao'] = df_final['descricao_situacao'].fillna(df_final['desc_situacao'])
    df_final['codigo_situacao'] = df_final['codigo_situacao'].fillna(df_final['cod_situacao'])
    df_final['descricao_tipo_socorro'] = df_final['descricao_tipo_socorro'].fillna(df_final['desc_tipo_socorro'])

    df_final.drop(columns=['no_boletim', 'seq_veic', 'cod_categ', 'cod_especie', 'desc_situacao', 'desc_tipo_socorro', 'nome_envolvido', 'cod_situacao'], inplace=True)

    for col in ['descricao_categoria', 'descricao_especie', 'descricao_situacao', 'descricao_tipo_socorro']:
        df_final[col] = df_final[col].str.strip()
    for col in ['data_hora_boletim']:
        df_final[col] = pd.to_datetime(df_final[col], dayfirst=True)
    df_final['last_modified'] = pd.to_datetime(df_final['last_modified'])

    dict_rename = {
        '_id': 'id',
    }
    df_final = df_final.rename(columns=dict_rename)

    s3_client.write_csv_file(df_final, f"gold/{folder}/enhanced_{folder.replace('-', '_')}.csv", header=True)


if __name__ == '__main__':
    main()

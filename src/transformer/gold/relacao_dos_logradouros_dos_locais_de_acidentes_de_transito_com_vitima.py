import pandas as pd

from src.helpers.aws.s3 import S3
from src.helpers.logger import SetupLogger

_log = SetupLogger('etl_mobilidade.src.transformer.gold.relacao_dos_logradouros_dos_locais_de_acidentes_de_transito_com_vitima')


def main():
    s3_client = S3()
    folder = 'relacao-dos-logradouros-dos-locais-de-acidentes-de-transito-com-vitima'
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
    df_final['numero_bairro'] = df_final['numero_bairro'].fillna(df_final['no_bairro'])
    df_final['numero_imovel'] = df_final['numero_imovel'].fillna(df_final['no_imovel'])
    df_final['numero_imovel_proximo'] = df_final['numero_imovel_proximo'].fillna(df_final['no_imovel_proximo'])
    df_final['numero_municipio'] = df_final['numero_municipio'].fillna(df_final['no_municipio'])
    df_final['numero_logradouro'] = df_final['numero_logradouro'].fillna(df_final['no_logradouro'])
    df_final['numero_boletim'] = df_final['numero_boletim'].fillna(df_final['no_boletim'])
    df_final['nome_logradouro_anterior'] = df_final['nome_logradouro_anterior'].fillna(df_final['nome_logradoro_anterior'])

    df_final.drop(columns=['no_bairro', 'no_imovel', 'no_imovel_proximo', 'no_municipio', 'no_logradouro', 'no_boletim', 'seq_logradouros', 'nome_logradoro_anterior'], inplace=True)

    for col in ['nome_municipio', 'nome_logradouro', 'nome_logradouro_anterior', 'tipo_bairro', 'descricao_tipo_bairro', 'nome_bairro', 'tipo_logradouro_anterior', 'tipo_logradouro']:
        df_final[col] = df_final[col].str.strip()
    for col in ['data_boletim']:
        df_final[col] = pd.to_datetime(df_final[col], dayfirst=True)
    df_final['last_modified'] = pd.to_datetime(df_final['last_modified'])

    dict_rename = {
        '_id': 'id',
        'data_boletim': 'data_hora_boletim',
    }
    df_final = df_final.rename(columns=dict_rename)

    s3_client.write_csv_file(df_final, f"gold/{folder}/enhanced_{folder.replace('-', '_')}.csv", header=True)


if __name__ == '__main__':
    main()

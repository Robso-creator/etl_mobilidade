import pandas as pd

from src.helpers.aws.s3 import S3
from src.helpers.logger import SetupLogger

_log = SetupLogger('etl_mobilidade.src.transformer.gold.relacao_das_pessoas_envolvidas_nos_acidentes_de_transito_com_vitima')


def main():
    s3_client = S3()
    folder = 'relacao-das-pessoas-envolvidas-nos-acidentes-de-transito-com-vitima'
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
    df_final['num_boletim'] = df_final['num_boletim'].fillna(df_final['no_boletim'])
    df_final.drop(columns=['no_boletim', 'cod_severidade_antiga'], inplace=True)

    for col in ['desc_severidade', 'categoria_habilitacao', 'descricao_habilitacao', 'especie_veiculo']:
        df_final[col] = df_final[col].str.strip()
    for col_boolean in ['condutor', 'passageiro', 'pedestre']:
        df_final[col_boolean] = df_final[col_boolean].replace({'N': False, 'S': True})
    for col_boolean in ['cinto_seguranca', 'embreagues']:
        df_final[col_boolean] = df_final[col_boolean].replace({'NÃO': False, 'SIM': True, 'NÃO INFORMADO': None})

    df_final['nascimento'] = df_final['nascimento'].replace('00/00/0000', pd.NaT)
    for col in ['nascimento', 'data_hora_boletim']:
        df_final[col] = pd.to_datetime(df_final[col], dayfirst=True)

    df_final['last_modified'] = pd.to_datetime(df_final['last_modified'])

    dict_rename = {
        '_id': 'id',
    }
    df_final = df_final.rename(columns=dict_rename)
    s3_client.write_csv_file(df_final, f"gold/{folder}/enhanced_{folder.replace('-', '_')}.csv", header=True)


if __name__ == '__main__':
    main()

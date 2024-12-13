import pandas as pd

from src.helpers.aws.s3 import S3
from src.helpers.logger import SetupLogger
from src.helpers.transformation import convert_utm_to_latlon

_log = SetupLogger('etl_mobilidade.src.transformer.gold.relacao_de_ocorrencias_de_acidentes_de_transito_com_vitima')


def main():
    s3_client = S3()
    folder = 'relacao-de-ocorrencias-de-acidentes-de-transito-com-vitima'
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
    _log.info('Extracting coordinates')
    df_final[['latitude', 'longitude']] = df_final.apply(
        lambda row: pd.Series(convert_utm_to_latlon(row['coordenada_x'], row['coordenada_y'])),
        axis=1,
    )

    dict_rename = {
        '_id': 'id',
        'coordenada_x': 'easting',
        'coordenada_y': 'northing',
        'data hora_boletim': 'data_hora_boletim',
    }
    df_final = df_final.rename(columns=dict_rename)

    cols_to_strip = ['desc_tipo_acidente', 'desc_tempo', 'pavimento', 'desc_regional', 'origem_boletim']
    for col in cols_to_strip:
        df_final[col] = df_final[col].str.strip()

    for col_boolean in ['hora_informada', 'indicador_fatalidade', 'local_sinalizado']:
        df_final[col_boolean] = df_final[col_boolean].replace({'NÃO': False, 'SIM': True, 'NÃO INFORMADO': None})

    for col in ['data_hora_boletim', 'data_inclusao']:
        df_final[col] = pd.to_datetime(df_final[col], dayfirst=True)

    df_final['data_alteracao_smsa'] = df_final['data_alteracao_smsa'].replace('00/00/0000', pd.NaT)
    _log.info('Writing file to S3')
    s3_client.write_csv_file(df_final, f"gold/{folder}/enhanced_{folder.replace('-', '_')}.csv", header=True)


if __name__ == '__main__':
    main()

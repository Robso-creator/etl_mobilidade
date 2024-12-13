import pandas as pd

from src.helpers.aws.s3 import S3
from src.helpers.logger import SetupLogger
from src.helpers.transformation import convert_utm_to_latlon
from src.helpers.transformation import extract_coordinates_linestring

_log = SetupLogger('etl_mobilidade.src.transformer.gold.redutor_de_velocidade')


def main():
    s3_client = S3()
    folder = 'redutor-de-velocidade'
    list_file_path, list_file_name, _ = s3_client.list_files(prefix=f'bronze/{folder}')

    df_list = []
    for i, file_path in enumerate(list_file_path):
        if file_path.endswith('.csv'):
            _df = s3_client.read_to_df(f'bronze/{folder}/{list_file_name[i]}')
            _df.columns = _df.columns.str.lower()
            df_list.append(_df)

    _log.info('Concatenating dataframes')
    df_final = pd.concat(df_list, ignore_index=True)
    del df_list
    _log.info('Extracting coordinates')
    df_final[['easting', 'northing']] = df_final['geometria'].apply(lambda x: pd.Series(extract_coordinates_linestring(x)))
    df_final[['latitude', 'longitude']] = df_final.apply(
        lambda row: pd.Series(convert_utm_to_latlon(row['easting'], row['northing'])),
        axis=1,
    )

    _log.info('Writing file to S3')
    s3_client.write_csv_file(df_final, f"gold/{folder}/enhanced_{folder.replace('-', '_')}.csv", header=True)


if __name__ == '__main__':
    main()
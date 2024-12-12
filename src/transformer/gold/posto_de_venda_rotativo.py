import pandas as pd

from src.helpers.aws.s3 import S3
from src.helpers.transformation import convert_utm_to_latlon
from src.helpers.transformation import extract_coordinates_point


def main():
    s3_client = S3()
    folder = 'posto-de-venda-rotativo'
    list_file_path, list_file_name, _ = s3_client.list_files(prefix=f'bronze/{folder}')

    df_list = []
    for i, file_path in enumerate(list_file_path):
        if file_path.endswith('.csv'):
            _df = s3_client.read_to_df(f'bronze/{folder}/{list_file_name[i]}')
            df_list.append(_df)

    df_final = pd.concat(df_list, ignore_index=True)

    df_final[['EASTING', 'NORTHING']] = df_final['GEOMETRIA'].apply(lambda x: pd.Series(extract_coordinates_point(x)))
    df_final[['LATITUDE', 'LONGITUDE']] = df_final.apply(
        lambda row: pd.Series(convert_utm_to_latlon(row['EASTING'], row['NORTHING'])),
        axis=1,
    )

    df_final.columns = df_final.columns.str.lower()

    s3_client.write_csv_file(df_final, f"gold/{folder}/enhanced_{folder.replace('-', '_')}.csv", header=True)


if __name__ == '__main__':
    main()

# python -m src.transformer.gold.posto_de_venda_rotativo

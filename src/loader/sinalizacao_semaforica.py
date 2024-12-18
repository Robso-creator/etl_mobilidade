import pandas as pd

from src.database.models import SinalizacaoSemaforica
from src.helpers.aws.s3 import S3
from src.helpers.logger import SetupLogger
from src.helpers.output_table import send_to_db

_log = SetupLogger('src.loader.sinalizacao_semaforica')


def main():
    s3_client = S3()
    folder = 'localizacao-das-sinalizacoes-semaforicas'
    list_file_path, list_file_name, _ = s3_client.list_files(prefix=f'gold/{folder}')
    df_list = []
    for i, file_path in enumerate(list_file_path):
        if file_path.endswith('.csv'):
            _df = s3_client.read_to_df(f'gold/{folder}/{list_file_name[i]}')
            _df.columns = _df.columns.str.lower()
            df_list.append(_df)

    df_final = pd.concat(df_list, ignore_index=True)
    del df_list

    send_to_db(df_final, SinalizacaoSemaforica)


if __name__ == '__main__':
    main()

# python -m src.loader.sinalizacao_semaforica

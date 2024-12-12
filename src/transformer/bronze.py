import json
from io import BytesIO

import pandas as pd

from src.helpers.aws.s3 import S3

lst_packages = [
    'posto-de-venda-rotativo',
    'redutor-de-velocidade',
    'circulacao-viaria-no-do-trecho',
    'localizacao-das-sinalizacoes-semaforicas',
    'faces-de-quadras-regulamentadas-com-estacionamento-rotativo',
    'estacionamento-rotativo-para-motofrete',
    'estacionamento_idoso',
    'relacao-de-ocorrencias-de-acidentes-de-transito-com-vitima',
    'relacao-dos-logradouros-dos-locais-de-acidentes-de-transito-com-vitima',
    'relacao-dos-veiculos-envolvidos-nos-acidentes-de-transito-com-vitima',
    'relacao-das-pessoas-envolvidas-nos-acidentes-de-transito-com-vitima',
]


def main():
    s3_client = S3()

    for package in lst_packages:
        list_file_path, list_file_name, _ = s3_client.list_files(prefix=f'landing/{package}')
        for i, file_path in enumerate(list_file_path):
            content = s3_client.read_file(file_path).read()

            json_content = json.loads(content.decode('utf-8'))

            df = pd.DataFrame(json_content['data'])

            df['RESOURCE_ID'] = json_content['metadata']['id']
            df['PACKAGE_ID'] = json_content['metadata']['package_id']
            df['NAME'] = json_content['metadata']['name']
            df['LAST_MODIFIED'] = json_content['metadata']['last_modified']
            df['LAST_MODIFIED'] = pd.to_datetime(df['LAST_MODIFIED'])

            buffer = BytesIO()
            df.to_csv(buffer, index=False)
            buffer.seek(0)

            s3_client.write_file(buffer, f"bronze/{package}/{list_file_name[i].replace('.json', '.csv')}")


if __name__ == '__main__':
    # main()
    s3_client = S3()
    df = s3_client.read_to_df('bronze/posto-de-venda-rotativo/20230301_posto_venda_rotativo.csv')
    print(df.head())

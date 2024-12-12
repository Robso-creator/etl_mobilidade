import io
import json
import urllib.request

from src.helpers.aws.s3 import S3
from src.helpers.logger import SetupLogger
from src.helpers.transformation import remove_accents

_log = SetupLogger('etl_mobilidade.src.extractor.main')

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
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    }
    CORE_URL = 'https://dados.pbh.gov.br/api/3/action/'
    s3_client = S3()

    for package in lst_packages:
        _log.info(f'Getting resources from package {package}')
        response = urllib.request.Request(f'{CORE_URL}package_show?id={package}', headers=headers)
        response_dict = json.loads(urllib.request.urlopen(response).read())['result']['resources']

        for resource in [_dict for _dict in response_dict if _dict['format'] == 'CSV']:
            _log.info(f"Getting data from resource {resource['name']} | {resource['id']}")
            response = urllib.request.Request(
                f"{CORE_URL}datastore_search?resource_id={resource['id']}&limit=1000000",
                headers=headers,
            )
            _dict = {
                'metadata': resource,
                'data': json.loads(urllib.request.urlopen(response).read())['result']['records'],
            }

            json_data = json.dumps(_dict)
            json_buffer = io.BytesIO(json_data.encode('utf-8'))
            file_name = resource['name'].split('.')[0].replace(' ', '_').replace('-', '_').replace('(', '').replace(')', '').replace('/', '_').replace('__', '_').replace('__', '_').lower()
            file_name = remove_accents(file_name)

            s3_client.write_file(json_buffer, f"landing/{package}/{file_name}.json")


if __name__ == '__main__':
    main()

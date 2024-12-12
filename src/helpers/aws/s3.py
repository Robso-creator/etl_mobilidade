import io
import json
import os

import pandas as pd
from botocore.exceptions import ClientError

from src import settings
from src.helpers.aws.core import AWS
from src.helpers.logger import SetupLogger

_log = SetupLogger('etl_mobilidade.src.helpers.s3')


class S3(AWS):
    def __init__(self, bucket=None, access_id=None, secret_id=None):
        super().__init__(service_name='s3', access_id=access_id, secret_id=secret_id)

        self.bucket = bucket or settings.MINIO_BUCKET

    def list_files(self, prefix=None, name_matches=None, keep_folders=False):
        """
        Function to list all files on a folder (and sub folders) on s3 given a prefix
        :param prefix: path of folder (eg. path = 'posto-de-venda-rotativo/')
        :param name_matches: pattern to find on file name (eg.select only files that ends with
                            .zip -> name_matches = '*.zip')
        :param keep_folders: T/F -> if True, keep folders on list (folders have no file_name)
        :return: 3 lists: file path, file name and file modification time
        """
        kw_args = {'Bucket': self.bucket, 'Prefix': prefix}
        list_file_path = []
        list_file_name = []
        modification_time = []
        _log.info(f"Getting list files from prefix {prefix}..")
        while True:
            objs = self.client.list_objects_v2(**kw_args)
            if not objs.get('Contents'):
                return list(), list(), list()
            for obj in objs.get('Contents'):
                list_file_path.append(obj['Key'])
                list_file_name.append(os.path.split(obj['Key'])[1])
                modification_time.append(obj['LastModified'])
            try:
                kw_args['ContinuationToken'] = objs['NextContinuationToken']
            except KeyError:
                break

        df = pd.DataFrame(
            {
                'filepath': list_file_path,
                'filename': list_file_name,
                'modification_time': modification_time,
            },
        )

        if not keep_folders:  # in other words, only files
            df = df.loc[df['filename'] != '']
        if name_matches:  # match for name_matches
            df = df.loc[df['filename'].str.contains(name_matches)]
        list_file_path = df['filepath'].tolist()
        list_file_name = df['filename'].tolist()
        list_modification_time = df['modification_time'].tolist()
        _log.info(f"Returning list files from prefix {prefix}")
        return list_file_path, list_file_name, list_modification_time

    def read_file(self, path):
        """
        path =  'posto-de-venda-rotativo/.... .EXT''
        return (s3.object)
        """
        data = io.BytesIO()
        try:
            _log.info(f"reading '{self.bucket}/{path}'")
            self.client.download_fileobj(self.bucket, path, data)
        except ClientError:
            raise FileNotFoundError(f"Can't find file: s3://{self.bucket}/{path}")

        data.name = path
        data.seek(0)
        return data

    def read_to_df(self, path, sep=',', decimal='.', sheet_name=0):
        """
        Read a file into pandas dataframe
        :param path: path of file
        :param sep: separation
        :param decimal: decimal
        :param sheet_name: sheet_name file is excel
        :return: dataframe
        """
        allowed_extensions = ['.csv', '.xlsx']
        _file_ext = os.path.splitext(path)[1]
        if _file_ext not in allowed_extensions:
            raise LookupError(f"file extension '{_file_ext}' not allowed -> only allowed: '{allowed_extensions}'")

        _file = self.read_file(path=path)

        df = pd.DataFrame()

        if _file_ext == '.csv':
            df = pd.read_csv(_file, sep=sep, decimal=decimal)

        if _file_ext == '.xlsx':
            df = pd.read_excel(_file, sheet_name=sheet_name, engine='openpyxl')

        return df

    def write_file(self, data, path):
        data.seek(0)
        _log.info(f"saving at '{self.bucket}/{path}'")
        _content_type = 'text/plain' if self.simulate else ''
        self.client.put_object(Body=data.getvalue(), Bucket=self.bucket, Key=path, ContentType=_content_type)

        return path

    def write_csv_file(self, df, path, sep=',', header=False, decimal_format='.', index=False):
        """
        path -> path to write csv (eg. 'posto-de-venda-rotativo/xxx.csv')
        return (s3.object)
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError('df is not a pandas DataFrame')

        if df.empty:
            raise OSError('DataFrame is empty')

        # check if file is '.csv'
        if path[-4:] != '.csv':
            raise TypeError(f"File is not csv --> '{path}'")

        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, sep=sep, decimal=decimal_format, header=header, index=index)

        return self.write_file(csv_buffer, path)

    def delete_file(self, path):
        """
        Delete a file given a path
        :param path: path of file
        :return: nothing
        """

        kwargs = {
            'Bucket': self.bucket,
            'Key': path,
        }

        self.client.delete_object(**kwargs)

        return f"{self.bucket}/{path}"

    def delete_folder(self, path_folder):
        """
        Delete a folder given a path
        :param path_folder: folder path
        :return: nothing
        """

        if not path_folder.endswith('/'):
            raise ValueError("A prefix must be a folder... it must end with '/'")

        bucket = self.resource.Bucket(self.bucket)
        bucket.objects.filter(Prefix=path_folder).delete()

    def list_folders(self, prefix=None):
        """
        Function to list all folders name and folders path
        :param prefix: path of folder (eg. path = 'posto-de-venda-rotativo/')
        :return: 2 lists: list_file_path, list_file_name
        """
        kw_args = {'Bucket': self.bucket, 'Prefix': prefix, 'Delimiter': '/'}
        list_file_path = []
        list_file_name = []

        # _log.info(f"Getting list folders from prefix {prefix}..")
        while True:
            objs = self.client.list_objects_v2(**kw_args)
            if not objs.get('CommonPrefixes'):
                return list(), list()
            for obj in objs.get('CommonPrefixes'):
                list_file_path.append(obj['Prefix'][:-1])
                list_file_name.append(os.path.split(obj['Prefix'][:-1])[1])
            try:
                kw_args['ContinuationToken'] = objs['NextContinuationToken']
            except KeyError:
                break

        _log.info(f"Returning list folders from prefix {prefix}")

        return list_file_path, list_file_name


if __name__ == '__main__':
    s3_client = S3()

    data = {'hello': 'world'}
    json_data = json.dumps(data, indent=4)
    json_buffer = io.BytesIO(json_data.encode('utf-8'))
    s3_client.write_file(json_buffer, 'data.json')

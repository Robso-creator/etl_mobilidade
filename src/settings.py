import os

from loadotenv import load_env

load_env()

ENV = os.getenv('ENV')
SIMULATE = False if os.getenv('ENV').lower() == 'production' else True

AWS_REGION = 'us-east-1'
MINIO_ROOT_USER = os.getenv('MINIO_ROOT_USER')
MINIO_ROOT_PASSWORD = os.getenv('MINIO_ROOT_PASSWORD')
MINIO_BUCKET = os.getenv('MINIO_BUCKET')

DB_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'

AWS_ENDPOINT_URL_MINIO = 'http://minio-mobilidade:9000'

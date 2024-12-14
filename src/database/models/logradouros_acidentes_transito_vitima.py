import pandas as pd
import pandera as pa
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from src.database.models.base import _template
from src.database.models.base import Base
from src.database.utils import get_indexes
from src.database.utils import mount_config_dict


class LogradourosAcidentesTransitoVitima(Base):
    __tablename__ = 'logradouros_acidentes_transito_vitima'

    dict_substitute = {
        'each_line_represents': 'um logradouro onde ocorreu um acidente de trânsito com vítima registrado',
        'freshness': 'Indeterminada',
        'data_source': 'Relação dos logradouros dos locais de acidentes de trânsito com vítima',
        'product': 'Mobilidade Urbana',
    }
    __table_args__ = {
        'comment': _template.substitute(**dict_substitute),
        'schema': 'public',
    }

    id = Column('id', Integer, primary_key=True, nullable=False, comment='Identificador único do logradouro')
    numero_boletim = Column('numero_boletim', String(20), comment='Número do boletim de ocorrência')
    data_hora_boletim = Column('data_hora_boletim', DateTime, comment='Data e hora do boletim')
    numero_municipio = Column('numero_municipio', Float, comment='Número do município')
    nome_municipio = Column('nome_municipio', String(50), comment='Nome do município')
    sequencia_logradouros = Column('sequencia_logradouros', Float, comment='Sequência dos logradouros')
    numero_logradouro = Column('numero_logradouro', Float, comment='Número do logradouro')
    tipo_logradouro = Column('tipo_logradouro', String(10), comment='Tipo de logradouro')
    nome_logradouro = Column('nome_logradouro', String(100), comment='Nome do logradouro')
    tipo_logradouro_anterior = Column('tipo_logradouro_anterior', String(10), comment='Tipo do logradouro anterior')
    numero_bairro = Column('numero_bairro', Float, comment='Número do bairro')
    nome_bairro = Column('nome_bairro', String(50), comment='Nome do bairro')
    tipo_bairro = Column('tipo_bairro', String(2), comment='Tipo do bairro')
    descricao_tipo_bairro = Column('descricao_tipo_bairro', String(20), comment='Descrição do tipo de bairro')
    numero_imovel = Column('numero_imovel', String, comment='Número do imóvel')
    numero_imovel_proximo = Column('numero_imovel_proximo', Float, comment='Número do imóvel próximo')
    resource_id = Column('resource_id', String, comment='Identificador único do recurso')
    package_id = Column('package_id', String, comment='Identificador único do pacote')
    name = Column('name', String(100), comment='Nome do recurso')
    last_modified = Column('last_modified', DateTime, comment='Data e hora da última modificação')
    nome_logradouro_anterior = Column('nome_logradouro_anterior', String(100), comment='Nome do logradouro anterior')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columns, self.keys = get_indexes(self.__table__)

    def get_config_dict(self):
        config = mount_config_dict(self)
        return config

    @staticmethod
    def get_dc_schema() -> pa.DataFrameSchema:
        return pa.DataFrameSchema(
            columns={
                'id': pa.Column(
                    dtype=int,
                    checks=[
                        pa.Check(lambda s: s.is_unique, error="A coluna 'id' deve conter valores únicos"),
                    ],
                    nullable=False,
                    required=True,
                    description='Identificador único do logradouro',
                ),
                'numero_boletim': pa.Column(
                    dtype=str,
                    description='Número do boletim de ocorrência',
                ),
                'data_hora_boletim': pa.Column(
                    dtype=pd.Timestamp,
                    description='Data e hora do boletim',
                ),
                'numero_municipio': pa.Column(
                    dtype=float,
                    nullable=True,
                    description='Número do município',
                ),
                'nome_municipio': pa.Column(
                    dtype=str,
                    description='Nome do município',
                ),
                'sequencia_logradouros': pa.Column(
                    dtype=float,
                    nullable=True,
                    description='Sequência dos logradouros',
                ),
                'numero_logradouro': pa.Column(
                    dtype=float,
                    nullable=True,
                    description='Número do logradouro',
                ),
                'tipo_logradouro': pa.Column(
                    dtype=str,
                    description='Tipo de logradouro',
                ),
                'nome_logradouro': pa.Column(
                    dtype=str,
                    description='Nome do logradouro',
                ),
                'tipo_logradouro_anterior': pa.Column(
                    dtype=str,
                    description='Tipo do logradouro anterior',
                ),
                'numero_bairro': pa.Column(
                    dtype=float,
                    nullable=True,
                    description='Número do bairro',
                ),
                'nome_bairro': pa.Column(
                    dtype=str,
                    description='Nome do bairro',
                ),
                'tipo_bairro': pa.Column(
                    dtype=str,
                    description='Tipo do bairro',
                ),
                'descricao_tipo_bairro': pa.Column(
                    dtype=str,
                    description='Descrição do tipo de bairro',
                ),
                'numero_imovel': pa.Column(
                    dtype=str,
                    description='Número do imóvel',
                ),
                'numero_imovel_proximo': pa.Column(
                    dtype=float,
                    nullable=True,
                    description='Número do imóvel próximo',
                ),
                'resource_id': pa.Column(
                    dtype=str,
                    description='Identificador único do recurso',
                ),
                'package_id': pa.Column(
                    dtype=str,
                    description='Identificador único do pacote',
                ),
                'name': pa.Column(
                    dtype=str,
                    description='Nome do recurso',
                ),
                'last_modified': pa.Column(
                    dtype=pd.Timestamp,
                    description='Data e hora da última modificação',
                ),
                'nome_logradouro_anterior': pa.Column(
                    dtype=str,
                    description='Nome do logradouro anterior',
                ),
            },
        )

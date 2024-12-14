import pandas as pd
import pandera as pa
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from src.database.models.base import _template
from src.database.models.base import Base
from src.database.utils import get_indexes
from src.database.utils import mount_config_dict


class OcorrenciasAcidentesTransitoVitima(Base):
    __tablename__ = 'ocorrencias_acidentes_transito_vitima'

    dict_substitute = {
        'each_line_represents': 'uma ocorrência de acidente de trânsito com vítima registrada',
        'freshness': 'Indeterminada',
        'data_source': 'Relação de ocorrências de acidentes de trânsito com vítima',
        'product': 'Mobilidade Urbana',
    }
    __table_args__ = {
        'comment': _template.substitute(**dict_substitute),
        'schema': 'public',
    }

    id = Column('id', Integer, primary_key=True, nullable=False, comment='Identificador único da ocorrência')
    numero_boletim = Column('numero_boletim', String(20), comment='Número do boletim de ocorrência')
    data_hora_boletim = Column('data_hora_boletim', DateTime, comment='Data e hora do boletim')
    data_inclusao = Column('data_inclusao', DateTime, comment='Data de inclusão do boletim')
    tipo_acidente = Column('tipo_acidente', String(10), comment='Tipo de acidente')
    desc_tipo_acidente = Column('desc_tipo_acidente', String(50), comment='Descrição do tipo de acidente')
    cod_tempo = Column('cod_tempo', Integer, comment='Código do tempo')
    desc_tempo = Column('desc_tempo', String(20), comment='Descrição do tempo')
    cod_pavimento = Column('cod_pavimento', Integer, comment='Código do pavimento')
    pavimento = Column('pavimento', String(20), comment='Descrição do pavimento')
    cod_regional = Column('cod_regional', Integer, comment='Código da região')
    desc_regional = Column('desc_regional', String(20), comment='Descrição da região')
    origem_boletim = Column('origem_boletim', String(20), comment='Origem do boletim')
    local_sinalizado = Column('local_sinalizado', Boolean, comment='Indicador se o local é sinalizado')
    velocidade_permitida = Column('velocidade_permitida', Integer, comment='Velocidade permitida no local')
    easting = Column('easting', Float, comment='Coordenada Easting')
    northing = Column('northing', Float, comment='Coordenada Northing')
    hora_informada = Column('hora_informada', Boolean, comment='Indicador se a hora foi informada')
    indicador_fatalidade = Column('indicador_fatalidade', Boolean, comment='Indicador de fatalidade')
    valor_ups = Column('valor_ups', Integer, comment='Valor UPS')
    descricao_ups = Column('descricao_ups', String(20), comment='Descrição da UPS')
    data_alteracao_smsa = Column('data_alteracao_smsa', DateTime, comment='Data de alteração pela SMSA')
    valor_ups_antiga = Column('valor_ups_antiga', Integer, comment='Valor da UPS antiga')
    descricao_ups_antiga = Column('descricao_ups_antiga', String(20), comment='Descrição da UPS antiga')
    resource_id = Column('resource_id', String, comment='Identificador único do recurso')
    package_id = Column('package_id', String, comment='Identificador único do pacote')
    name = Column('name', String(100), comment='Nome do recurso')
    last_modified = Column('last_modified', DateTime, comment='Data e hora da última modificação')
    latitude = Column('latitude', Float, comment='Latitude')
    longitude = Column('longitude', Float, comment='Longitude')

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
                    description='Identificador único da ocorrência',
                ),
                'numero_boletim': pa.Column(
                    dtype=str,
                    description='Número do boletim de ocorrência',
                ),
                'data_hora_boletim': pa.Column(
                    dtype=pd.Timestamp,
                    description='Data e hora do boletim',
                ),
                'data_inclusao': pa.Column(
                    dtype=pd.Timestamp,
                    description='Data de inclusão do boletim',
                ),
                'tipo_acidente': pa.Column(
                    dtype=str,
                    description='Tipo de acidente',
                ),
                'desc_tipo_acidente': pa.Column(
                    dtype=str,
                    description='Descrição do tipo de acidente',
                ),
                'cod_tempo': pa.Column(
                    dtype=int,
                    description='Código do tempo',
                ),
                'desc_tempo': pa.Column(
                    dtype=str,
                    description='Descrição do tempo',
                ),
                'cod_pavimento': pa.Column(
                    dtype=int,
                    description='Código do pavimento',
                ),
                'pavimento': pa.Column(
                    dtype=str,
                    description='Descrição do pavimento',
                ),
                'cod_regional': pa.Column(
                    dtype=int,
                    description='Código da região',
                ),
                'desc_regional': pa.Column(
                    dtype=str,
                    description='Descrição da região',
                ),
                'origem_boletim': pa.Column(
                    dtype=str,
                    description='Origem do boletim',
                ),
                'local_sinalizado': pa.Column(
                    dtype=bool,
                    nullable=True,
                    description='Indicador se o local é sinalizado',
                ),
                'velocidade_permitida': pa.Column(
                    dtype=int,
                    description='Velocidade permitida no local',
                ),
                'easting': pa.Column(
                    dtype=float,
                    nullable=True,
                    description='Coordenada Easting',
                ),
                'northing': pa.Column(
                    dtype=float,
                    nullable=True,
                    description='Coordenada Northing',
                ),
                'hora_informada': pa.Column(
                    dtype=bool,
                    nullable=True,
                    description='Indicador se a hora foi informada',
                ),
                'indicador_fatalidade': pa.Column(
                    dtype=bool,
                    nullable=True,
                    description='Indicador de fatalidade',
                ),
                'valor_ups': pa.Column(
                    dtype=int,
                    description='Valor UPS',
                ),
                'descricao_ups': pa.Column(
                    dtype=str,
                    description='Descrição da UPS',
                ),
                'data_alteracao_smsa': pa.Column(
                    dtype=pd.Timestamp,
                    nullable=True,
                    description='Data de alteração pela SMSA',
                ),
                'valor_ups_antiga': pa.Column(
                    dtype=int,
                    description='Valor da UPS antiga',
                ),
                'descricao_ups_antiga': pa.Column(
                    dtype=str,
                    description='Descrição da UPS antiga',
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
                'latitude': pa.Column(
                    dtype=float,
                    nullable=True,
                    description='Latitude',
                ),
                'longitude': pa.Column(
                    dtype=float,
                    nullable=True,
                    description='Longitude',
                ),
            },
        )

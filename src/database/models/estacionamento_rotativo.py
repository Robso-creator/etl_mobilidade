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


class EstacionamentoRotativo(Base):
    __tablename__ = 'estacionamento_rotativo'

    dict_substitute = {
        'each_line_represents': 'um estacionamento rotativo',
        'freshness': 'Indeterminada',
        'data_source': 'Estacionamento Rotativo',
        'product': 'Mobilidade',
    }
    __table_args__ = {
        'comment': _template.substitute(**dict_substitute),
        'schema': 'public',
    }

    id = Column('id', Integer, primary_key=True, nullable=False, comment='Identificador único do estacionamento')
    fid = Column('fid', String(100), comment='ID do estacionamento rotativo')
    id_estacionamento = Column('id_estacionamento', Integer, comment='Identificador do estacionamento')
    numero_vagas_fisicas = Column('numero_vagas_fisicas', Integer, comment='Número de vagas físicas')
    numero_vagas_rotativas = Column('numero_vagas_rotativas', Integer, comment='Número de vagas rotativas')
    tempo_permanencia = Column('tempo_permanencia', String(50), comment='Tempo máximo de permanência')
    logradouro = Column('logradouro', String(100), comment='Nome do logradouro')
    referencia_logradouro = Column('referencia_logradouro', String(100), comment='Referência do logradouro')
    bairro = Column('bairro', String(50), comment='Bairro do estacionamento')
    geometria = Column('geometria', String, comment='Geometria do estacionamento')
    periodo_valido_regra_operacao = Column('periodo_valido_regra_operacao', String(50), comment='Período válido de operação')
    dia_regra_operacao = Column('dia_regra_operacao', String(50), comment='Dias da semana de operação')
    resource_id = Column('resource_id', String, comment='Identificador do recurso')
    package_id = Column('package_id', String, comment='Identificador do pacote')
    name = Column('name', String(100), comment='Nome do estacionamento')
    last_modified = Column('last_modified', DateTime, comment='Data e hora da última modificação')
    easting = Column('easting', Float, comment='Coordenada Easting')
    northing = Column('northing', Float, comment='Coordenada Northing')
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
                    description='Identificador único do estacionamento',
                ),
                'fid': pa.Column(
                    dtype=str,
                    nullable=True,
                    description='ID do estacionamento rotativo',
                ),
                'id_estacionamento': pa.Column(
                    dtype=int,
                    nullable=True,
                    description='Identificador do estacionamento',
                ),
                'numero_vagas_fisicas': pa.Column(
                    dtype=int,
                    nullable=True,
                    description='Número de vagas físicas',
                ),
                'numero_vagas_rotativas': pa.Column(
                    dtype=int,
                    nullable=True,
                    description='Número de vagas rotativas',
                ),
                'tempo_permanencia': pa.Column(
                    dtype=str,
                    nullable=True,
                    description='Tempo máximo de permanência',
                ),
                'logradouro': pa.Column(
                    dtype=str,
                    nullable=True,
                    description='Nome do logradouro',
                ),
                'referencia_logradouro': pa.Column(
                    dtype=str,
                    nullable=True,
                    description='Referência do logradouro',
                ),
                'bairro': pa.Column(
                    dtype=str,
                    nullable=True,
                    description='Bairro do estacionamento',
                ),
                'geometria': pa.Column(
                    dtype=str,
                    nullable=True,
                    description='Geometria do estacionamento',
                ),
                'periodo_valido_regra_operacao': pa.Column(
                    dtype=str,
                    nullable=True,
                    description='Período válido de operação',
                ),
                'dia_regra_operacao': pa.Column(
                    dtype=str,
                    nullable=True,
                    description='Dias da semana de operação',
                ),
                'resource_id': pa.Column(
                    dtype=str,
                    nullable=True,
                    description='Identificador do recurso',
                ),
                'package_id': pa.Column(
                    dtype=str,
                    nullable=True,
                    description='Identificador do pacote',
                ),
                'name': pa.Column(
                    dtype=str,
                    nullable=True,
                    description='Nome do estacionamento',
                ),
                'last_modified': pa.Column(
                    dtype=pd.Timestamp,
                    nullable=True,
                    description='Data e hora da última modificação',
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

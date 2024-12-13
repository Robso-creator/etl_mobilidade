from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from src.database.models.base import _template
from src.database.models.base import Base
from src.database.utils import get_indexes
from src.database.utils import mount_config_dict


class EstacionamentoRotativoIdoso(Base):
    __tablename__ = 'estacionamento_rotativo_idoso'

    dict_substitute = {
        'each_line_represents': 'um estacionamento rotativo para idosos',
        'freshness': 'Indeterminada',
        'data_source': 'Localização das Vagas de Estacionamento de Idosos',
        'product': 'Mobilidade',
    }
    __table_args__ = {
        'comment': _template.substitute(**dict_substitute),
        'schema': 'public',
    }

    id = Column('id', Integer, primary_key=True, nullable=False, comment='Identificador único do estacionamento')
    fid = Column('fid', String(100), comment='ID do estacionamento rotativo')
    id_edesp = Column('id_edesp', Integer, comment='Identificador de estacionamento')
    tipo_estacionamento = Column('tipo_estacionamento', String(50), comment='Tipo de estacionamento')
    destinacao_especifica = Column('destinacao_especifica', String(50), comment='Destinação específica do estacionamento')
    dia_regra_operacao = Column('dia_regra_operacao', String(50), comment='Dias da semana de operação')
    periodo_valido_regra_operacao = Column('periodo_valido_regra_operacao', String(50), comment='Período válido de operação')
    numero_vagas_fisicas = Column('numero_vagas_fisicas', Integer, comment='Número de vagas físicas')
    numero_vagas_rotativas = Column('numero_vagas_rotativas', Integer, comment='Número de vagas rotativas')
    tempo_permanencia = Column('tempo_permanencia', String(50), comment='Tempo máximo de permanência')
    tipo_logradouro = Column('tipo_logradouro', String(50), comment='Tipo de logradouro')
    logradouro = Column('logradouro', String(100), comment='Nome do logradouro')
    referencia_logradouro = Column('referencia_logradouro', String(100), comment='Referência do logradouro')
    bairro = Column('bairro', String(50), comment='Bairro do estacionamento')
    geometria = Column('geometria', String, comment='Geometria do estacionamento')
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

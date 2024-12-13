from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from src.database.models.base import _template
from src.database.models.base import Base
from src.database.utils import get_indexes
from src.database.utils import mount_config_dict


class RedutorVelocidade(Base):
    __tablename__ = 'redutor_velocidade'

    dict_substitute = {
        'each_line_represents': 'um redutor de velocidade registrado',
        'freshness': 'Indeterminada',
        'data_source': 'Redutor de Velocidade',
        'product': 'Mobilidade Urbana',
    }
    __table_args__ = {
        'comment': _template.substitute(**dict_substitute),
        'schema': 'public',
    }

    id = Column('id', Integer, primary_key=True, nullable=False, comment='Identificador único do redutor de velocidade')
    id_redutor_velocidade = Column('id_redutor_velocidade', Integer, comment='Identificador do redutor de velocidade')
    num_projeto_operacional = Column('num_projeto_operacional', String(50), nullable=True, comment='Número do projeto operacional')
    endereco_referencia = Column('endereco_referencia', String(100), comment='Endereço de referência do redutor de velocidade')
    bairro = Column('bairro', String(50), comment='Bairro onde está localizado o redutor de velocidade')
    referencia_localizacao = Column('referencia_localizacao', String(100), comment='Referência da localização do redutor de velocidade')
    data_implantacao = Column('data_implantacao', DateTime, nullable=True, comment='Data de implantação do redutor de velocidade')
    data_ultima_manutencao = Column('data_ultima_manutencao', DateTime, nullable=True, comment='Data da última manutenção do redutor de velocidade')
    geometria = Column('geometria', String, comment='Geometria do redutor de velocidade')
    resource_id = Column('resource_id', String, comment='Identificador único do recurso')
    package_id = Column('package_id', String, comment='Identificador único do pacote')
    name = Column('name', String(100), comment='Nome do recurso')
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

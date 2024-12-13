from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from src.database.models.base import _template
from src.database.models.base import Base
from src.database.utils import get_indexes
from src.database.utils import mount_config_dict


class CirculacaoViaria(Base):
    __tablename__ = 'circulacao_viaria'

    dict_substitute = {
        'each_line_represents': 'um trecho de circulação registrado',
        'freshness': 'Indeterminada',
        'data_source': 'Circulação Viária - Nó do Trecho',
        'product': 'Mobilidade Urbana',
    }
    __table_args__ = {
        'comment': _template.substitute(**dict_substitute),
        'schema': 'public',
    }

    id = Column('id', Integer, primary_key=True, nullable=False, comment='Identificador único do trecho')
    id_ntcv = Column('id_ntcv', Float, comment='Identificador NTCV')
    geometria = Column('geometria', String, comment='Geometria do trecho')
    resource_id = Column('resource_id', String, comment='Identificador único do recurso')
    package_id = Column('package_id', String, comment='Identificador único do pacote')
    name = Column('name', String(100), comment='Nome do trecho')
    last_modified = Column('last_modified', DateTime, comment='Data e hora da última modificação')
    id_tcv = Column('id_tcv', Float, comment='Identificador TCV')
    tipo_trecho_circulacao = Column('tipo_trecho_circulacao', String(50), comment='Tipo de trecho de circulação')
    tipo_logradouro = Column('tipo_logradouro', String(50), comment='Tipo de logradouro')
    logradouro = Column('logradouro', String(100), comment='Logradouro')
    id_no_circ_inicial = Column('id_no_circ_inicial', Float, comment='Identificador do nó inicial')
    id_no_circ_final = Column('id_no_circ_final', Float, comment='Identificador do nó final')
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

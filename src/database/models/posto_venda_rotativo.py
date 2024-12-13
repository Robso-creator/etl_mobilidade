from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from src.database.models.base import _template
from src.database.models.base import Base
from src.database.utils import get_indexes
from src.database.utils import mount_config_dict


class PostoVendaRotativo(Base):
    __tablename__ = 'posto_venda_rotativo'

    dict_substitute = {
        'each_line_represents': 'um posto de venda rotativo registrado',
        'freshness': 'Indeterminada',
        'data_source': 'Posto de Venda Rotativo',
        'product': 'Mobilidade Urbana',
    }
    __table_args__ = {
        'comment': _template.substitute(**dict_substitute),
        'schema': 'public',
    }

    id = Column('id', Integer, primary_key=True, nullable=False, comment='Identificador único do posto de venda rotativo')
    id_posto_venda_rotativo = Column('id_posto_venda_rotativo', Integer, comment='Identificador do posto de venda rotativo')
    endereco = Column('endereco', String(100), comment='Endereço do posto de venda rotativo')
    complemento = Column('complemento', String(100), comment='Complemento do endereço')
    geometria = Column('geometria', String, comment='Geometria do posto de venda rotativo')
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

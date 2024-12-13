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


class SinalizacaoSemaforica(Base):
    __tablename__ = 'sinalizacao_semaforica'

    dict_substitute = {
        'each_line_represents': 'uma sinalização semafórica registrada',
        'freshness': 'Indeterminada',
        'data_source': 'Localização das Sinalizações Semafóricas',
        'product': 'Sinalização Semafórica',
    }
    __table_args__ = {
        'comment': _template.substitute(**dict_substitute),
        'schema': 'public',
    }

    id = Column('id', Integer, primary_key=True, nullable=False, comment='Identificador único da sinalização semafórica')
    fid = Column('fid', String(100), comment='ID da sinalização semafórica')
    id_sinalizacao_semaforica = Column('id_sinalizacao_semaforica', Integer, comment='Identificador da sinalização semafórica')
    cod_sinalizacao_semaforica = Column('cod_sinalizacao_semaforica', String(50), comment='Código da sinalização semafórica')
    nome = Column('nome', String(100), comment='Nome da localização da sinalização semafórica')
    tp_travessia_pedestre = Column('tp_travessia_pedestre', String(50), comment='Tipo de travessia de pedestre')
    botoeira = Column('botoeira', Boolean, comment='Indicação de botoeira (True/False)')
    botoeira_sonora = Column('botoeira_sonora', Boolean, comment='Indicação de botoeira sonora (True/False)')
    laco_detector_veicular = Column('laco_detector_veicular', Boolean, comment='Indicação de laço detector veicular (True/False)')
    qtd_tr_c_foco = Column('qtd_tr_c_foco', Integer, comment='Quantidade de travessias com foco')
    qtd_tr_s_foco = Column('qtd_tr_s_foco', Integer, comment='Quantidade de travessias sem foco')
    geometria = Column('geometria', String, comment='Geometria da localização da sinalização semafórica')
    resource_id = Column('resource_id', String, comment='Identificador único do recurso')
    package_id = Column('package_id', String, comment='Identificador único do pacote')
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

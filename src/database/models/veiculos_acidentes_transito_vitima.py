from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from src.database.models.base import _template
from src.database.models.base import Base
from src.database.utils import get_indexes
from src.database.utils import mount_config_dict


class VeiculosAcidentesTransitoVitima(Base):
    __tablename__ = 'veiculos_acidentes_transito_vitima'

    dict_substitute = {
        'each_line_represents': 'um veículo envolvido em um acidente de trânsito com vítima registrado',
        'freshness': 'Indeterminada',
        'data_source': 'Relação dos veículos envolvidos nos acidentes de trânsito com vítima',
        'product': 'Mobilidade Urbana',
    }
    __table_args__ = {
        'comment': _template.substitute(**dict_substitute),
        'schema': 'public',
    }

    id = Column('id', Integer, primary_key=True, nullable=False, comment='Identificador único do veículo')
    numero_boletim = Column('numero_boletim', String(20), comment='Número do boletim de ocorrência')
    data_hora_boletim = Column('data_hora_boletim', DateTime, comment='Data e hora do boletim')
    sequencial_veiculo = Column('sequencial_veiculo', Float, comment='Sequencial do veículo no boletim')
    codigo_categoria = Column('codigo_categoria', Float, comment='Código da categoria do veículo')
    descricao_categoria = Column('descricao_categoria', String(50), comment='Descrição da categoria do veículo')
    codigo_especie = Column('codigo_especie', Float, comment='Código da espécie do veículo')
    descricao_especie = Column('descricao_especie', String(50), comment='Descrição da espécie do veículo')
    codigo_situacao = Column('codigo_situacao', Float, comment='Código da situação do veículo')
    descricao_situacao = Column('descricao_situacao', String(50), comment='Descrição da situação do veículo')
    tipo_socorro = Column('tipo_socorro', Integer, comment='Tipo de socorro')
    descricao_tipo_socorro = Column('descricao_tipo_socorro', String(50), comment='Descrição do tipo de socorro')
    resource_id = Column('resource_id', String, comment='Identificador único do recurso')
    package_id = Column('package_id', String, comment='Identificador único do pacote')
    name = Column('name', String(100), comment='Nome do recurso')
    last_modified = Column('last_modified', DateTime, comment='Data e hora da última modificação')
    nss_boletim = Column('nss_boletim', String, comment='NSS do boletim')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columns, self.keys = get_indexes(self.__table__)

    def get_config_dict(self):
        config = mount_config_dict(self)
        return config

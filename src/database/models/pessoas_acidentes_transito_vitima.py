import pandas as pd
import pandera as pa
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String

from src.database.models.base import _template
from src.database.models.base import Base
from src.database.utils import get_indexes
from src.database.utils import mount_config_dict


class PessoasAcidentesTransitoVitima(Base):
    __tablename__ = 'pessoas_acidentes_transito_vitima'

    dict_substitute = {
        'each_line_represents': 'um envolvido em um acidente de trânsito com vítima registrado',
        'freshness': 'Indeterminada',
        'data_source': 'Relação das pessoas envolvidas nos acidentes de trânsito com vítima',
        'product': 'Segurança Viária',
    }
    __table_args__ = {
        'comment': _template.substitute(**dict_substitute),
        'schema': 'public',
    }

    id = Column('id', Integer, primary_key=True, nullable=False, comment='Identificador único do envolvido')
    num_boletim = Column('num_boletim', String(20), comment='Número do boletim de ocorrência')
    data_hora_boletim = Column('data_hora_boletim', DateTime, comment='Data e hora do boletim')
    no_envolvido = Column('no_envolvido', Integer, comment='Número do envolvido no acidente')
    condutor = Column('condutor', Boolean, comment='Indicador se o envolvido era o condutor')
    cod_severidade = Column('cod_severidade', Integer, comment='Código da severidade do acidente')
    desc_severidade = Column('desc_severidade', String(50), comment='Descrição da severidade do acidente')
    sexo = Column('sexo', String(1), comment='Sexo do envolvido')
    cinto_seguranca = Column('cinto_seguranca', Boolean, comment='Indicador se o envolvido estava usando cinto de segurança')
    embreagues = Column('embreagues', Boolean, comment='Indicador se o envolvido estava embriagado')
    idade = Column('idade', Integer, comment='Idade do envolvido')
    nascimento = Column('nascimento', DateTime, comment='Data de nascimento do envolvido')
    categoria_habilitacao = Column('categoria_habilitacao', String(10), comment='Categoria da habilitação do envolvido')
    descricao_habilitacao = Column('descricao_habilitacao', String(100), comment='Descrição da habilitação do envolvido')
    declaracao_obito = Column('declaracao_obito', Boolean, comment='Indicador se houve declaração de óbito')
    especie_veiculo = Column('especie_veiculo', String(50), comment='Espécie do veículo envolvido')
    pedestre = Column('pedestre', Boolean, comment='Indicador se o envolvido era pedestre')
    passageiro = Column('passageiro', Boolean, comment='Indicador se o envolvido era passageiro')
    resource_id = Column('resource_id', String, comment='Identificador único do recurso')
    package_id = Column('package_id', String, comment='Identificador único do pacote')
    name = Column('name', String(100), comment='Nome do recurso')
    last_modified = Column('last_modified', DateTime, comment='Data e hora da última modificação')

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
                    description='Identificador único do envolvido',
                ),
                'num_boletim': pa.Column(
                    dtype=str,
                    description='Número do boletim de ocorrência',
                ),
                'data_hora_boletim': pa.Column(
                    dtype=pd.Timestamp,
                    description='Data e hora do boletim',
                ),
                'no_envolvido': pa.Column(
                    dtype=int,
                    description='Número do envolvido no acidente',
                ),
                'condutor': pa.Column(
                    dtype=bool,
                    nullable=True,
                    description='Indicador se o envolvido era o condutor',
                ),
                'cod_severidade': pa.Column(
                    dtype=int,
                    description='Código da severidade do acidente',
                ),
                'desc_severidade': pa.Column(
                    dtype=str,
                    description='Descrição da severidade do acidente',
                ),
                'sexo': pa.Column(
                    dtype=str,
                    description='Sexo do envolvido',
                ),
                'cinto_seguranca': pa.Column(
                    dtype=bool,
                    nullable=True,
                    description='Indicador se o envolvido estava usando cinto de segurança',
                ),
                'embreagues': pa.Column(
                    dtype=bool,
                    nullable=True,
                    description='Indicador se o envolvido estava embriagado',
                ),
                'idade': pa.Column(
                    dtype=int,
                    description='Idade do envolvido',
                ),
                'nascimento': pa.Column(
                    dtype=pd.Timestamp,
                    nullable=True,
                    description='Data de nascimento do envolvido',
                ),
                'categoria_habilitacao': pa.Column(
                    dtype=str,
                    description='Categoria da habilitação do envolvido',
                ),
                'descricao_habilitacao': pa.Column(
                    dtype=str,
                    description='Descrição da habilitação do envolvido',
                ),
                'declaracao_obito': pa.Column(
                    dtype=bool,
                    nullable=True,
                    description='Indicador se houve declaração de óbito',
                ),
                'especie_veiculo': pa.Column(
                    dtype=str,
                    description='Espécie do veículo envolvido',
                ),
                'pedestre': pa.Column(
                    dtype=bool,
                    nullable=True,
                    description='Indicador se o envolvido era pedestre',
                ),
                'passageiro': pa.Column(
                    dtype=bool,
                    nullable=True,
                    description='Indicador se o envolvido era passageiro',
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
            },
        )

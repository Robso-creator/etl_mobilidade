"""'main'

Revision ID: 1a7373ae8efd
Revises:
Create Date: 2024-12-13 16:33:21.659717

"""
from typing import Sequence
from typing import Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = '1a7373ae8efd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'circulacao_viaria',
        sa.Column('id', sa.Integer(), nullable=False, comment='Identificador único do trecho'),
        sa.Column('id_ntcv', sa.Float(), nullable=True, comment='Identificador NTCV'),
        sa.Column('geometria', sa.String(), nullable=True, comment='Geometria do trecho'),
        sa.Column('resource_id', sa.String(), nullable=True, comment='Identificador único do recurso'),
        sa.Column('package_id', sa.String(), nullable=True, comment='Identificador único do pacote'),
        sa.Column('name', sa.String(length=100), nullable=True, comment='Nome do trecho'),
        sa.Column('last_modified', sa.DateTime(), nullable=True, comment='Data e hora da última modificação'),
        sa.Column('id_tcv', sa.Float(), nullable=True, comment='Identificador TCV'),
        sa.Column('tipo_trecho_circulacao', sa.String(length=50), nullable=True, comment='Tipo de trecho de circulação'),
        sa.Column('tipo_logradouro', sa.String(length=50), nullable=True, comment='Tipo de logradouro'),
        sa.Column('logradouro', sa.String(length=100), nullable=True, comment='Logradouro'),
        sa.Column('id_no_circ_inicial', sa.Float(), nullable=True, comment='Identificador do nó inicial'),
        sa.Column('id_no_circ_final', sa.Float(), nullable=True, comment='Identificador do nó final'),
        sa.Column('easting', sa.Float(), nullable=True, comment='Coordenada Easting'),
        sa.Column('northing', sa.Float(), nullable=True, comment='Coordenada Northing'),
        sa.Column('latitude', sa.Float(), nullable=True, comment='Latitude'),
        sa.Column('longitude', sa.Float(), nullable=True, comment='Longitude'),
        sa.PrimaryKeyConstraint('id'),
        schema='public',
        comment='\nCaracterísticas da tabela:  \n\n__cada linha representa__: um trecho de circulação registrado \n\n__frequência de atualização dos dados__: Indeterminada \n\n__fonte de dados__: Circulação Viária - Nó do Trecho \n\n__produto__: Mobilidade Urbana \n\n',
    )
    op.create_table(
        'estacionamento_rotativo',
        sa.Column('id', sa.Integer(), nullable=False, comment='Identificador único do estacionamento'),
        sa.Column('fid', sa.String(length=100), nullable=True, comment='ID do estacionamento rotativo'),
        sa.Column('id_estacionamento', sa.Integer(), nullable=True, comment='Identificador do estacionamento'),
        sa.Column('numero_vagas_fisicas', sa.Integer(), nullable=True, comment='Número de vagas físicas'),
        sa.Column('numero_vagas_rotativas', sa.Integer(), nullable=True, comment='Número de vagas rotativas'),
        sa.Column('tempo_permanencia', sa.String(length=50), nullable=True, comment='Tempo máximo de permanência'),
        sa.Column('logradouro', sa.String(length=100), nullable=True, comment='Nome do logradouro'),
        sa.Column('referencia_logradouro', sa.String(length=100), nullable=True, comment='Referência do logradouro'),
        sa.Column('bairro', sa.String(length=50), nullable=True, comment='Bairro do estacionamento'),
        sa.Column('geometria', sa.String(), nullable=True, comment='Geometria do estacionamento'),
        sa.Column('periodo_valido_regra_operacao', sa.String(length=50), nullable=True, comment='Período válido de operação'),
        sa.Column('dia_regra_operacao', sa.String(length=50), nullable=True, comment='Dias da semana de operação'),
        sa.Column('resource_id', sa.String(), nullable=True, comment='Identificador do recurso'),
        sa.Column('package_id', sa.String(), nullable=True, comment='Identificador do pacote'),
        sa.Column('name', sa.String(length=100), nullable=True, comment='Nome do estacionamento'),
        sa.Column('last_modified', sa.DateTime(), nullable=True, comment='Data e hora da última modificação'),
        sa.Column('easting', sa.Float(), nullable=True, comment='Coordenada Easting'),
        sa.Column('northing', sa.Float(), nullable=True, comment='Coordenada Northing'),
        sa.Column('latitude', sa.Float(), nullable=True, comment='Latitude'),
        sa.Column('longitude', sa.Float(), nullable=True, comment='Longitude'),
        sa.PrimaryKeyConstraint('id'),
        schema='public',
        comment='\nCaracterísticas da tabela:  \n\n__cada linha representa__: um estacionamento rotativo \n\n__frequência de atualização dos dados__: Indeterminada \n\n__fonte de dados__: Estacionamento Rotativo \n\n__produto__: Mobilidade \n\n',
    )
    op.create_table(
        'estacionamento_rotativo_idoso',
        sa.Column('id', sa.Integer(), nullable=False, comment='Identificador único do estacionamento'),
        sa.Column('fid', sa.String(length=100), nullable=True, comment='ID do estacionamento rotativo'),
        sa.Column('id_edesp', sa.Integer(), nullable=True, comment='Identificador de estacionamento'),
        sa.Column('tipo_estacionamento', sa.String(length=50), nullable=True, comment='Tipo de estacionamento'),
        sa.Column('destinacao_especifica', sa.String(length=50), nullable=True, comment='Destinação específica do estacionamento'),
        sa.Column('dia_regra_operacao', sa.String(length=50), nullable=True, comment='Dias da semana de operação'),
        sa.Column('periodo_valido_regra_operacao', sa.String(length=50), nullable=True, comment='Período válido de operação'),
        sa.Column('numero_vagas_fisicas', sa.Integer(), nullable=True, comment='Número de vagas físicas'),
        sa.Column('numero_vagas_rotativas', sa.Integer(), nullable=True, comment='Número de vagas rotativas'),
        sa.Column('tempo_permanencia', sa.String(length=50), nullable=True, comment='Tempo máximo de permanência'),
        sa.Column('tipo_logradouro', sa.String(length=50), nullable=True, comment='Tipo de logradouro'),
        sa.Column('logradouro', sa.String(length=100), nullable=True, comment='Nome do logradouro'),
        sa.Column('referencia_logradouro', sa.String(length=100), nullable=True, comment='Referência do logradouro'),
        sa.Column('bairro', sa.String(length=50), nullable=True, comment='Bairro do estacionamento'),
        sa.Column('geometria', sa.String(), nullable=True, comment='Geometria do estacionamento'),
        sa.Column('resource_id', sa.String(), nullable=True, comment='Identificador do recurso'),
        sa.Column('package_id', sa.String(), nullable=True, comment='Identificador do pacote'),
        sa.Column('name', sa.String(length=100), nullable=True, comment='Nome do estacionamento'),
        sa.Column('last_modified', sa.DateTime(), nullable=True, comment='Data e hora da última modificação'),
        sa.Column('easting', sa.Float(), nullable=True, comment='Coordenada Easting'),
        sa.Column('northing', sa.Float(), nullable=True, comment='Coordenada Northing'),
        sa.Column('latitude', sa.Float(), nullable=True, comment='Latitude'),
        sa.Column('longitude', sa.Float(), nullable=True, comment='Longitude'),
        sa.PrimaryKeyConstraint('id'),
        schema='public',
        comment='\nCaracterísticas da tabela:  \n\n__cada linha representa__: um estacionamento rotativo para idosos \n\n__frequência de atualização dos dados__: Indeterminada \n\n__fonte de dados__: Localização das Vagas de Estacionamento de Idosos \n\n__produto__: Mobilidade \n\n',
    )
    op.create_table(
        'estacionamento_rotativo_motofrete',
        sa.Column('id', sa.Integer(), nullable=False, comment='Identificador único do estacionamento'),
        sa.Column('fid', sa.String(length=100), nullable=True, comment='ID do estacionamento rotativo'),
        sa.Column('id_edesp', sa.Integer(), nullable=True, comment='Identificador de estacionamento'),
        sa.Column('tipo_estacionamento', sa.String(length=50), nullable=True, comment='Tipo de estacionamento'),
        sa.Column('destinacao_especifica', sa.String(length=50), nullable=True, comment='Destinação específica do estacionamento'),
        sa.Column('dia_regra_operacao', sa.String(length=50), nullable=True, comment='Dias da semana de operação'),
        sa.Column('periodo_valido_regra_operacao', sa.String(length=50), nullable=True, comment='Período válido de operação'),
        sa.Column('numero_vagas_fisicas', sa.Integer(), nullable=True, comment='Número de vagas físicas'),
        sa.Column('numero_vagas_rotativas', sa.Integer(), nullable=True, comment='Número de vagas rotativas'),
        sa.Column('tempo_permanencia', sa.String(length=50), nullable=True, comment='Tempo máximo de permanência'),
        sa.Column('tipo_logradouro', sa.String(length=50), nullable=True, comment='Tipo de logradouro'),
        sa.Column('logradouro', sa.String(length=100), nullable=True, comment='Nome do logradouro'),
        sa.Column('referencia_logradouro', sa.String(length=100), nullable=True, comment='Referência do logradouro'),
        sa.Column('bairro', sa.String(length=50), nullable=True, comment='Bairro do estacionamento'),
        sa.Column('geometria', sa.String(), nullable=True, comment='Geometria do estacionamento'),
        sa.Column('resource_id', sa.String(), nullable=True, comment='Identificador do recurso'),
        sa.Column('package_id', sa.String(), nullable=True, comment='Identificador do pacote'),
        sa.Column('name', sa.String(length=100), nullable=True, comment='Nome do estacionamento'),
        sa.Column('last_modified', sa.DateTime(), nullable=True, comment='Data e hora da última modificação'),
        sa.Column('easting', sa.Float(), nullable=True, comment='Coordenada Easting'),
        sa.Column('northing', sa.Float(), nullable=True, comment='Coordenada Northing'),
        sa.Column('latitude', sa.Float(), nullable=True, comment='Latitude'),
        sa.Column('longitude', sa.Float(), nullable=True, comment='Longitude'),
        sa.PrimaryKeyConstraint('id'),
        schema='public',
        comment='\nCaracterísticas da tabela:  \n\n__cada linha representa__: um estacionamento rotativo para motofrete \n\n__frequência de atualização dos dados__: Indeterminada \n\n__fonte de dados__: Localização das Vagas de Estacionamento para Motofrete \n\n__produto__: Mobilidade \n\n',
    )
    op.create_table(
        'logradouros_acidentes_transito_vitima',
        sa.Column('id', sa.Integer(), nullable=False, comment='Identificador único do logradouro'),
        sa.Column('numero_boletim', sa.String(length=20), nullable=True, comment='Número do boletim de ocorrência'),
        sa.Column('data_hora_boletim', sa.DateTime(), nullable=True, comment='Data e hora do boletim'),
        sa.Column('numero_municipio', sa.Float(), nullable=True, comment='Número do município'),
        sa.Column('nome_municipio', sa.String(length=50), nullable=True, comment='Nome do município'),
        sa.Column('sequencia_logradouros', sa.Float(), nullable=True, comment='Sequência dos logradouros'),
        sa.Column('numero_logradouro', sa.Float(), nullable=True, comment='Número do logradouro'),
        sa.Column('tipo_logradouro', sa.String(length=10), nullable=True, comment='Tipo de logradouro'),
        sa.Column('nome_logradouro', sa.String(length=100), nullable=True, comment='Nome do logradouro'),
        sa.Column('tipo_logradouro_anterior', sa.String(length=10), nullable=True, comment='Tipo do logradouro anterior'),
        sa.Column('numero_bairro', sa.Float(), nullable=True, comment='Número do bairro'),
        sa.Column('nome_bairro', sa.String(length=50), nullable=True, comment='Nome do bairro'),
        sa.Column('tipo_bairro', sa.String(length=2), nullable=True, comment='Tipo do bairro'),
        sa.Column('descricao_tipo_bairro', sa.String(length=20), nullable=True, comment='Descrição do tipo de bairro'),
        sa.Column('numero_imovel', sa.Integer(), nullable=True, comment='Número do imóvel'),
        sa.Column('numero_imovel_proximo', sa.Float(), nullable=True, comment='Número do imóvel próximo'),
        sa.Column('resource_id', sa.String(), nullable=True, comment='Identificador único do recurso'),
        sa.Column('package_id', sa.String(), nullable=True, comment='Identificador único do pacote'),
        sa.Column('name', sa.String(length=100), nullable=True, comment='Nome do recurso'),
        sa.Column('last_modified', sa.DateTime(), nullable=True, comment='Data e hora da última modificação'),
        sa.Column('nome_logradouro_anterior', sa.String(length=100), nullable=True, comment='Nome do logradouro anterior'),
        sa.PrimaryKeyConstraint('id'),
        schema='public',
        comment='\nCaracterísticas da tabela:  \n\n__cada linha representa__: um logradouro onde ocorreu um acidente de trânsito com vítima registrado \n\n__frequência de atualização dos dados__: Indeterminada \n\n__fonte de dados__: Relação dos logradouros dos locais de acidentes de trânsito com vítima \n\n__produto__: Mobilidade Urbana \n\n',
    )
    op.create_table(
        'ocorrencias_acidentes_transito_vitima',
        sa.Column('id', sa.Integer(), nullable=False, comment='Identificador único da ocorrência'),
        sa.Column('numero_boletim', sa.String(length=20), nullable=True, comment='Número do boletim de ocorrência'),
        sa.Column('data_hora_boletim', sa.DateTime(), nullable=True, comment='Data e hora do boletim'),
        sa.Column('data_inclusao', sa.DateTime(), nullable=True, comment='Data de inclusão do boletim'),
        sa.Column('tipo_acidente', sa.String(length=10), nullable=True, comment='Tipo de acidente'),
        sa.Column('desc_tipo_acidente', sa.String(length=50), nullable=True, comment='Descrição do tipo de acidente'),
        sa.Column('cod_tempo', sa.Integer(), nullable=True, comment='Código do tempo'),
        sa.Column('desc_tempo', sa.String(length=20), nullable=True, comment='Descrição do tempo'),
        sa.Column('cod_pavimento', sa.Integer(), nullable=True, comment='Código do pavimento'),
        sa.Column('pavimento', sa.String(length=20), nullable=True, comment='Descrição do pavimento'),
        sa.Column('cod_regional', sa.Integer(), nullable=True, comment='Código da região'),
        sa.Column('desc_regional', sa.String(length=20), nullable=True, comment='Descrição da região'),
        sa.Column('origem_boletim', sa.String(length=20), nullable=True, comment='Origem do boletim'),
        sa.Column('local_sinalizado', sa.Boolean(), nullable=True, comment='Indicador se o local é sinalizado'),
        sa.Column('velocidade_permitida', sa.Integer(), nullable=True, comment='Velocidade permitida no local'),
        sa.Column('easting', sa.Float(), nullable=True, comment='Coordenada Easting'),
        sa.Column('northing', sa.Float(), nullable=True, comment='Coordenada Northing'),
        sa.Column('hora_informada', sa.Boolean(), nullable=True, comment='Indicador se a hora foi informada'),
        sa.Column('indicador_fatalidade', sa.Boolean(), nullable=True, comment='Indicador de fatalidade'),
        sa.Column('valor_ups', sa.Integer(), nullable=True, comment='Valor UPS'),
        sa.Column('descricao_ups', sa.String(length=20), nullable=True, comment='Descrição da UPS'),
        sa.Column('data_alteracao_smsa', sa.DateTime(), nullable=True, comment='Data de alteração pela SMSA'),
        sa.Column('valor_ups_antiga', sa.Integer(), nullable=True, comment='Valor da UPS antiga'),
        sa.Column('descricao_ups_antiga', sa.String(length=20), nullable=True, comment='Descrição da UPS antiga'),
        sa.Column('resource_id', sa.String(), nullable=True, comment='Identificador único do recurso'),
        sa.Column('package_id', sa.String(), nullable=True, comment='Identificador único do pacote'),
        sa.Column('name', sa.String(length=100), nullable=True, comment='Nome do recurso'),
        sa.Column('last_modified', sa.DateTime(), nullable=True, comment='Data e hora da última modificação'),
        sa.Column('latitude', sa.Float(), nullable=True, comment='Latitude'),
        sa.Column('longitude', sa.Float(), nullable=True, comment='Longitude'),
        sa.PrimaryKeyConstraint('id'),
        schema='public',
        comment='\nCaracterísticas da tabela:  \n\n__cada linha representa__: uma ocorrência de acidente de trânsito com vítima registrada \n\n__frequência de atualização dos dados__: Indeterminada \n\n__fonte de dados__: Relação de ocorrências de acidentes de trânsito com vítima \n\n__produto__: Mobilidade Urbana \n\n',
    )
    op.create_table(
        'pessoas_acidentes_transito_vitima',
        sa.Column('id', sa.Integer(), nullable=False, comment='Identificador único do envolvido'),
        sa.Column('num_boletim', sa.String(length=20), nullable=True, comment='Número do boletim de ocorrência'),
        sa.Column('data_hora_boletim', sa.DateTime(), nullable=True, comment='Data e hora do boletim'),
        sa.Column('no_envolvido', sa.Integer(), nullable=True, comment='Número do envolvido no acidente'),
        sa.Column('condutor', sa.Boolean(), nullable=True, comment='Indicador se o envolvido era o condutor'),
        sa.Column('cod_severidade', sa.Integer(), nullable=True, comment='Código da severidade do acidente'),
        sa.Column('desc_severidade', sa.String(length=50), nullable=True, comment='Descrição da severidade do acidente'),
        sa.Column('sexo', sa.String(length=1), nullable=True, comment='Sexo do envolvido'),
        sa.Column('cinto_seguranca', sa.Boolean(), nullable=True, comment='Indicador se o envolvido estava usando cinto de segurança'),
        sa.Column('embreagues', sa.Boolean(), nullable=True, comment='Indicador se o envolvido estava embriagado'),
        sa.Column('idade', sa.Integer(), nullable=True, comment='Idade do envolvido'),
        sa.Column('nascimento', sa.DateTime(), nullable=True, comment='Data de nascimento do envolvido'),
        sa.Column('categoria_habilitacao', sa.String(length=10), nullable=True, comment='Categoria da habilitação do envolvido'),
        sa.Column('descricao_habilitacao', sa.String(length=100), nullable=True, comment='Descrição da habilitação do envolvido'),
        sa.Column('declaracao_obito', sa.Boolean(), nullable=True, comment='Indicador se houve declaração de óbito'),
        sa.Column('especie_veiculo', sa.String(length=50), nullable=True, comment='Espécie do veículo envolvido'),
        sa.Column('pedestre', sa.Boolean(), nullable=True, comment='Indicador se o envolvido era pedestre'),
        sa.Column('passageiro', sa.Boolean(), nullable=True, comment='Indicador se o envolvido era passageiro'),
        sa.Column('resource_id', sa.String(), nullable=True, comment='Identificador único do recurso'),
        sa.Column('package_id', sa.String(), nullable=True, comment='Identificador único do pacote'),
        sa.Column('name', sa.String(length=100), nullable=True, comment='Nome do recurso'),
        sa.Column('last_modified', sa.DateTime(), nullable=True, comment='Data e hora da última modificação'),
        sa.PrimaryKeyConstraint('id'),
        schema='public',
        comment='\nCaracterísticas da tabela:  \n\n__cada linha representa__: um envolvido em um acidente de trânsito com vítima registrado \n\n__frequência de atualização dos dados__: Indeterminada \n\n__fonte de dados__: Relação das pessoas envolvidas nos acidentes de trânsito com vítima \n\n__produto__: Segurança Viária \n\n',
    )
    op.create_table(
        'posto_venda_rotativo',
        sa.Column('id', sa.Integer(), nullable=False, comment='Identificador único do posto de venda rotativo'),
        sa.Column('id_posto_venda_rotativo', sa.Integer(), nullable=True, comment='Identificador do posto de venda rotativo'),
        sa.Column('endereco', sa.String(length=100), nullable=True, comment='Endereço do posto de venda rotativo'),
        sa.Column('complemento', sa.String(length=100), nullable=True, comment='Complemento do endereço'),
        sa.Column('geometria', sa.String(), nullable=True, comment='Geometria do posto de venda rotativo'),
        sa.Column('resource_id', sa.String(), nullable=True, comment='Identificador único do recurso'),
        sa.Column('package_id', sa.String(), nullable=True, comment='Identificador único do pacote'),
        sa.Column('name', sa.String(length=100), nullable=True, comment='Nome do recurso'),
        sa.Column('last_modified', sa.DateTime(), nullable=True, comment='Data e hora da última modificação'),
        sa.Column('easting', sa.Float(), nullable=True, comment='Coordenada Easting'),
        sa.Column('northing', sa.Float(), nullable=True, comment='Coordenada Northing'),
        sa.Column('latitude', sa.Float(), nullable=True, comment='Latitude'),
        sa.Column('longitude', sa.Float(), nullable=True, comment='Longitude'),
        sa.PrimaryKeyConstraint('id'),
        schema='public',
        comment='\nCaracterísticas da tabela:  \n\n__cada linha representa__: um posto de venda rotativo registrado \n\n__frequência de atualização dos dados__: Indeterminada \n\n__fonte de dados__: Posto de Venda Rotativo \n\n__produto__: Mobilidade Urbana \n\n',
    )
    op.create_table(
        'redutor_velocidade',
        sa.Column('id', sa.Integer(), nullable=False, comment='Identificador único do redutor de velocidade'),
        sa.Column('id_redutor_velocidade', sa.Integer(), nullable=True, comment='Identificador do redutor de velocidade'),
        sa.Column('num_projeto_operacional', sa.String(length=50), nullable=True, comment='Número do projeto operacional'),
        sa.Column('endereco_referencia', sa.String(length=100), nullable=True, comment='Endereço de referência do redutor de velocidade'),
        sa.Column('bairro', sa.String(length=50), nullable=True, comment='Bairro onde está localizado o redutor de velocidade'),
        sa.Column('referencia_localizacao', sa.String(length=100), nullable=True, comment='Referência da localização do redutor de velocidade'),
        sa.Column('data_implantacao', sa.DateTime(), nullable=True, comment='Data de implantação do redutor de velocidade'),
        sa.Column('data_ultima_manutencao', sa.DateTime(), nullable=True, comment='Data da última manutenção do redutor de velocidade'),
        sa.Column('geometria', sa.String(), nullable=True, comment='Geometria do redutor de velocidade'),
        sa.Column('resource_id', sa.String(), nullable=True, comment='Identificador único do recurso'),
        sa.Column('package_id', sa.String(), nullable=True, comment='Identificador único do pacote'),
        sa.Column('name', sa.String(length=100), nullable=True, comment='Nome do recurso'),
        sa.Column('last_modified', sa.DateTime(), nullable=True, comment='Data e hora da última modificação'),
        sa.Column('easting', sa.Float(), nullable=True, comment='Coordenada Easting'),
        sa.Column('northing', sa.Float(), nullable=True, comment='Coordenada Northing'),
        sa.Column('latitude', sa.Float(), nullable=True, comment='Latitude'),
        sa.Column('longitude', sa.Float(), nullable=True, comment='Longitude'),
        sa.PrimaryKeyConstraint('id'),
        schema='public',
        comment='\nCaracterísticas da tabela:  \n\n__cada linha representa__: um redutor de velocidade registrado \n\n__frequência de atualização dos dados__: Indeterminada \n\n__fonte de dados__: Redutor de Velocidade \n\n__produto__: Mobilidade Urbana \n\n',
    )
    op.create_table(
        'sinalizacao_semaforica',
        sa.Column('id', sa.Integer(), nullable=False, comment='Identificador único da sinalização semafórica'),
        sa.Column('fid', sa.String(length=100), nullable=True, comment='ID da sinalização semafórica'),
        sa.Column('id_sinalizacao_semaforica', sa.Integer(), nullable=True, comment='Identificador da sinalização semafórica'),
        sa.Column('cod_sinalizacao_semaforica', sa.String(length=50), nullable=True, comment='Código da sinalização semafórica'),
        sa.Column('nome', sa.String(length=100), nullable=True, comment='Nome da localização da sinalização semafórica'),
        sa.Column('tp_travessia_pedestre', sa.String(length=50), nullable=True, comment='Tipo de travessia de pedestre'),
        sa.Column('botoeira', sa.Boolean(), nullable=True, comment='Indicação de botoeira (True/False)'),
        sa.Column('botoeira_sonora', sa.Boolean(), nullable=True, comment='Indicação de botoeira sonora (True/False)'),
        sa.Column('laco_detector_veicular', sa.Boolean(), nullable=True, comment='Indicação de laço detector veicular (True/False)'),
        sa.Column('qtd_tr_c_foco', sa.Integer(), nullable=True, comment='Quantidade de travessias com foco'),
        sa.Column('qtd_tr_s_foco', sa.Integer(), nullable=True, comment='Quantidade de travessias sem foco'),
        sa.Column('geometria', sa.String(), nullable=True, comment='Geometria da localização da sinalização semafórica'),
        sa.Column('resource_id', sa.String(), nullable=True, comment='Identificador único do recurso'),
        sa.Column('package_id', sa.String(), nullable=True, comment='Identificador único do pacote'),
        sa.Column('last_modified', sa.DateTime(), nullable=True, comment='Data e hora da última modificação'),
        sa.Column('easting', sa.Float(), nullable=True, comment='Coordenada Easting'),
        sa.Column('northing', sa.Float(), nullable=True, comment='Coordenada Northing'),
        sa.Column('latitude', sa.Float(), nullable=True, comment='Latitude'),
        sa.Column('longitude', sa.Float(), nullable=True, comment='Longitude'),
        sa.PrimaryKeyConstraint('id'),
        schema='public',
        comment='\nCaracterísticas da tabela:  \n\n__cada linha representa__: uma sinalização semafórica registrada \n\n__frequência de atualização dos dados__: Indeterminada \n\n__fonte de dados__: Localização das Sinalizações Semafóricas \n\n__produto__: Sinalização Semafórica \n\n',
    )
    op.create_table(
        'veiculos_acidentes_transito_vitima',
        sa.Column('id', sa.Integer(), nullable=False, comment='Identificador único do veículo'),
        sa.Column('numero_boletim', sa.String(length=20), nullable=True, comment='Número do boletim de ocorrência'),
        sa.Column('data_hora_boletim', sa.DateTime(), nullable=True, comment='Data e hora do boletim'),
        sa.Column('sequencial_veiculo', sa.Float(), nullable=True, comment='Sequencial do veículo no boletim'),
        sa.Column('codigo_categoria', sa.Float(), nullable=True, comment='Código da categoria do veículo'),
        sa.Column('descricao_categoria', sa.String(length=50), nullable=True, comment='Descrição da categoria do veículo'),
        sa.Column('codigo_especie', sa.Float(), nullable=True, comment='Código da espécie do veículo'),
        sa.Column('descricao_especie', sa.String(length=50), nullable=True, comment='Descrição da espécie do veículo'),
        sa.Column('codigo_situacao', sa.Float(), nullable=True, comment='Código da situação do veículo'),
        sa.Column('descricao_situacao', sa.String(length=50), nullable=True, comment='Descrição da situação do veículo'),
        sa.Column('tipo_socorro', sa.Integer(), nullable=True, comment='Tipo de socorro'),
        sa.Column('descricao_tipo_socorro', sa.String(length=50), nullable=True, comment='Descrição do tipo de socorro'),
        sa.Column('resource_id', sa.String(), nullable=True, comment='Identificador único do recurso'),
        sa.Column('package_id', sa.String(), nullable=True, comment='Identificador único do pacote'),
        sa.Column('name', sa.String(length=100), nullable=True, comment='Nome do recurso'),
        sa.Column('last_modified', sa.DateTime(), nullable=True, comment='Data e hora da última modificação'),
        sa.Column('nss_boletim', sa.String(), nullable=True, comment='NSS do boletim'),
        sa.PrimaryKeyConstraint('id'),
        schema='public',
        comment='\nCaracterísticas da tabela:  \n\n__cada linha representa__: um veículo envolvido em um acidente de trânsito com vítima registrado \n\n__frequência de atualização dos dados__: Indeterminada \n\n__fonte de dados__: Relação dos veículos envolvidos nos acidentes de trânsito com vítima \n\n__produto__: Mobilidade Urbana \n\n',
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('veiculos_acidentes_transito_vitima', schema='public')
    op.drop_table('sinalizacao_semaforica', schema='public')
    op.drop_table('redutor_velocidade', schema='public')
    op.drop_table('posto_venda_rotativo', schema='public')
    op.drop_table('pessoas_acidentes_transito_vitima', schema='public')
    op.drop_table('ocorrencias_acidentes_transito_vitima', schema='public')
    op.drop_table('logradouros_acidentes_transito_vitima', schema='public')
    op.drop_table('estacionamento_rotativo_motofrete', schema='public')
    op.drop_table('estacionamento_rotativo_idoso', schema='public')
    op.drop_table('estacionamento_rotativo', schema='public')
    op.drop_table('circulacao_viaria', schema='public')
    # ### end Alembic commands ###
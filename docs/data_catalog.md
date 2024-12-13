# Catalogação de dados do banco de ETL Mobilidade

Hoje temos __1 tabelas__ construídas no banco de dados. A seguir mais detalhes de cada tabela por ordem alfabética:

## 1) __circulacao_trecho__

Características da tabela:

__cada linha representa__: um trecho de circulação registrado

__frequência de atualização dos dados__: Diariamente

__fonte de dados__: Sistema de Gerenciamento de Tráfego

__produto__: Monitoramento de tráfego

__colunas que tornam uma linha única__: id



| Coluna | Tipo | Comentário | Chave Primária | Índice |
| --- | --- | --- |--- |--- |
| __id__ | Inteiro | Identificador único do trecho | Sim |Não |
| __id_ntcv__ | Decimal | Identificador NTCV | Não |Não |
| __geometria__ | Texto | Geometria do trecho | Não |Não |
| __resource_id__ | Texto | Identificador único do recurso | Não |Não |
| __package_id__ | Texto | Identificador único do pacote | Não |Não |
| __name__ | Texto | Nome do trecho | Não |Não |
| __last_modified__ | Data/Hora | Data e hora da última modificação | Não |Não |
| __id_tcv__ | Decimal | Identificador TCV | Não |Não |
| __tipo_trecho_circulacao__ | Texto | Tipo de trecho de circulação | Não |Não |
| __tipo_logradouro__ | Texto | Tipo de logradouro | Não |Não |
| __logradouro__ | Texto | Logradouro | Não |Não |
| __id_no_circ_inicial__ | Decimal | Identificador do nó inicial | Não |Não |
| __id_no_circ_final__ | Decimal | Identificador do nó final | Não |Não |
| __easting__ | Decimal | Coordenada Easting | Não |Não |
| __northing__ | Decimal | Coordenada Northing | Não |Não |
| __latitude__ | Decimal | Latitude | Não |Não |
| __longitude__ | Decimal | Longitude | Não |Não |

# ETL Dados de Mobilidade da Prefeitura de Belo Horizonte
*Projeto elaborado em **72 horas** para realizar a extração, transformação e carga de dados de mobilidade urbana da prefeitura de Belo Horizonte.*

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
![makefile](https://img.shields.io/badge/makefile-enabled-brightgreen?logo=gmail&logoColor=blue)
[![pytest](https://img.shields.io/badge/pytest-enabled-brightgreen?logo=pytest&logoColor=yellow)](https://docs.pytest.org/en/7.4.x/)
[![docker](https://img.shields.io/badge/docker-enabled-brightgreen?logo=docker&logoColor=blue)](https://www.docker.com/)
[![minio](https://img.shields.io/badge/minio-enabled-brightgreen?logo=minio&logoColor=red)](https://min.io/)
[![postgresql](https://img.shields.io/badge/postgresql-enabled-brightgreen?logo=postgresql&logoColor=blue)](https://www.postgresql.org/)

---

## Tabela de Conteúdos

- [Introducao](#introdução)
- [Instalação](#instalação)
- [Uso](#uso)
- [Fluxo de Dados](#fluxo-de-dados)
- [Tecnologias](#tecnologias)
- [Documentação Contínua](#documentaçao-contínua)

___
## Introdução

Este projeto de ETL foi desenvolvido em um prazo de 72 horas com o objetivo de extrair, transformar e carregar
dados de mobilidade urbana fornecidos pela Prefeitura de Belo Horizonte. Utilizando tecnologias modernas como MinIO
para armazenamento de dados, PostgreSQL como Data Warehouse e Python com Pandas para processos ETL, o projeto garante
uma integração eficiente e uma documentação contínua do banco de dados. A infraestrutura é gerenciada com Docker,
assegurando portabilidade e facilidade de implantação. Além disso, o uso de pre-commit e MKDocs reforça a qualidade e a
documentação do código.


---

## Instalação

Passos para instalar e configurar o projeto localmente:

```bash
# Clone o repositório
git clone git@github.com:Robso-creator/etl_mobilidade.git

# Entre no diretório do projeto
cd etl_mobilidade

# Crie uma virtualenv
python3 -m venv venv
. venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

Crie arquivo `.env` no diretório raiz do projeto com as seguintes variáveis de ambiente:

```env
ENV=development

MINIO_ROOT_USER=user
MINIO_ROOT_PASSWORD=password
MINIO_BUCKET=bucket-mobilidade-local

DB_URI=postgresql://postgres:postgres@172.19.0.20:5432/mobilidade
```

---

## Uso

```bash
# Faça a build da imagem
make build-img-local

# Execute o container
make enter-container

# Execute o script
python -m src.pipeline
```

> Acesse o MinIO em [http://localhost:9004](http://localhost:9004) com as credenciais definidas no arquivo `.env` para visualizar os arquivos extraídos/tratados.

---

## Fluxo de Dados

![img](src/assets/fluxograma.png)

---

## Tecnologias

### DataLake

- **MinIO**: Sistema de armazenamento de objetos de código aberto de alto desempenho.

### DataWarehouse

- **Postgres**: Banco de dados relacional de código aberto.
  - **Alembic**: Ferramenta de migração de banco de dados para Python. Todas as tabelas foram criadas via código, garantindo a rastreabilidade e a manutenibilidade do banco de dados.
- **Continuous Documentation**: Documentação contínua do banco de dados, sempre que uma tabela nova é criada, ao realizar o deploy a documentação é atualizada

### ETL

- **Python**: Linguagem de programação de alto nível. Coleta via API aberta, salvando os dados em um arquivo .json na landing.
- **Pandas**: Biblioteca de software escrita como extensão da linguagem de programação Python para manipulação e análise de dados.
    - Landing para Bronze, realizado a troca de formato de arquivo para .csv
    - Bronze para Gold, realizado a limpeza e tratamento dos dados, assim como a sua agregação
    - Gold para DataWarehouse, realizado a carga dos dados tratados no banco de dados em chunks, para evitar consumo exagerado de processamento.

### Infraestrutura

- **Docker**: Plataforma de software que permite a criação, o teste e a implantação de aplicativos rapidamente. Todas as dependências do projeto estão em containers.

### Extras

- **Pre-commit**: Framework para gerenciar e manter ganchos de pre-commit. Garantindo códigos que seguem padrões estabelecidos pela comunidade Python.
- **MKDocs**: É um gerador de sites de documentação estática voltado para projetos de código aberto.
  - **Material**: Tema para o MKDocs.
  - **Deploy no github pages**: Deploy acontece sempre que há merge na main, execução workflow no github actions.
- **Pytest**: Framework de teste para Python. Utilizado para testar as funções do projeto.
  - Execução workflow no github actions quando se cria um Pull Request.

___

## Documentaçao Contínua

**Continuous Documentation** é uma prática que assegura que a documentação esteja sempre atualizada em
tempo real, documentaçã e código andam lado a lado. Pode ser aplicado em diversos contextos, no banco de dados do ETL Mobilidade sempre que uma nova tabela é criada ou há alguma alteração na estrutura do banco de dados, a documentação é
automaticamente atualizada durante o processo de deploy. Isso garante que desenvolvedores e stakeholders sempre tenham
acesso à documentação mais recente, facilitando a compreensão da estrutura e do conteúdo do banco de dados, além de
melhorar a colaboração e a manutenção do sistema. A prática de Continuous Documentation é especialmente útil em
ambientes ágeis onde mudanças frequentes são comuns, garantindo que a documentação nunca fique desatualizada.

Pode acessar a documentação do banco de dados do projeto clicando [aqui](https://robso-creator.github.io/etl_mobilidade/data_catalog).
![Screenshot da Documentação](src/assets/screenshot_documentation.png)

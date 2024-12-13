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

- [Instalação](#instalação)
- [Uso](#uso)
- [Fluxo de Dados](#fluxo-de-dados)

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
```
ENV=development

MINIO_ROOT_USER=user
MINIO_ROOT_PASSWORD=password
MINIO_BUCKET=bucket-mobilidade-local

DB_URI=postgresql://postgres:postgres@localhost:5432/postgres
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

# ETL Mobility Data from Prefeitura de Belo Horizonte
<sub>Não fala Inglês [Clique aqui](https://github.com/Robso-creator/etl_mobilidade/blob/main/README-en.md) para ver
essa página em Português</sub>

*Project developed in **72 hours** to extract, transform, and load urban mobility data from the Prefeitura de Belo Horizonte.*

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
![makefile](https://img.shields.io/badge/makefile-enabled-brightgreen?logo=gmail&logoColor=blue)
[![pytest](https://img.shields.io/badge/pytest-enabled-brightgreen?logo=pytest&logoColor=yellow)](https://docs.pytest.org/en/7.4.x/)
[![docker](https://img.shields.io/badge/docker-enabled-brightgreen?logo=docker&logoColor=blue)](https://www.docker.com/)
[![minio](https://img.shields.io/badge/minio-enabled-brightgreen?logo=minio&logoColor=red)](https://min.io/)
[![postgresql](https://img.shields.io/badge/postgresql-enabled-brightgreen?logo=postgresql&logoColor=blue)](https://www.postgresql.org/)

---

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Data Flow](#data-flow)
- [Technologies](#technologies)
- [Continuous Documentation](#continuous-documentation)

___
## Introduction

This ETL project was developed within 72 hours with the objective of extracting, transforming, and loading urban mobility data provided by the Prefeitura de Belo Horizonte. Using modern technologies like MinIO for data storage, PostgreSQL as the Data Warehouse, and Python with Pandas for ETL processes, the project ensures efficient integration and continuous database documentation. The infrastructure is managed with Docker, ensuring portability and ease of deployment. Additionally, the use of pre-commit and MKDocs enhances the quality and documentation of the code.


---

## Installation

Steps to install and set up the project locally:

```bash
# Clone the repository
git clone git@github.com:Robso-creator/etl_mobilidade.git

# Go into the project directory
cd etl_mobilidade

# Create a virtualenv
python3 -m venv venv
. venv/bin/activate

# Install dependencies
pip install -r requirements/requirements-dev.txt
```
Create a `.env` file in the root directory of the project with the following environment variables:

```env
ENV=development

MINIO_ROOT_USER=user
MINIO_ROOT_PASSWORD=password
MINIO_BUCKET=bucket-mobilidade-local

DB_URI=postgresql://postgres:postgres@172.19.0.20:5432/postgres
```

---

## Usage

```bash
# Build the image
make build-img-local

# Enter the container
make enter-container

# Run the script
python -m src.pipeline
```
> Access MinIO at http://localhost:9004 with the credentials defined in the `.env` file to view the extracted/processed files.

---

## Data Flow

![img](src/assets/fluxograma.png)

___

## Technologies

### DataLake
- MinIO: High-performance open-source object storage system.

### DataWarehouse
- Postgres: Open-source relational database.
  - Alembic: Database migration tool for Python. All tables were created via code, ensuring traceability and maintainability of the database.
- Continuous Documentation: Continuous documentation of the database, automatically updated every time a new table is created during deployment.

### ETL
- Python: High-level programming language. Data collection via open API, saving data in a .json file in the landing area.
- Pandas: Software library written as an extension of Python for data manipulation and analysis.
  - Landing to Bronze, file format changed to .csv
  - Bronze to Gold, data cleaning and treatment, along with aggregation
  - Gold to DataWarehouse, data loaded into the database in chunks to avoid excessive processing consumption.

### Infrastructure

- Docker: Software platform that allows for the quick creation, testing, and deployment of applications. All project dependencies are containerized.

### Extras

- Pre-commit: Framework to manage and maintain pre-commit hooks, ensuring code follows Python community standards.
- MKDocs: Static site generator for project documentation.
  - Material: Theme for MKDocs.
  - Deploy on GitHub Pages: Deployment happens every time there is a merge to the main branch, triggering the GitHub Actions workflow.
- Pytest: Testing framework for Python. Used to test the project's functions.
  - GitHub Actions workflow triggered when a pull request is created.

---

## Continuous Documentation

**Continuous Documentation** is a practice that ensures documentation is always up-to-date in real-time, with documentation and code evolving together. It can be applied in various contexts, and in the ETL Mobility project, every time a new table is created or there are changes to the database structure, the documentation is automatically updated during the deployment process. This ensures developers and stakeholders always have access to the most recent documentation, facilitating the understanding of the database structure and content, and improving collaboration and system maintenance. The practice of Continuous Documentation is especially useful in agile environments where frequent changes are common, ensuring documentation never becomes outdated.

You can access the project's database documentation by clicking [here](https://robso-creator.github.io/etl_mobilidade/data_catalog).
![Documentation Screenshot](src/assets/screenshot_documentation.png)

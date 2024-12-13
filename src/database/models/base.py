from string import Template

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

_template_string = """
Características da tabela:  \n
__cada linha representa__: $each_line_represents \n
__frequência de atualização dos dados__: $freshness \n
__fonte de dados__: $data_source \n
__produto__: $product \n
"""
_template = Template(_template_string)

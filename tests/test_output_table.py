import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

from src.helpers.output_table import send_to_db
from src import settings

@pytest.fixture
def sample_dataframe():
    return pd.DataFrame({
        'col1': [1, 2, 3, 4],
        'col2': ['a', 'b', 'c', 'd']
    })

@pytest.fixture
def mock_engine():
    with patch('src.helpers.output_table.create_engine') as mock_create_engine:
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine
        yield mock_engine

@pytest.fixture
def mock_inspect():
    with patch('src.helpers.output_table.inspect') as mock_inspect:
        yield mock_inspect

@pytest.fixture
def mock_logger():
    with patch('src.helpers.output_table._log') as mock_logger:
        yield mock_logger

def test_send_to_db(sample_dataframe, mock_engine, mock_inspect, mock_logger):
    mock_inspector = MagicMock()
    mock_inspector.get_table_names.return_value = ['test_table']
    mock_inspector.get_columns.return_value = [{'name': 'col1'}, {'name': 'col2'}]
    mock_inspect.return_value = mock_inspector

    send_to_db(sample_dataframe, 'test_table', chunk_size=2)

    mock_inspect.assert_called_once_with(mock_engine)
    mock_inspector.get_table_names.assert_called_once()
    mock_inspector.get_columns.assert_called_once_with('test_table')

    assert mock_logger.info.call_count == 7

def test_send_to_db_table_not_exist(sample_dataframe, mock_engine, mock_inspect, mock_logger):
    mock_inspector = MagicMock()
    mock_inspector.get_table_names.return_value = ['other_table']
    mock_inspect.return_value = mock_inspector

    with pytest.raises(ValueError, match="Tabela 'test_table' não existe no banco de dados"):
        send_to_db(sample_dataframe, 'test_table', chunk_size=2)

def test_send_to_db_sqlalchemy_error(sample_dataframe, mock_engine, mock_inspect, mock_logger):
    mock_inspector = MagicMock()
    mock_inspector.get_table_names.return_value = ['test_table']
    mock_inspector.get_columns.return_value = [{'name': 'col1'}, {'name': 'col2'}]
    mock_inspect.return_value = mock_inspector

    with patch.object(pd.DataFrame, 'to_sql', side_effect=SQLAlchemyError):
        with pytest.raises(SQLAlchemyError):
            send_to_db(sample_dataframe, 'test_table', chunk_size=2)

    assert mock_logger.info.call_count == 4
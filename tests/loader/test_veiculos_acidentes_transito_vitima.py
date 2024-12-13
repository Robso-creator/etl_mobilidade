import pytest
from unittest.mock import patch
import pandas as pd
from src.loader.veiculos_acidentes_transito_vitima import main


@pytest.fixture
def mock_s3():
    with patch('src.loader.veiculos_acidentes_transito_vitima.S3') as MockS3:
        mock_s3 = MockS3.return_value
        yield mock_s3


@pytest.fixture
def mock_send_to_db():
    with patch('src.loader.veiculos_acidentes_transito_vitima.send_to_db') as mock_send:
        yield mock_send


def test_main(mock_s3, mock_send_to_db):
    # Mocking S3 list_files method
    mock_s3.list_files.return_value = (['path/to/file1.csv', 'path/to/file2.csv'], ['file1.csv', 'file2.csv'], None)

    df_mock = pd.DataFrame({'col1': [1, 2], 'col2': ['a', 'b']})
    mock_s3.read_to_df.return_value = df_mock

    main()

    mock_s3.list_files.assert_called_once_with(prefix='gold/relacao-dos-veiculos-envolvidos-nos-acidentes-de-transito-com-vitima')
    assert mock_s3.read_to_df.call_count == 2
    mock_send_to_db.assert_called_once()

    called_df = mock_send_to_db.call_args[0][0]
    assert called_df.shape == (4, 2)
    assert called_df.columns.tolist() == ['col1', 'col2']


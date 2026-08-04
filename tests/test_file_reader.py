from unittest.mock import Mock, patch
import pytest
from src.file_reader import read_csv_file, read_excel_file


@patch("src.file_reader.pd.read_csv")
def test_read_csv_success(mock_read_csv):
    """Тест: успешное чтение CSV."""
    mock_df = Mock()
    mock_df.to_dict.return_value = [{"id": 1, "state": "EXECUTED"}]
    mock_read_csv.return_value = mock_df

    result = read_csv_file("data/transactions.csv")

    assert len(result) == 1
    assert result[0]["id"] == 1
    mock_read_csv.assert_called_once_with("data/transactions.csv")


@patch("src.file_reader.pd.read_csv")
def test_read_csv_multiple_records(mock_read_csv):
    """Тест: чтение CSV с несколькими записями."""
    mock_df = Mock()
    mock_df.to_dict.return_value = [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "CANCELED"}]
    mock_read_csv.return_value = mock_df

    result = read_csv_file("data/transactions.csv")

    assert len(result) == 2
    assert result[1]["state"] == "CANCELED"


@patch("src.file_reader.pd.read_csv")
def test_read_csv_empty(mock_read_csv):
    """Тест: пустой CSV."""
    mock_df = Mock()
    mock_df.to_dict.return_value = []
    mock_read_csv.return_value = mock_df

    result = read_csv_file("data/empty.csv")
    assert result == []


@patch("src.file_reader.pd.read_csv")
def test_read_csv_file_not_found(mock_read_csv):
    """Тест: файл не найден."""
    mock_read_csv.side_effect = FileNotFoundError("File not found")

    with pytest.raises(FileNotFoundError):
        read_csv_file("non_existent.csv")


@patch("src.file_reader.pd.read_excel")
def test_read_excel_success(mock_read_excel):
    """Тест: успешное чтение Excel."""
    mock_df = Mock()
    mock_df.to_dict.return_value = [{"id": 1, "amount": 100}]
    mock_read_excel.return_value = mock_df

    result = read_excel_file("data/test.xlsx")

    assert len(result) == 1
    assert result[0]["id"] == 1
    mock_read_excel.assert_called_once_with("data/test.xlsx", sheet_name=0, index_col=None)


@patch("src.file_reader.pd.read_excel")
def test_read_excel_with_sheet(mock_read_excel):
    """Тест: чтение Excel с указанием листа."""
    mock_df = Mock()
    mock_df.to_dict.return_value = [{"id": 1}]
    mock_read_excel.return_value = mock_df

    read_excel_file("data/test.xlsx", sheet_name="Sheet2")

    mock_read_excel.assert_called_once_with("data/test.xlsx", sheet_name="Sheet2", index_col=None)


@patch("src.file_reader.pd.read_excel")
def test_read_excel_with_index(mock_read_excel):
    """Тест: чтение Excel с указанием индекса."""
    mock_df = Mock()
    mock_df.to_dict.return_value = [{"id": 1}]
    mock_read_excel.return_value = mock_df

    read_excel_file("data/test.xlsx", index_col=0)

    mock_read_excel.assert_called_once_with("data/test.xlsx", sheet_name=0, index_col=0)


@patch("src.file_reader.pd.read_excel")
def test_read_excel_file_not_found(mock_read_excel):
    """Тест: файл не найден."""
    mock_read_excel.side_effect = FileNotFoundError("File not found")

    with pytest.raises(FileNotFoundError):
        read_excel_file("non_existent.xlsx")

"""
Тесты для модуля utils.py с использованием Mock.
"""

import json
from unittest.mock import Mock, patch

from src.utils import load_transactions_from_json


def test_load_transactions_success():
    """Тест: успешная загрузка транзакций."""
    mock_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    mock_json_load = Mock(return_value=mock_data)

    with patch("json.load", mock_json_load):
        with patch("builtins.open"):
            result = load_transactions_from_json("any/path.json")

    assert result == mock_data
    mock_json_load.assert_called_once()


def test_load_transactions_file_not_found():
    """Тест: файл не найден."""
    mock_open = Mock(side_effect=FileNotFoundError)

    with patch("builtins.open", mock_open):
        result = load_transactions_from_json("non_existent.json")

    assert result == []
    mock_open.assert_called_once_with("non_existent.json", "r", encoding="utf-8")


def test_load_transactions_json_decode_error():
    """Тест: ошибка парсинга JSON."""
    mock_json_load = Mock(side_effect=json.JSONDecodeError("Invalid JSON", "", 0))

    with patch("json.load", mock_json_load):
        with patch("builtins.open"):
            result = load_transactions_from_json("any/path.json")

    assert result == []
    mock_json_load.assert_called_once()


def test_load_transactions_not_list():
    """Тест: данные не являются списком."""
    mock_data = {"key": "value"}
    mock_json_load = Mock(return_value=mock_data)

    with patch("json.load", mock_json_load):
        with patch("builtins.open"):
            result = load_transactions_from_json("any/path.json")

    assert result == []
    mock_json_load.assert_called_once()


def test_load_transactions_empty_list():
    """Тест: пустой список в файле."""
    mock_data = []
    mock_json_load = Mock(return_value=mock_data)

    with patch("json.load", mock_json_load):
        with patch("builtins.open"):
            result = load_transactions_from_json("any/path.json")

    assert result == []
    mock_json_load.assert_called_once()

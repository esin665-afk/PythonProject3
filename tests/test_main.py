"""
Тесты для модуля main.py.
"""

from unittest.mock import patch

from src.main import main


@patch('builtins.input')
@patch('src.main.load_transactions_from_json')
def test_main_json_choice(mock_load, mock_input):
    """Тест: выбор JSON-файла."""
    mock_input.side_effect = ["1", "EXECUTED", "нет", "нет", "нет"]
    mock_load.return_value = [{"id": 1, "state": "EXECUTED"}]

    with patch('builtins.print'):
        main()

    mock_load.assert_called_once_with("data/operations.json")


@patch('builtins.input')
def test_main_invalid_choice(mock_input):
    """Тест: неверный выбор меню."""
    mock_input.side_effect = ["5"]

    with patch('builtins.print'):
        main()

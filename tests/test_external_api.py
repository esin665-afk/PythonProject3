"""
Тесты для модуля external_api.py.
"""

from unittest.mock import Mock, patch

import pytest
import requests

from src.external_api import convert_to_rubles


def test_convert_rub():
    """Тест: RUB в RUB (без API)."""
    transaction = {"operationAmount": {"amount": "100.50", "currency": {"code": "RUB"}}}
    result = convert_to_rubles(transaction)
    assert result == 100.50


@patch('src.external_api.requests.get')
def test_convert_success(mock_get):
    """Тест: успешная конвертация через API."""
    # Настраиваем мок для response
    mock_response = mock_get.return_value
    mock_response.json.return_value = {"result": 90.0}
    mock_response.raise_for_status = Mock()  # ← исправлено

    transaction = {"operationAmount": {"amount": "10.00", "currency": {"code": "USD"}}}
    result = convert_to_rubles(transaction)

    assert result == 900.0
    mock_get.assert_called_once()


@patch('src.external_api.requests.get')
def test_convert_api_error(mock_get):
    """Тест: ошибка API → fallback."""
    mock_get.side_effect = requests.RequestException("API Error")

    transaction = {"operationAmount": {"amount": "10.00", "currency": {"code": "USD"}}}
    result = convert_to_rubles(transaction)

    assert result == 900.0


@patch('src.external_api.os.getenv')
def test_convert_no_api_key(mock_getenv):
    """Тест: нет API-ключа → ошибка."""
    mock_getenv.return_value = None

    transaction = {"operationAmount": {"amount": "10.00", "currency": {"code": "USD"}}}
    with pytest.raises(ValueError, match="API_KEY не найден"):
        convert_to_rubles(transaction)

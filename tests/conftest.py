import pytest
from typing import List, Dict, Any


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    """Фикстура с примерами транзакций."""
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 123456789, 'state': 'PENDING', 'date': '2020-01-01T10:00:00.000000'},
    ]


@pytest.fixture
def sample_card_numbers() -> List[str]:
    """Фикстура с номерами карт для тестирования."""
    return [
        "7000792289606361",
        "1234567890123456",
        "0000000000000000",
        "9999999999999999",
    ]


@pytest.fixture
def sample_account_numbers() -> List[str]:
    """Фикстура с номерами счетов для тестирования."""
    return [
        "73654108430135874305",
        "12345678901234567890",
        "00000000000000000000",
        "1234",
    ]


@pytest.fixture
def sample_dates() -> List[str]:
    """Фикстура с датами для тестирования."""
    return [
        "2024-03-11T02:26:18.671407",
        "2025-12-25T10:30:00.000000",
        "1999-01-01T00:00:00.000000",
        "2023-06-15T14:22:30.123456",
    ]
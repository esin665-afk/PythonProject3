import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Visa 7000792289606361", "Visa 7000 79** **** 6361"),
        ("MasterCard 1234567890123456", "MasterCard 1234 56** **** 3456"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 12345678901234567890", "Счет **7890"),
    ],
)
def test_mask_account_card_valid(input_str, expected):
    """Тест корректного маскирования карты или счета."""
    assert mask_account_card(input_str) == expected


def test_mask_account_card_no_space():
    """Тест, когда нет пробела между типом и номером."""
    with pytest.raises(ValueError):
        mask_account_card("Visa7000792289606361")


@pytest.mark.parametrize(
    "input_str",
    [
        "Visa 123",  # слишком короткий номер карты
        "Счет 123",  # слишком короткий номер счета
        "Visa abcdef",  # буквы вместо цифр
        "",  # пустая строка
    ],
)
def test_mask_account_card_invalid(input_str):
    """Тест с некорректными данными."""
    with pytest.raises(ValueError):
        mask_account_card(input_str)


def test_mask_account_card_only_number():
    """Тест, когда передаётся только номер без типа."""
    with pytest.raises(ValueError):
        mask_account_card("7000792289606361")


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2025-12-25T10:30:00.000000", "25.12.2025"),
        ("1999-01-01T00:00:00.000000", "01.01.1999"),
    ],
)
def test_widget_get_date_valid(date_string, expected):
    """Тест корректного преобразования даты."""
    assert get_date(date_string) == expected


@pytest.mark.parametrize(
    "date_string",
    [
        "2024/03/11T02:26:18",
        "2024-03-11",
        "",
        "not a date",
    ],
)
def test_widget_get_date_invalid(date_string):
    """Тест с некорректными форматами даты."""
    with pytest.raises(ValueError):
        get_date(date_string)

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("0000000000000000", "0000 00** **** 0000"),
        ("9999999999999999", "9999 99** **** 9999"),
        (7000792289606361, "7000 79** **** 6361"),  # int
    ],
)
def test_mask_card_number_valid(card_number, expected):
    """Тест корректного маскирования номера карты."""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "card_number",
    [
        "123",  # слишком короткий
        "12345678901234567",  # слишком длинный
        "1234abcd5678",  # содержит буквы
        "",  # пустая строка
    ],
)
def test_mask_card_number_invalid(card_number):
    """Тест с некорректными номерами карт."""
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


def test_mask_card_number_whitespace():
    """Тест с пробелами в начале и конце."""
    assert get_mask_card_number(" 7000792289606361 ") == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("12345678901234567890", "**7890"),
        ("00000000000000000000", "**0000"),
        ("1234", "**1234"),
        (73654108430135874305, "**4305"),  # int
    ],
)
def test_mask_account_valid(account_number, expected):
    """Тест корректного маскирования номера счета."""
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "account_number",
    [
        "123",  # слишком короткий
        "abc",  # содержит буквы
        "",  # пустая строка
    ],
)
def test_mask_account_invalid(account_number):
    """Тест с некорректными номерами счетов."""
    with pytest.raises(ValueError):
        get_mask_account(account_number)


def test_mask_account_whitespace():
    """Тест с пробелами в начале и конце."""
    assert get_mask_account(" 73654108430135874305 ") == "**4305"

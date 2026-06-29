from typing import Union

"""
Модуль для маскирования данных карт и счетов.
"""


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """
    Маскирует номер банковской карты.

    Формат вывода: XXXX XX** **** XXXX
    Видны первые 6 цифр и последние 4 цифры.

    Args:
        card_number: Номер карты (16 цифр).

    Returns:
        Замаскированный номер карты.

    Raises:
        ValueError: Если номер пустой, содержит буквы или длина не 16.

    Example:
        >>> get_mask_card_number("7000792289606361")
        '7000 79** **** 6361'
    """
    ...
    card_str = str(card_number).strip()
    # Проверка на пустую строку
    if not card_str:
        raise ValueError("Номер карты не может быть пустым")

    # Проверка, что строка содержит только цифры
    if not card_str.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")

    # Проверка длины - должно быть ровно 16 цифр
    if len(card_str) != 16:
        raise ValueError(f"Номер карты должен содержать ровно 16 цифр, получено {len(card_str)}")

    # Форматирование: 7000 79** **** 6361
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета.

    Формат вывода: **XXXX
    Видны только последние 4 цифры номера.

    Args:
        account_number (Union[str, int]): Номер счета.

    Returns:
        str: Замаскированный номер счета в формате "**XXXX".

    Raises:
        ValueError: Если номер счета пустой, содержит не цифры или его длина меньше 4.

    Example:
        >>> get_mask_account("73654108430135874305")
        '**4305'

        >>> get_mask_account(12345678901234567890)
        '**7890'
    """
    # Преобразуем в строку
    account_str = str(account_number).strip()

    # Проверка на пустую строку
    if not account_str:
        raise ValueError("Номер счета не может быть пустым")

    # Проверка, что строка содержит только цифры
    if not account_str.isdigit():
        raise ValueError("Номер счета должен содержать только цифры")

    # Проверка длины - должно быть минимум 4 цифры
    if len(account_str) < 4:
        raise ValueError(f"Номер счета должен содержать минимум 4 цифры, получено {len(account_str)}")

    # Показываем две звездочки и последние 4 цифры
    return f"**{account_str[-4:]}"

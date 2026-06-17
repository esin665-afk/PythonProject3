"""
Модуль для маскирования данных карт и счетов.
"""


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты: 7000 79** **** 6361"""
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
    """Маскирует номер счета: **4305"""
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

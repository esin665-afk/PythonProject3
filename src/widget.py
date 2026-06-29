from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_info: str) -> str:
    """
    Маскирует номер банковской карты или счета в строке с указанием типа.

    Функция принимает строку, содержащую тип (например, "Visa", "Mastercard", "Счет")
    и номер карты или счета. Номер маскируется с помощью соответствующих функций:
    - Для карт (16 цифр) используется get_mask_card_number
    - Для счетов (больше 16 цифр) используется get_mask_account

    Args:
        account_card_info (str): Строка с типом и номером, разделённые пробелом.
            Например: "Visa 7000792289606361" или "Счет 73654108430135874305"

    Returns:
        str: Строка с типом и замаскированным номером.
            Например: "Visa 7000 79** **** 6361" или "Счет **4305"

    Raises:
        ValueError: Если строка не содержит тип и номер, разделённые пробелом.

    Example:
        >>> mask_account_card("Visa 7000792289606361")
        'Visa 7000 79** **** 6361'

        >>> mask_account_card("Счет 73654108430135874305")
        'Счет **4305'

        >>> mask_account_card("Mastercard 1234567890123456")
        'Mastercard 1234 56** **** 3456'
    """

    # Разделяем строку на части
    parts = account_card_info.rsplit(" ", 1)

    # Если разделить не удалось (нет пробела), возвращаем исходную строку
    if len(parts) != 2:
        return account_card_info

    name_part, number_part = parts

    # Проверяем, является ли номер номером счета (длинный, более 16 цифр)
    # Или если в названии есть слово "Счет"
    if "Счет" in name_part or len(number_part) > 16:
        masked_number = get_mask_account(number_part)
    else:
        masked_number = get_mask_card_number(number_part)

    return f"{name_part} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует строку с датой из формата ISO в формат ДД.ММ.ГГГГ.

    Args:
        date_string (str): Строка с датой в формате ISO (YYYY-MM-DDTHH:MM:SS.ffffff).

    Returns:
        str: Дата в формате "ДД.ММ.ГГГГ".

    Raises:
        ValueError: Если строка не соответствует формату ISO.

    Example:
        >>> get_date("2024-03-11T02:26:18.671407")
        '11.03.2024'

        >>> get_date("2025-12-25T10:30:00")
        '25.12.2025'
    """

    # Извлекаем часть до 'T' (дата)
    date_part = date_string.split("T")[0]

    # Разделяем на год, месяц, день
    year, month, day = date_part.split("-")

    # Возвращаем в формате ДД.ММ.ГГГГ
    return f"{day}.{month}.{year}"

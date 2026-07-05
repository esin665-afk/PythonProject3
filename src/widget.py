from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_info: str) -> str:
    """
    Маскирует номер банковской карты или счета в строке с указанием типа.

    Args:
        account_card_info (str): Строка с типом и номером, разделённые пробелом.

    Returns:
        str: Строка с типом и замаскированным номером.

    Raises:
        ValueError: Если строка не содержит тип и номер, разделённые пробелом,
                   или номер пустой, или содержит не цифры.

    Examples:
        >>> mask_account_card("Visa 7000792289606361")
        'Visa 7000 79** **** 6361'
        >>> mask_account_card("Счет 73654108430135874305")
        'Счет **4305'
    """
    # Проверка на пустую строку
    if not account_card_info or not account_card_info.strip():
        raise ValueError("Строка не может быть пустой")

    # Разделяем строку на части
    parts = account_card_info.rsplit(" ", 1)

    # Если разделить не удалось (нет пробела) — выбрасываем исключение
    if len(parts) != 2:
        raise ValueError("Неверный формат: ожидается тип и номер через пробел")

    name_part, number_part = parts

    # Проверка, что номер не пустой
    if not number_part or not number_part.strip():
        raise ValueError("Номер карты/счета не может быть пустым")

    # Проверка, что номер состоит только из цифр
    if not number_part.isdigit():
        raise ValueError("Номер должен содержать только цифры")

    # Если в названии есть "Счет" или номер длиннее 16 цифр — маскируем как счет
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
    """
    # Проверяем, что строка содержит "T" (разделитель даты и времени)
    if "T" not in date_string:
        raise ValueError(f"Неверный формат даты: отсутствует разделитель 'T': {date_string}")

    try:
        dt = datetime.fromisoformat(date_string)
        return dt.strftime("%d.%m.%Y")
    except ValueError as e:
        raise ValueError(f"Неверный формат даты: {e}")

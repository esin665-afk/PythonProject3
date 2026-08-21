from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_info: str) -> str:
    """
    Маскирует номер банковской карты или счета в строке с указанием типа.
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
    """
    # Проверяем, что строка содержит "T" (разделитель даты и времени)
    if "T" not in date_string:
        raise ValueError(f"Неверный формат даты: отсутствует разделитель 'T': {date_string}")

    try:
        dt = datetime.fromisoformat(date_string)
        return dt.strftime("%d.%m.%Y")
    except ValueError as e:
        raise ValueError(f"Неверный формат даты: {e}")

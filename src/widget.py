from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_info: str) -> str:
    """
    Принимает строку с типом и номером карты или счета и возвращает замаскированный номер.
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
    Принимает строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает в формате "ДД.ММ.ГГГГ".
    """

    # Извлекаем часть до 'T' (дата)
    date_part = date_string.split("T")[0]

    # Разделяем на год, месяц, день
    year, month, day = date_part.split("-")

    # Возвращаем в формате ДД.ММ.ГГГГ
    return f"{day}.{month}.{year}"

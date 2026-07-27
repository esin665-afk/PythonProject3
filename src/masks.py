import logging
import os
from typing import Union

"""
Модуль для маскирования данных карт и счетов.
"""

# Настройка логирования для модуля masks
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(f"{log_dir}/masks.log", mode='w', encoding='utf-8')
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

masks_logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """
    Маскирует номер банковской карты.
    """

    masks_logger.info("Маскирование номера карты начато")
    card_str = str(card_number).strip()
    # Проверка на пустую строку
    if not card_str:
        masks_logger.error("Номер карты не может быть пустым")
        raise ValueError("Номер карты не может быть пустым")

    # Проверка, что строка содержит только цифры
    if not card_str.isdigit():
        masks_logger.error(f"Номер карты '{card_str}' содержит не цифры")
        raise ValueError("Номер карты должен содержать только цифры")

    # Проверка длины - должно быть ровно 16 цифр
    if len(card_str) != 16:
        masks_logger.error(f"Номер карты имеет длину {len(card_str)} (ожидается 16)")
        raise ValueError(f"Номер карты должен содержать ровно 16 цифр, получено {len(card_str)}")

    # Форматирование: 7000 79** **** 6361
    result = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    masks_logger.info(f"Успешное маскирование: {result}")
    return result

def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета.

    """
    # Преобразуем в строку
    masks_logger.info("Маскирование номера счета начато")
    account_str = str(account_number).strip()

    # Проверка на пустую строку
    if not account_str:
        masks_logger.error("Номер счета не может быть пустым")
        raise ValueError("Номер счета не может быть пустым")

    # Проверка, что строка содержит только цифры
    if not account_str.isdigit():
        masks_logger.error(f"Номер счета '{account_str}' содержит не цифры")
        raise ValueError("Номер счета должен содержать только цифры")

    # Проверка длины - должно быть минимум 4 цифры
    if len(account_str) < 4:
        masks_logger.error(f"Номер счета имеет длину {len(account_str)} (минимум 4)")
        raise ValueError(f"Номер счета должен содержать минимум 4 цифры, получено {len(account_str)}")

    # Показываем две звездочки и последние 4 цифры
    result = f"**{account_str[-4:]}"
    masks_logger.info(f"Успешное маскирование: {result}")
    return result

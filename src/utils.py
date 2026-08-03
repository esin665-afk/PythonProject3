"""
Модуль utils содержит вспомогательные функции для работы с данными.
"""

import json
import logging
import os
from typing import Any, Dict, List

# Настройка логирования для модуля utils
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(f"{log_dir}/utils.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

utils_logger.addHandler(file_handler)


def load_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает данные о финансовых транзакциях из JSON-файла.
    """
    utils_logger.info(f"Загрузка транзакций из файла: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Если данные — это список, возвращаем его
        if isinstance(data, list):
            utils_logger.info(f"Успешно загружено {len(data)} транзакций")
            return data

        # Если данные не список, возвращаем пустой список
        utils_logger.warning("Данные в файле не являются списком")
        return []

    except FileNotFoundError:
        utils_logger.error(f"Файл не найден: {file_path}")
        return []

    except json.JSONDecodeError as e:
        utils_logger.error(f"Ошибка парсинга JSON: {e}")
        return []

    except UnicodeDecodeError as e:
        utils_logger.error(f"Ошибка кодировки файла: {e}")
        return []

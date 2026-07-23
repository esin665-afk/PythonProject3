"""
Модуль utils содержит вспомогательные функции для работы с данными.
"""

import json
from typing import List, Dict, Any


def load_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает данные о финансовых транзакциях из JSON-файла.

    Args:
        file_path (str): Путь до JSON-файла.

    Returns:
        List[Dict[str, Any]]: Список словарей с транзакциями.
                               Если файл не найден, пуст, содержит не список
                               или повреждён, возвращает пустой список.

    Example:
        >>> transactions = load_transactions_from_json("data/operations.json")
        >>> len(transactions) > 0
        True
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Если данные — это список, возвращаем его
        if isinstance(data, list):
            return data

        # Если данные не список, возвращаем пустой список
        return []

    except (FileNotFoundError, json.JSONDecodeError, UnicodeDecodeError):
        # Файл не найден, повреждён или не может быть прочитан
        return []
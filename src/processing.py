"""
Модуль для обработки данных.
Содержит функции для фильтрации и сортировки транзакций.
"""

import re
from typing import Any, Dict, List


def filter_by_state(transactions: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список транзакций по заданному статусу.
    """
    # Проверка на пустой список
    if not transactions:
        return []

    # Возвращаем новый список с транзакциями, где state соответствует указанному
    return [item for item in transactions if item.get("state") == state]


def sort_by_date(transactions: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список транзакций по дате.
    """
    if not transactions:
        return []

    # Сортировка по ключу 'date'
    # Если в каком-то словаре нет ключа 'date', используется пустая строка
    return sorted(transactions, key=lambda x: x.get("date", ""), reverse=reverse)


def search_by_description(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """
    Ищет транзакции, в описании которых содержится заданная строка (регистронезависимо).
    """
    if not transactions or not search_string:
        return transactions if transactions else []

    # Экранируем специальные символы и делаем поиск регистронезависимым
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)

    return [item for item in transactions if pattern.search(item.get("description", ""))]

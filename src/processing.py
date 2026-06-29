"""
Модуль для обработки данных.
Содержит функции для фильтрации и сортировки транзакций.
"""

from typing import List, Dict, Any


def filter_by_state(transactions: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список транзакций по заданному статусу.
    """
    # Проверка на пустой список
    if not transactions:
        return []

    # Возвращаем новый список с транзакциями, где state соответствует указанному
    return [item for item in transactions if item.get('state') == state]
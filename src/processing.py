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


def sort_by_date(transactions: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список транзакций по дате.
    """
    if not transactions:
        return []

    # Сортировка по ключу 'date'
    # Если в каком-то словаре нет ключа 'date', используется пустая строка
    return sorted(transactions, key=lambda x: x.get('date', ''), reverse=reverse)


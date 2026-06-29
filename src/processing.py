"""
Модуль для обработки данных.
Содержит функции для фильтрации и сортировки транзакций.
"""

from typing import Any, Dict, List


def filter_by_state(transactions: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список транзакций по заданному статусу.

    Args:
        transactions (List[Dict[str, Any]]): Список словарей с транзакциями.
            Каждый словарь должен содержать ключ 'state'.
        state (str): Статус для фильтрации. По умолчанию 'EXECUTED'.

    Returns:
        List[Dict[str, Any]]: Новый список транзакций с указанным статусом.

    Example:
        >>> transactions = [
        ...     {'id': 1, 'state': 'EXECUTED', 'date': '2024-01-01'},
        ...     {'id': 2, 'state': 'PENDING', 'date': '2024-01-02'},
        ...     {'id': 3, 'state': 'EXECUTED', 'date': '2024-01-03'}
        ... ]
        >>> filter_by_state(transactions)
        [{'id': 1, 'state': 'EXECUTED', 'date': '2024-01-01'}, {'id': 3, 'state': 'EXECUTED', 'date': '2024-01-03'}]

        >>> filter_by_state(transactions, 'PENDING')
        [{'id': 2, 'state': 'PENDING', 'date': '2024-01-02'}]
    """
    # Проверка на пустой список
    if not transactions:
        return []

    # Возвращаем новый список с транзакциями, где state соответствует указанному
    return [item for item in transactions if item.get("state") == state]


def sort_by_date(transactions: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список транзакций по дате.

    Args:
        transactions (List[Dict[str, Any]]): Список словарей с транзакциями.
            Каждый словарь должен содержать ключ 'date'.
        reverse (bool): Если True — сортировка по убыванию (сначала новые).
            Если False — сортировка по возрастанию (сначала старые).
            По умолчанию True.

    Returns:
        List[Dict[str, Any]]: Отсортированный список транзакций.

    Example:
        >>> transactions = [
        ...     {'id': 1, 'date': '2024-03-11T10:00:00'},
        ...     {'id': 2, 'date': '2024-03-10T10:00:00'},
        ...     {'id': 3, 'date': '2024-03-12T10:00:00'}
        ... ]
        >>> sort_by_date(transactions)
        [{'id': 3, 'date': '2024-03-12T10:00:00'}, {'id': 1, 'date': '2024-03-11T10:00:00'}, {'id': 2, 'date': '2024-03-10T10:00:00'}]

        >>> sort_by_date(transactions, reverse=False)
        [{'id': 2, 'date': '2024-03-10T10:00:00'}, {'id': 1, 'date': '2024-03-11T10:00:00'}, {'id': 3, 'date': '2024-03-12T10:00:00'}]
    """
    if not transactions:
        return []

    # Сортировка по ключу 'date'
    # Если в каком-то словаре нет ключа 'date', используется пустая строка
    return sorted(transactions, key=lambda x: x.get("date", ""), reverse=reverse)

"""
Модуль generators содержит функции-генераторы для обработки данных банковских транзакций.
"""

from typing import List, Dict, Any, Iterator


def filter_by_currency(
    transactions: List[Dict[str, Any]], currency: str = "USD"
) -> Iterator[Dict[str, Any]]:
    """
    Генератор, который фильтрует транзакции по заданной валюте.

    Args:
        transactions: Список словарей с транзакциями.
        currency: Код валюты для фильтрации (по умолчанию "USD").

    Yields:
        Словарь транзакции, если её валюта совпадает с заданной.

    Example:
        >>> transactions = [
        ...     {"id": 1, "operationAmount": {"currency": {"code": "USD"}}},
        ...     {"id": 2, "operationAmount": {"currency": {"code": "EUR"}}},
        ...     {"id": 3, "operationAmount": {"currency": {"code": "USD"}}},
        ... ]
        >>> usd = filter_by_currency(transactions, "USD")
        >>> next(usd)["id"]
        1
        >>> next(usd)["id"]
        3
    """
    for transaction in transactions:
        try:
            currency_code = (
                transaction
                .get("operationAmount", {})
                .get("currency", {})
                .get("code")
            )
            if currency_code == currency:
                yield transaction
        except (AttributeError, TypeError):
            continue


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генератор, который возвращает описания транзакций.

    Args:
        transactions: Список словарей с транзакциями.

    Yields:
        Строка с описанием транзакции.
    """
    for transaction in transactions:
        description = transaction.get("description")
        if description:
            yield description


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт в заданном диапазоне.

    Аргументы:
        start: Начальное значение (включительно).
        stop: Конечное значение (НЕ включительно).

    Возвращает:
        Номер карты в формате "XXXX XXXX XXXX XXXX".

    Исключения:
        ValueError: Если start < 0, start >= stop или stop > 10000000000000000.

    Пример:
        >>> for card in card_number_generator(1, 5):
        ...     print(card)
        0000 0000 0000 0001
        0000 0000 0000 0002
        0000 0000 0000 0003
        0000 0000 0000 0004
    """
    # Проверка на отрицательное значение
    if start < 0:
        raise ValueError("Начальное значение не может быть отрицательным")

    # Проверка: start должен быть меньше stop
    if start >= stop:
        raise ValueError("Начальное значение должно быть меньше конечного")

    # Проверка максимального значения (16 цифр = 10^16)
    if stop > 10000000000000000:
        raise ValueError("Конечное значение не может превышать 10000000000000000")

    for number in range(start, stop):
        # Форматируем число как 16-значное с ведущими нулями
        formatted = f"{number:016d}"
        # Разбиваем по 4 цифры
        yield f"{formatted[:4]} {formatted[4:8]} {formatted[8:12]} {formatted[12:16]}"
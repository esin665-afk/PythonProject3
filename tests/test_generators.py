"""
Тесты для модуля generators.py.
"""

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

# ============================================================
# ПРИМЕР ВХОДНЫХ ДАННЫХ ИЗ ЗАДАНИЯ
# ============================================================

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229"
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657"
    }
]


# ============================================================
# ТЕСТЫ ДЛЯ filter_by_currency (используют пример из задания)
# ============================================================

def test_filter_by_currency_usd_from_example():
    """Тест: фильтрация по USD из примера в задании."""
    result = list(filter_by_currency(transactions, "USD"))

    # Ожидаем 3 транзакции с USD (id: 939719570, 142264268, 895315941)
    assert len(result) == 3
    assert result[0]["id"] == 939719570
    assert result[1]["id"] == 142264268
    assert result[2]["id"] == 895315941

    # Проверяем, что все транзакции имеют валюту USD
    for tr in result:
        assert tr["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_rub_from_example():
    """Тест: фильтрация по RUB из примера в задании."""
    result = list(filter_by_currency(transactions, "RUB"))

    # Ожидаем 2 транзакции с RUB (id: 873106923, 594226727)
    assert len(result) == 2
    assert result[0]["id"] == 873106923
    assert result[1]["id"] == 594226727

    # Проверяем, что все транзакции имеют валюту RUB
    for tr in result:
        assert tr["operationAmount"]["currency"]["code"] == "RUB"


def test_filter_by_currency_eur_from_example():
    """Тест: фильтрация по EUR (в примере нет EUR)."""
    result = list(filter_by_currency(transactions, "EUR"))
    assert result == []


def test_filter_by_currency_default_from_example():
    """Тест: валюта по умолчанию (USD) из примера."""
    result = list(filter_by_currency(transactions))

    # Ожидаем 3 транзакции с USD
    assert len(result) == 3
    for tr in result:
        assert tr["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_generator_behavior_from_example():
    """Тест: проверка поведения генератора на примере из задания."""
    gen = filter_by_currency(transactions, "USD")

    # Проверяем, что это генератор
    assert hasattr(gen, "__iter__")
    assert hasattr(gen, "__next__")

    # Проверяем пошаговую выдачу
    first = next(gen)
    assert first["id"] == 939719570

    second = next(gen)
    assert second["id"] == 142264268

    third = next(gen)
    assert third["id"] == 895315941

    # Транзакций с USD больше нет
    with pytest.raises(StopIteration):
        next(gen)


# ============================================================
# ТЕСТЫ ДЛЯ transaction_descriptions (используют пример из задания)
# ============================================================

def test_transaction_descriptions_from_example():
    """Тест: получение описаний из примера в задании."""
    result = list(transaction_descriptions(transactions))

    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert result == expected


def test_transaction_descriptions_generator_behavior_from_example():
    """Тест: проверка поведения генератора на примере из задания."""
    gen = transaction_descriptions(transactions)

    assert hasattr(gen, "__iter__")
    assert hasattr(gen, "__next__")

    first = next(gen)
    assert first == "Перевод организации"

    second = next(gen)
    assert second == "Перевод со счета на счет"

    # Проверяем, что можно преобразовать в список
    remaining = list(gen)
    assert len(remaining) == 3


# ============================================================
# ТЕСТЫ ДЛЯ card_number_generator
# ============================================================

@pytest.mark.parametrize("start, stop, expected", [
    (1, 5, [
        '0000 0000 0000 0001',
        '0000 0000 0000 0002',
        '0000 0000 0000 0003',
        '0000 0000 0000 0004',
    ]),
    (5, 10, [
        '0000 0000 0000 0005',
        '0000 0000 0000 0006',
        '0000 0000 0000 0007',
        '0000 0000 0000 0008',
        '0000 0000 0000 0009',
    ]),
    (9999999999999990, 9999999999999995, [
        '9999 9999 9999 9990',
        '9999 9999 9999 9991',
        '9999 9999 9999 9992',
        '9999 9999 9999 9993',
        '9999 9999 9999 9994',
    ]),
    (0, 3, [
        '0000 0000 0000 0000',
        '0000 0000 0000 0001',
        '0000 0000 0000 0002',
    ]),
])
def test_card_number_generator_valid_range(start, stop, expected):
    """Тест: генератор выдает правильные номера карт в диапазоне."""
    result = list(card_number_generator(start, stop))
    assert result == expected


def test_card_number_generator_single():
    """Тест: генерация одного номера."""
    result = list(card_number_generator(5, 6))
    assert result == ['0000 0000 0000 0005']


def test_card_number_generator_format():
    """Тест: проверка формата номеров карт (XXXX XXXX XXXX XXXX)."""
    gen = card_number_generator(1234567890123456, 1234567890123457)
    result = next(gen)

    parts = result.split(' ')
    assert len(parts) == 4
    for part in parts:
        assert len(part) == 4
        assert part.isdigit()
    assert result == '1234 5678 9012 3456'


def test_card_number_generator_edge_cases():
    """Тест: крайние значения диапазона."""
    # Минимальное значение (0)
    result = list(card_number_generator(0, 1))
    assert result == ['0000 0000 0000 0000']

    # Максимальное значение (9999999999999999)
    result = list(card_number_generator(9999999999999999, 10000000000000000))
    assert result == ['9999 9999 9999 9999']


def test_card_number_generator_stop_iteration():
    """Тест: генератор правильно завершает генерацию."""
    gen = card_number_generator(1, 3)
    assert next(gen) == '0000 0000 0000 0001'
    assert next(gen) == '0000 0000 0000 0002'
    with pytest.raises(StopIteration):
        next(gen)


@pytest.mark.parametrize("start, stop", [
    (5, 5),   # start == stop
    (10, 5),  # start > stop
])
def test_card_number_generator_start_ge_stop(start, stop):
    """Тест: ошибка когда start >= stop."""
    with pytest.raises(ValueError, match="Начальное значение должно быть меньше конечного"):
        list(card_number_generator(start, stop))


def test_card_number_generator_negative_start():
    """Тест: ошибка при отрицательном start."""
    with pytest.raises(ValueError, match="Начальное значение не может быть отрицательным"):
        list(card_number_generator(-1, 5))


def test_card_number_generator_stop_too_large():
    """Тест: ошибка когда stop > 10000000000000000."""
    with pytest.raises(ValueError, match="Конечное значение не может превышать 10000000000000000"):
        list(card_number_generator(0, 10000000000000001))


def test_card_number_generator_stop_equals_max():
    """Тест: stop равен максимальному допустимому значению."""
    result = list(card_number_generator(9999999999999999, 10000000000000000))
    assert result == ['9999 9999 9999 9999']


def test_card_number_generator_large_range_limited():
    """Тест: большой диапазон (берём только первые 3)."""
    gen = card_number_generator(9999999999999900, 9999999999999910)

    first_three = []
    for i in range(3):
        first_three.append(next(gen))

    expected = [
        '9999 9999 9999 9900',
        '9999 9999 9999 9901',
        '9999 9999 9999 9902',
    ]
    assert first_three == expected

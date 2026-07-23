"""
Тесты для модуля generators.py.
"""

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

# ============================================================
# ТЕСТЫ ДЛЯ filter_by_currency (используют фикстуру)
# ============================================================

def test_filter_by_currency_usd_from_example(example_transactions_from_homework):
    """Тест: фильтрация по USD из примера в задании."""
    result = list(filter_by_currency(example_transactions_from_homework, "USD"))

    assert len(result) == 3
    assert result[0]["id"] == 939719570
    assert result[1]["id"] == 142264268
    assert result[2]["id"] == 895315941

    for tr in result:
        assert tr["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_rub_from_example(example_transactions_from_homework):
    """Тест: фильтрация по RUB из примера в задании."""
    result = list(filter_by_currency(example_transactions_from_homework, "RUB"))

    assert len(result) == 2
    assert result[0]["id"] == 873106923
    assert result[1]["id"] == 594226727

    for tr in result:
        assert tr["operationAmount"]["currency"]["code"] == "RUB"


def test_filter_by_currency_eur_from_example(example_transactions_from_homework):
    """Тест: фильтрация по EUR (в примере нет EUR)."""
    result = list(filter_by_currency(example_transactions_from_homework, "EUR"))
    assert result == []


def test_filter_by_currency_default_from_example(example_transactions_from_homework):
    """Тест: валюта по умолчанию (USD) из примера."""
    result = list(filter_by_currency(example_transactions_from_homework))

    assert len(result) == 3
    for tr in result:
        assert tr["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_generator_behavior_from_example(example_transactions_from_homework):
    """Тест: проверка поведения генератора на примере из задания."""
    gen = filter_by_currency(example_transactions_from_homework, "USD")

    assert hasattr(gen, "__iter__")
    assert hasattr(gen, "__next__")

    first = next(gen)
    assert first["id"] == 939719570

    second = next(gen)
    assert second["id"] == 142264268

    third = next(gen)
    assert third["id"] == 895315941

    with pytest.raises(StopIteration):
        next(gen)


# ============================================================
# ТЕСТЫ ДЛЯ transaction_descriptions (используют фикстуру)
# ============================================================

def test_transaction_descriptions_from_example(example_transactions_from_homework):
    """Тест: получение описаний из примера в задании."""
    result = list(transaction_descriptions(example_transactions_from_homework))

    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert result == expected


def test_transaction_descriptions_generator_behavior_from_example(example_transactions_from_homework):
    """Тест: проверка поведения генератора на примере из задания."""
    gen = transaction_descriptions(example_transactions_from_homework)

    assert hasattr(gen, "__iter__")
    assert hasattr(gen, "__next__")

    first = next(gen)
    assert first == "Перевод организации"

    second = next(gen)
    assert second == "Перевод со счета на счет"

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
    result = list(card_number_generator(0, 1))
    assert result == ['0000 0000 0000 0000']

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
    (5, 5),
    (10, 5),
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

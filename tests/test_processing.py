import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(sample_transactions):
    """Тест фильтрации по статусу EXECUTED."""
    result = filter_by_state(sample_transactions, 'EXECUTED')
    assert len(result) == 2
    for item in result:
        assert item.get('state') == 'EXECUTED'


def test_filter_by_state_canceled(sample_transactions):
    """Тест фильтрации по статусу CANCELED."""
    result = filter_by_state(sample_transactions, 'CANCELED')
    assert len(result) == 2
    for item in result:
        assert item.get('state') == 'CANCELED'


def test_filter_by_state_pending(sample_transactions):
    """Тест фильтрации по статусу PENDING."""
    result = filter_by_state(sample_transactions, 'PENDING')
    assert len(result) == 1
    for item in result:
        assert item.get('state') == 'PENDING'


@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("CANCELED", 2),
    ("PENDING", 1),
    ("INVALID", 0),
])
def test_filter_by_state_parametrized(sample_transactions, state, expected_count):
    """Параметризованный тест фильтрации по разным статусам."""
    result = filter_by_state(sample_transactions, state)
    assert len(result) == expected_count


def test_filter_by_state_default(sample_transactions):
    """Тест со статусом по умолчанию (EXECUTED)."""
    result = filter_by_state(sample_transactions)
    assert len(result) == 2
    for item in result:
        assert item.get('state') == 'EXECUTED'


def test_filter_by_state_empty_list():
    """Тест с пустым списком."""
    assert filter_by_state([]) == []


def test_filter_by_state_missing_key():
    """Тест, когда в некоторых словарях нет ключа 'state'."""
    transactions = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 2},
        {'id': 3, 'state': 'EXECUTED'},
    ]
    result = filter_by_state(transactions, 'EXECUTED')
    assert len(result) == 2
    assert result[0]['id'] == 1
    assert result[1]['id'] == 3


def test_filter_by_state_no_matches(sample_transactions):
    """Тест, когда нет транзакций с указанным статусом."""
    result = filter_by_state(sample_transactions, 'NOT_EXIST')
    assert result == []

def test_sort_by_date_descending(sample_transactions):
    """Тест сортировки по убыванию (новые сначала)."""
    result = sort_by_date(sample_transactions)
    dates = [item['date'] for item in result]
    for i in range(len(dates) - 1):
        assert dates[i] >= dates[i + 1]

def test_sort_by_date_ascending(sample_transactions):
    """Тест сортировки по возрастанию (старые сначала)."""
    result = sort_by_date(sample_transactions, reverse=False)
    dates = [item['date'] for item in result]
    for i in range(len(dates) - 1):
        assert dates[i] <= dates[i + 1]

def test_sort_by_date_empty_list():
    """Тест с пустым списком."""
    assert sort_by_date([]) == []

def test_sort_by_date_same_dates():
    """Тест с одинаковыми датами."""
    transactions = [
        {'id': 1, 'date': '2024-01-01T10:00:00'},
        {'id': 2, 'date': '2024-01-01T10:00:00'},
        {'id': 3, 'date': '2024-01-02T10:00:00'},
    ]
    result = sort_by_date(transactions)
    # Проверяем, что даты идут в правильном порядке (убывание)
    dates = [item['date'] for item in result]
    assert dates == [
        '2024-01-02T10:00:00',
        '2024-01-01T10:00:00',
        '2024-01-01T10:00:00'
    ]

def test_sort_by_date_missing_key():
    """Тест, когда в некоторых словарях нет ключа 'date'."""
    transactions = [
            {'id': 1, 'date': '2024-01-01T10:00:00'},
            {'id': 2},
            {'id': 3, 'date': '2024-01-03T10:00:00'},
        ]
    result = sort_by_date(transactions)
        # Транзакция без даты должна быть в конце
    assert result[0]['id'] == 3
    assert result[1]['id'] == 1
    assert result[2]['id'] == 2

def test_sort_by_date_unsorted():
    """Тест сортировки произвольного списка транзакций."""
    transactions = [
            {'id': 1, 'date': '2023-01-01T10:00:00'},
            {'id': 2, 'date': '2024-01-01T10:00:00'},
            {'id': 3, 'date': '2022-01-01T10:00:00'},
            {'id': 4, 'date': '2024-06-01T10:00:00'},
        ]
    result = sort_by_date(transactions)
    dates = [item['date'] for item in result]
    expected_order = [
            '2024-06-01T10:00:00',
            '2024-01-01T10:00:00',
            '2023-01-01T10:00:00',
            '2022-01-01T10:00:00',
        ]
    assert dates == expected_order

def test_sort_by_date_single_transaction():
    """Тест с одной транзакцией."""
    transactions = [{'id': 1, 'date': '2024-01-01T10:00:00'}]
    result = sort_by_date(transactions)
    assert len(result) == 1
    assert result[0]['id'] == 1

@pytest.mark.parametrize("reverse, expected_first", [
        (True, 3),  # убывание: сначала самая новая (id 3)
        (False, 1),  # возрастание: сначала самая старая (id 1)
    ])
def test_sort_by_date_parametrized(reverse, expected_first):
    """Параметризованный тест сортировки."""
    transactions = [
            {'id': 1, 'date': '2024-01-01T10:00:00'},
            {'id': 2, 'date': '2024-06-01T10:00:00'},
            {'id': 3, 'date': '2024-12-01T10:00:00'},
        ]
    result = sort_by_date(transactions, reverse=reverse)
    assert result[0]['id'] == expected_first
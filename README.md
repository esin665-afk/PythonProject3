# 💳 PythonProject3

Проект для обработки и маскирования банковских транзакций.

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://python.org)
[![Poetry](https://img.shields.io/badge/Poetry-2.0.0-purple.svg)](https://python-poetry.org)

---

## 📋 Описание проекта

Данный проект предоставляет набор функций для:

- ✅ **Маскирования** номеров банковских карт и счетов  
- ✅ **Преобразования** форматов дат  
- ✅ **Фильтрации** и **сортировки** транзакций  
- ✅ **Обработки** данных банковских операций

---
## 🎯 Цель проекта

**Цель проекта** — разработать набор удобных и надёжных Python-функций для работы с банковскими данными.

Проект решает следующие задачи:

- 🔒 **Безопасность данных** — маскирование номеров карт и счетов для защиты личной информации
- 📅 **Унификация форматов** — преобразование дат в единый читаемый формат
- 🔍 **Анализ транзакций** — фильтрация и сортировка операций для удобного анализа
- 🧪 **Качество кода** — использование линтеров, тестов и проверки типов для надёжности

Проект разработан в рамках учебного курса по Python и демонстрирует навыки:
- Работы с функциями и модулями
- Обработки исключений
- Фильтрации и сортировки данных
- Написания тестов
- Использования инструментов качества кода (`Flake8`, `Black`, `isort`, `mypy`)

---

## 🛠️ Инструкция по установке

### 1. Проверьте версию Python

Убедитесь, что у вас установлен Python **3.12 или выше**:

```bash
python --version
# или
python3 --version
```

Если Python не установлен, скачайте его с [официального сайта](https://www.python.org/downloads/).

---

### 2. Установите Poetry

Poetry — менеджер зависимостей для Python.

**Linux / macOS:**
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

**Windows (PowerShell):**
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

**Проверка установки:**
```bash
poetry --version
```

> **⚠️ Важно:** Не используйте `pip install poetry` — это может вызвать конфликты. Устанавливайте Poetry только через официальный скрипт.

---

### 3. Клонируйте репозиторий

```bash
git clone git@github.com:esin665-afk/PythonProject3.git
cd PythonProject3
```

Если SSH-ключ не настроен, используйте HTTPS:
```bash
git clone https://github.com/esin665-afk/PythonProject3.git
cd PythonProject3
```

---

### 4. Установите зависимости

```bash
poetry install
```

Эта команда установит все основные зависимости и зависимости для разработки (линтеры, тесты).

---

### 5. Активируйте виртуальное окружение

```bash
poetry shell
```

Теперь вы работаете внутри виртуального окружения проекта.

---

### 6. Проверьте установку

Запустите тесты, чтобы убедиться, что всё работает:

```bash
pytest tests/ -v
```

Если все тесты прошли успешно — установка завершена! ✅

---

## Альтернативная установка (без Poetry)

Если вы не используете Poetry:

```bash
# 1. Создать виртуальное окружение
python -m venv venv

# 2. Активировать его
source venv/bin/activate  # Linux / macOS
# или
venv\Scripts\activate     # Windows

# 3. Установить зависимости
pip install -r requirements.txt
```

> **Примечание:** Если `requirements.txt` отсутствует, создайте его:
> ```bash
> poetry export -f requirements.txt --output requirements.txt
> ```

---

## 🔧 Установка инструментов качества кода (опционально)

```bash
poetry install --with lint
```

Или отдельно:
```bash
pip install flake8 black isort mypy
```

---

## ⚠️ Возможные проблемы

| Проблема | Решение |
|----------|---------|
| `poetry: command not found` | Добавьте Poetry в PATH: `export PATH="$HOME/.local/bin:$PATH"` |
| `ModuleNotFoundError: No module named 'src'` | Убедитесь, что вы в корне проекта: `export PYTHONPATH="${PYTHONPATH}:$(pwd)"` |
| Ошибка при установке зависимостей | Обновите Poetry: `poetry self update`, затем повторите `poetry install` |

---

## 📦 Структура проекта (для справки)

```
PythonProject3/
├── src/
│   ├── __init__.py
│   ├── masks.py
│   └── processing.py
├── tests/
│   ├── __init__.py
│   ├── test_masks.py
│   └── test_processing.py
├── .flake8
├── .gitignore
├── pyproject.toml
├── poetry.lock
└── README.md
```

---

## 📖 Инструкции по использованию функций

### Модуль `masks.py` — маскирование данных

#### 1. `get_mask_card_number(card_number: str) -> str`

Маскирует номер банковской карты.

**Формат вывода:** `XXXX XX** **** XXXX`  
**Правила:** видны первые 6 цифр и последние 4 цифры, остальные заменены звёздочками.

**Пример использования:**
```python
from src.masks import get_mask_card_number

card = "7000792289606361"
masked = get_mask_card_number(card)
print(masked)
# Вывод: 7000 79** **** 6361
```

**Обработка ошибок:**
- Если номер содержит меньше 16 цифр → выбрасывается `ValueError`
- Если номер содержит буквы → выбрасывается `ValueError`

---

#### 2. `get_mask_account(account_number: str) -> str`

Маскирует номер банковского счета.

**Формат вывода:** `**XXXX`  
**Правила:** видны только последние 4 цифры номера.

**Пример использования:**
```python
from src.masks import get_mask_account

account = "73654108430135874305"
masked = get_mask_account(account)
print(masked)
# Вывод: **4305
```

**Обработка ошибок:**
- Если номер содержит менее 4 цифр → выбрасывается `ValueError`
- Если номер содержит буквы → выбрасывается `ValueError`

---

#### 3. `get_date(date_string: str) -> str`

Преобразует дату из формата ISO в формат `ДД.ММ.ГГГГ`.

**Входной формат:** `"YYYY-MM-DDTHH:MM:SS.ffffff"`  
**Выходной формат:** `"ДД.ММ.ГГГГ"`

**Пример использования:**
```python
from src.masks import get_date

date_str = "2024-03-11T02:26:18.671407"
formatted = get_date(date_str)
print(formatted)
# Вывод: 11.03.2024
```

**Обработка ошибок:**
- Если строка не соответствует формату ISO → выбрасывается `ValueError`

---

### Модуль `processing.py` — обработка транзакций

#### 4. `filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]`

Фильтрует список транзакций по статусу.

**Параметры:**
- `transactions` — список словарей с транзакциями
- `state` — статус для фильтрации (по умолчанию `"EXECUTED"`)

**Пример использования:**
```python
from src.processing import filter_by_state

transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Фильтр по умолчанию (EXECUTED)
executed = filter_by_state(transactions)
print(executed)
# Вывод: [{'id': 41428829, ...}, {'id': 939719570, ...}]

# Фильтр по статусу CANCELED
canceled = filter_by_state(transactions, 'CANCELED')
print(canceled)
# Вывод: [{'id': 594226727, ...}, {'id': 615064591, ...}]
```

---

#### 5. `sort_by_date(transactions: List[Dict], reverse: bool = True) -> List[Dict]`

Сортирует список транзакций по дате.

**Параметры:**
- `transactions` — список словарей с транзакциями
- `reverse` — порядок сортировки:
  - `True` (по умолчанию) — по убыванию (сначала новые)
  - `False` — по возрастанию (сначала старые)

**Пример использования:**
```python
from src.processing import sort_by_date

transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Сортировка по убыванию (новые сначала)
sorted_desc = sort_by_date(transactions)
print(sorted_desc)
# Вывод: сначала 2019-07-03, затем 2018-10-14, 2018-09-12, 2018-06-30

# Сортировка по возрастанию (старые сначала)
sorted_asc = sort_by_date(transactions, reverse=False)
print(sorted_asc)
# Вывод: сначала 2018-06-30, затем 2018-09-12, 2018-10-14, 2019-07-03
```

---

### 🔄 Комбинированное использование функций

Часто функции применяются вместе: сначала фильтрация, затем сортировка.

**Пример:**
```python
from src.processing import filter_by_state, sort_by_date

transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# 1. Отфильтровать выполненные транзакции
filtered = filter_by_state(transactions, 'EXECUTED')

# 2. Отсортировать их по дате (новые сначала)
sorted_filtered = sort_by_date(filtered)

print(sorted_filtered)
# Вывод: [{'id': 41428829, ...}, {'id': 939719570, ...}]
```

---
## 🧪 Тестирование

Для проверки работоспособности проекта используется библиотека `pytest` с плагином `pytest-cov` для измерения покрытия кода.

### Запуск всех тестов

```bash
poetry run pytest tests/ -v
```

### Запуск конкретного файла с тестами

```bash
poetry run pytest tests/test_masks.py -v
poetry run pytest tests/test_processing.py -v
poetry run pytest tests/test_widget.py -v
```

### Запуск тестов с отчётом о покрытии

```bash
poetry run pytest tests/ --cov=src --cov-report=term-missing
```

### Пример вывода

```
============================= test session starts ==============================
collected 28 items

tests/test_masks.py ............                                       [ 42%]
tests/test_processing.py ........                                      [ 71%]
tests/test_widget.py ........                                          [100%]

============================== 28 passed in 0.15s ==============================
```

### Покрытие кода тестами

Цель проекта — **не менее 80% покрытия**. Для проверки используйте команду:

```bash
poetry run pytest tests/ --cov=src --cov-report=html
```

После этого откройте `htmlcov/index.html` в браузере, чтобы увидеть детальный отчёт по каждой функции и строке кода.

### Структура тестов

```
tests/
├── conftest.py          # Фикстуры для тестов
├── test_masks.py        # Тесты для модуля masks
├── test_processing.py   # Тесты для модуля processing
└── test_widget.py       # Тесты для модуля widget
```

### Что тестируется

| Модуль | Функции | Количество тестов |
|--------|---------|-------------------|
| `masks.py` | `get_mask_card_number`, `get_mask_account`, `get_date` | ~15 |
| `processing.py` | `filter_by_state`, `sort_by_date` | ~10 |
| `widget.py` | `mask_account_card`, `get_date` | ~8 |

Все тесты используют:
- ✅ Фикстуры для общих данных
- ✅ Параметризацию для разных случаев
- ✅ Проверку исключений (`pytest.raises`)
- ✅ Граничные случаи
## 👨‍💻 Автор

**Василий Есин**  
- GitHub: [@esin665-afk](https://github.com/esin665-afk)  
- Email: esin665@mail.ru

---

⭐ Если функции полезны — поставьте звёздочку на GitHub!



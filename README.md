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
src/
├── __init__.py
├── decorators.py         # Декораторы для логирования (НОВЫЙ МОДУЛЬ)
├── generators.py
├── masks.py
├── processing.py
└── widget.py
```

---

## 📖 Инструкции по использованию функций

### Модуль `masks.py` — маскирование данных

#### 1. `get_mask_card_number(card_number: str) -> str`

Маскирует номер банковской карты.

**Формат вывода:** `XXXX XX** **** XXXX`  
**Правила:** видны первые 6 цифр и последние 4 цифры, остальные заменены звёздочками.

**Пример:**
```python
from src.masks import get_mask_card_number

card = "7000792289606361"
masked = get_mask_card_number(card)
print(masked)  # 7000 79** **** 6361
```

---

#### 2. `get_mask_account(account_number: str) -> str`

Маскирует номер банковского счета.

**Формат вывода:** `**XXXX`  
**Правила:** видны только последние 4 цифры.

**Пример:**
```python
from src.masks import get_mask_account

account = "73654108430135874305"
masked = get_mask_account(account)
print(masked)  # **4305
```

---

#### 3. `get_date(date_string: str) -> str`

Преобразует дату из формата ISO в `ДД.ММ.ГГГГ`.

**Пример:**
```python
from src.masks import get_date

date_str = "2024-03-11T02:26:18.671407"
formatted = get_date(date_str)
print(formatted)  # 11.03.2024
```

---

### Модуль `processing.py` — обработка транзакций

#### 4. `filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]`

Фильтрует транзакции по статусу.

**Пример:**
```python
from src.processing import filter_by_state

transactions = [
    {'id': 1, 'state': 'EXECUTED'},
    {'id': 2, 'state': 'PENDING'}
]

executed = filter_by_state(transactions)
print(executed)  # [{'id': 1, 'state': 'EXECUTED'}]
```

---

#### 5. `sort_by_date(transactions: List[Dict], reverse: bool = True) -> List[Dict]`

Сортирует транзакции по дате.

**Пример:**
```python
from src.processing import sort_by_date

sorted_transactions = sort_by_date(transactions)
print(sorted_transactions)  # Сначала новые
```

---

### Модуль `widget.py` — обработка строк с картами и счетами

#### 6. `mask_account_card(account_card_info: str) -> str`

Принимает строку с типом и номером карты/счета, возвращает строку с замаскированным номером.

**Пример:**
```python
from src.widget import mask_account_card

result = mask_account_card("Visa 7000792289606361")
print(result)  # Visa 7000 79** **** 6361

result = mask_account_card("Счет 73654108430135874305")
print(result)  # Счет **4305
```

---

### Модуль `generators.py` — функции-генераторы (НОВЫЙ МОДУЛЬ)

#### 7. `filter_by_currency(transactions: List[Dict], currency: str = "USD") -> Iterator[Dict]`

Генератор, фильтрующий транзакции по валюте.

**Пример:**
```python
from src.generators import filter_by_currency

transactions = [
    {"id": 1, "operationAmount": {"currency": {"code": "USD"}}},
    {"id": 2, "operationAmount": {"currency": {"code": "EUR"}}},
    {"id": 3, "operationAmount": {"currency": {"code": "USD"}}},
]

usd = filter_by_currency(transactions, "USD")
for tr in usd:
    print(tr["id"])
# Вывод: 1, 3
```

---

#### 8. `transaction_descriptions(transactions: List[Dict]) -> Iterator[str]`

Генератор, возвращающий описания транзакций.

**Пример:**
```python
from src.generators import transaction_descriptions

transactions = [
    {"description": "Перевод организации"},
    {"description": "Оплата услуг"},
]

descriptions = transaction_descriptions(transactions)
for desc in descriptions:
    print(desc)
# Вывод: Перевод организации, Оплата услуг
```

---

#### 9. `card_number_generator(start: int, stop: int) -> Iterator[str]`

Генератор номеров банковских карт в формате `XXXX XXXX XXXX XXXX`.

**Параметры:**
- `start` — начальное значение (включительно)
- `stop` — конечное значение (не включительно, как в `range()`)

**Пример:**
```python
from src.generators import card_number_generator

for card in card_number_generator(1, 5):
    print(card)
# 0000 0000 0000 0001
# 0000 0000 0000 0002
# 0000 0000 0000 0003
# 0000 0000 0000 0004
```
### Модуль `decorators.py` — декораторы для логирования

#### `log(filename: Optional[str] = None) -> Callable`

Декоратор для автоматического логирования вызовов функций.

**Параметры:**
- `filename` — имя файла для записи логов (если не указан, логи выводятся в консоль)

**Логирование:**
- При успешном выполнении: `имя_функции ok`
- При ошибке: `имя_функции error: тип_ошибки. Inputs: (аргументы), {kwargs}`

**Пример использования:**

```python
from src.decorators import log

# Логирование в консоль
@log()
def my_function(x, y):
    return x + y

my_function(1, 2)
# Вывод в консоль: my_function ok

# Логирование в файл
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)
# mylog.txt: my_function ok
---
### 🔄 Комбинированное использование

```python
from src.generators import filter_by_currency, transaction_descriptions

usd_transactions = filter_by_currency(transactions, "USD")
descriptions = transaction_descriptions(list(usd_transactions))

for desc in descriptions:
    print(desc)
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
poetry run pytest tests/test_generators.py -v
poetry run pytest tests/test_decorators.py -v

### Запуск тестов с отчётом о покрытии

```bash
poetry run pytest tests/ --cov=src --cov-report=term-missing
```

### Пример вывода

============================= test session starts ==============================
collected 38 items

tests/test_masks.py ............ [ 31%]
tests/test_processing.py ........ [ 52%]
tests/test_widget.py ........ [ 73%]
tests/test_generators.py ..... [ 89%]
tests/test_decorators.py ..... [100%]

============================== 38 passed in 0.20s ==============================
### Покрытие кода тестами

Цель проекта — **не менее 80% покрытия**. Для проверки используйте команду:

```bash
poetry run pytest tests/ --cov=src --cov-report=html
```

После этого откройте `htmlcov/index.html` в браузере, чтобы увидеть детальный отчёт по каждой функции и строке кода
### Структура тестов

tests/
├── conftest.py # Общие фикстуры для всех тестов
├── test_masks.py # Тесты для модуля masks
├── test_processing.py # Тесты для модуля processing
├── test_widget.py # Тесты для модуля widget
├── test_generators.py # Тесты для модуля generators
└── test_decorators.py # Тесты для модуля decorators (НОВЫЙ)
### Что тестируется

| Модуль | Функции | Количество тестов |
|--------|---------|-------------------|
| `masks.py` | `get_mask_card_number`, `get_mask_account`, `get_date` | ~15 |
| `processing.py` | `filter_by_state`, `sort_by_date` | ~10 |
| `widget.py` | `mask_account_card` | ~8 |
| `generators.py` | `filter_by_currency`, `transaction_descriptions`, `card_number_generator` | ~18 |
| `decorators.py` | `log` | ~6 |
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



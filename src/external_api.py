"""
Модуль external_api содержит функции для работы с внешними API.
"""

import os
import requests
from dotenv import load_dotenv
from typing import Dict, Any

load_dotenv()


def convert_to_rubles(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с данными транзакции.

    Returns:
        float: Сумма в рублях.
    """
    operation_amount = transaction.get("operationAmount", {})
    amount = float(operation_amount.get("amount", 0))
    currency_code = operation_amount.get("currency", {}).get("code", "RUB")

    if currency_code == "RUB":
        return amount

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY не найден. Установите API_KEY в .env")

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount=1"

    headers = {
        "apikey": api_key
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        data = response.json()
        result = data.get("result")

        if result is None:
            raise ValueError(f"Не удалось получить курс для {currency_code}")

        return amount * float(result)

    except requests.RequestException:
        fallback_rates = {
            "USD": 90.0,
            "EUR": 100.0,
            "RUB": 1.0,
            "CNY": 12.0,
            "GBP": 115.0,
            "JPY": 0.60,
            "CHF": 105.0,
        }
        rate = fallback_rates.get(currency_code, 90.0)
        return amount * rate

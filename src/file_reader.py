"""
Модуль для чтения финансовых транзакций из CSV и XLSX файлов.
"""

from typing import Any, Dict, List, Optional

import pandas as pd


def read_csv_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает CSV-файл и возвращает список словарей с транзакциями.
    """
    df = pd.read_csv(file_path)  # type: ignore
    result = df.to_dict(orient='records')  # type: ignore
    return result  # type: ignore


def read_excel_file(file_path: str, sheet_name: Optional[str] = None, index_col: Optional[int] = None) -> List[Dict[str, Any]]:
    """
    Читает XLSX-файл и возвращает список словарей с транзакциями.
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name, index_col=index_col)  # type: ignore
    result = df.to_dict(orient='records')  # type: ignore
    return result  # type: ignore

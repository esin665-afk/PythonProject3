from typing import Any, Dict, List

import pandas as pd


def read_csv_file(file_path: str) -> List[Dict[str, Any]]:
    """Читает CSV-файл и возвращает список словарей с транзакциями."""
    df = pd.read_csv(file_path)
    return df.to_dict(orient="records")


def read_excel_file(file_path: str, sheet_name: str = 0, index_col: int = None) -> List[Dict[str, Any]]:
    """Читает XLSX-файл и возвращает список словарей с транзакциями."""
    df = pd.read_excel(file_path, sheet_name=sheet_name, index_col=index_col)
    return df.to_dict(orient="records")

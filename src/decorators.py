"""
Модуль decorators содержит декораторы для логирования.
"""

import functools
import os
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable], Callable]:
    """
    Декоратор для логирования вызовов функций.

    Args:
        filename: Имя файла для записи логов.
                 Если None, логи выводятся в консоль.

    Returns:
        Декоратор функции.

    Example:
        @log()
        def my_function():
            pass

        @log("log.txt")
        def my_function():
            pass
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                _write_log(log_message, filename)
                return result
            except Exception as e:
                log_message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                _write_log(log_message, filename)
                raise

        return wrapper

    return decorator


def _write_log(message: str, filename: Optional[str] = None) -> None:
    """
    Записывает сообщение в файл или выводит в консоль.

    Args:
        message: Сообщение для записи.
        filename: Имя файла. Если None, вывод в консоль.
    """
    if filename:
        mode = "a" if os.path.exists(filename) else "w"
        with open(filename, mode, encoding="utf-8") as file:
            file.write(message + "\n")
    else:
        print(message)

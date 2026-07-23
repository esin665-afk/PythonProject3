"""
Тесты для модуля decorators.py.
"""

import os
import tempfile

import pytest

from src.decorators import log


def test_log_decorator_to_console(capsys):
    """Тест: вывод логов в консоль."""

    @log()
    def test_function():
        return "OK"

    result = test_function()
    assert result == "OK"
    captured = capsys.readouterr()
    assert "test_function ok" in captured.out


def test_log_decorator_to_file():
    """Тест: запись логов в файл."""
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, encoding="utf-8") as tmp:
        tmp_path = tmp.name

    @log(tmp_path)
    def test_function():
        return "OK"

    result = test_function()
    assert result == "OK"

    with open(tmp_path, "r", encoding="utf-8") as file:
        content = file.read()
        assert "test_function ok" in content

    os.unlink(tmp_path)


def test_log_decorator_error_to_console(capsys):
    """Тест: логирование ошибки в консоль."""

    @log()
    def test_function():
        raise ValueError("Test error")

    with pytest.raises(ValueError, match="Test error"):
        test_function()

    captured = capsys.readouterr()
    assert "test_function error: Test error" in captured.out


def test_log_decorator_error_to_file():
    """Тест: запись ошибки в файл."""
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, encoding="utf-8") as tmp:
        tmp_path = tmp.name

    @log(tmp_path)
    def test_function():
        raise ValueError("Test error")

    with pytest.raises(ValueError, match="Test error"):
        test_function()

    with open(tmp_path, "r", encoding="utf-8") as file:
        content = file.read()
        assert "test_function error: Test error" in content

    os.unlink(tmp_path)


def test_log_decorator_with_arguments():
    """Тест: логирование с аргументами функции."""

    @log()
    def add(a: int, b: int) -> int:
        return a + b

    result = add(2, 3)
    assert result == 5

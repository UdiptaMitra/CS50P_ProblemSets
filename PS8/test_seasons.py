from seasons import convert
import pytest


def test_valid_output():
    result = convert("2000-01-01")
    assert isinstance(result, str)
    assert "minutes" in result
    assert result[0].isupper()


def test_invalid_format_slashes():
    with pytest.raises(SystemExit):
        convert("2000/01/01")


def test_invalid_format_words():
    with pytest.raises(SystemExit):
        convert("January 1 2000")


def test_invalid_month():
    with pytest.raises(SystemExit):
        convert("2024-99-01")


def test_invalid_day():
    with pytest.raises(SystemExit):
        convert("2024-01-99")


def test_invalid_date():
    with pytest.raises(SystemExit):
        convert("2023-02-29")


def test_future_date():
    with pytest.raises(SystemExit):
        convert("3000-01-01")


def test_empty_input():
    with pytest.raises(SystemExit):
        convert("")


def test_random_text():
    with pytest.raises(SystemExit):
        convert("hello world")


def test_contains_minutes():
    result = convert("2020-01-01")
    assert result.endswith("minutes")

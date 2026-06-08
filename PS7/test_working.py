import pytest
from working import convert


def test_clean_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"


def test_no_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 1 PM") == "00:00 to 13:00"


def test_mixed_minutes():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"


def test_invalid_time():
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to")

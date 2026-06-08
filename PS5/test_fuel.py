"""Reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:
convert expects a str in X/Y format as input, wherein X is a non-negative integer and Y is a positive integer,
and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer,
or if X is greater than Y, then convert should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
gauge expects an int and returns a str that is:
"E" if that int is less than or equal to 1,
"F" if that int is greater than or equal to 99,
and "Z%" otherwise, wherein Z is that same int.
Implement two or more functions that collectively test your implementations of convert and gauge thoroughly,
each of whose names should begin with test_ so that you can execute your tests"""

import pytest
from fuel import convert, gauge


def test_convert_normal():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("2/10") == 20


def test_convert_edge_low():
    assert convert("0/100") == 0


def test_convert_edge_high():
    assert convert("99/100") == 99
    assert convert("100/100") == 100


def test_convert_value_errors():
    with pytest.raises(ValueError):
        convert("5/3")
    with pytest.raises(ValueError):
        convert("-1/4")
    with pytest.raises(ValueError):
        convert("a/5")
    with pytest.raises(ValueError):
        convert("3/b")


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_middle():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(73) == "73%"

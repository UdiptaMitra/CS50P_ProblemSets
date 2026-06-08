"""Reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the below, wherein value expects a str as input and
returns an int, namely 0 if that str starts with “hello”, 20 if that str starts with an “h” (but not “hello”), or 100 otherwise,
treating the str case-insensitively. You can assume that the string passed to the value function will not contain any leading spaces.
Only main should call print.
Implement three or more functions that collectively test your implementation of value thoroughly,
each of whose names should begin with test_ so that you can execute your tests."""

from bank import value


def test_hello():
    assert value("Hello  ") == 0


def test_h():
    assert value("   holly") == 20


def test_noh():
    assert value("kaise ho") == 100

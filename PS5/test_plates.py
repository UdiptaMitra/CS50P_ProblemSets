"""Reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein is_valid still expects a str as
input and returns True if that str meets all requirements and False if it does not, but main is only called if the value of __name__ is "__main__"
Implement four or more functions that collectively test your implementation of is_valid thoroughly,
each of whose names should begin with test_ so that you can execute your tests"""

from plates import is_valid


def test_startwith2letters():
    assert is_valid("50") == 0
    assert is_valid("CS50") == 1


def test_max6char():
    assert is_valid("OUTATIME") == 0
    assert is_valid("NRVOUS") == 1


def test_nummidd():
    assert is_valid("CS50P2") == 0
    assert is_valid("ECto88") == 1


def test_outofscript():
    assert is_valid("PI3.14") == 0


def test_firstnum0():
    assert is_valid("CS05") == 0

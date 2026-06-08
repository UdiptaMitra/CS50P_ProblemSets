"""Reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects a
str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
Implement one or more functions that collectively test your implementation of shorten thoroughly,
each of whose names should begin with test_ so that you can execute your tests"""

from twttr import shorten


def test_words():
    assert shorten("Twitter") == "Twttr"
    assert shorten("hello") == "hll"


def test_vowel():
    assert shorten("aeiouAEIUO") == ""
    assert shorten("bcdfgh") == "bcdfgh"


def test_numbers():
    assert shorten("12340hello") == "12340hll"


def test_puctuation():
    assert (
        shorten(r"hello,.;'/\!`@#$%^&*()_+-={}[]:") == r"hll,.;'/\!`@#$%^&*()_+-={}[]:"
    )

import pytest
from um import count

# -----------------------
# BASIC TESTS
# -----------------------


def test_single_um():
    assert count("um") == 1


def test_um_with_punctuation():
    assert count("Hello, um, world!") == 1


def test_multiple_ums():
    assert count("um um um") == 3


# -----------------------
# CASE INSENSITIVITY
# -----------------------


def test_mixed_case():
    assert count("Um UM uM") == 3


# -----------------------
# ENSURE SUBSTRINGS DO NOT MATCH
# -----------------------


def test_substring_in_word():
    # should NOT count "um" inside yummy or album or umbrella
    assert count("yummy album umbrella") == 0


def test_middle_of_word():
    assert count("grumpy drum hummer") == 0


# -----------------------
# EDGE SPACING CASES
# -----------------------


def test_leading_trailing_spaces():
    assert count("  um  ") == 1


def test_um_with_symbols():
    assert count("**um** @um? (um)") == 3


# -----------------------
# COMPLEX SENTENCES
# -----------------------


def test_sentence():
    assert count("Um... I think, um, maybe you should go?") == 2

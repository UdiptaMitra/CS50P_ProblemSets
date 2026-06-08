r"""It’s not uncommon, in English, at least, to say “um” when trying to, um, think of a word. The more you do it, though, the more
noticeable it tends to be!
Implement a function called count that expects a line of text as input as a str and returns, as an int, the number of times that
“um” appears in that text, case-insensitively, as a word unto itself, not as a substring of some other word.
For instance, given text like hello, um, world, the function should return 1. Text like yummy, though, the function should return 0.
Structure um.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not
import any other libraries. You’re welcome, but not required, to use re and/or sys.
Either before or after you implement count in um.py, additionally implement, in a file called test_um.py, three or more functions
that collectively test your implementation of count thoroughly, each of whose names should begin with test_ so that you can
execute your tests with pytest test_um.py.
Note that \b is the boundary between a \w and a \W character (or vice versa), or between \w at the beginning/end of the string
See thefreedictionary.com/words-containing-um for some words that contain “um”."""

import re


def main():
    print(count(input("Text: ")))


def count(s):
    num = re.findall(r"\bum\b", s.lower())
    return len(num)


if __name__ == "__main__":
    main()

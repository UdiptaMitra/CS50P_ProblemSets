"""Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock. Accordingly, instead of “09:00 to 17:00”,
many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM” is an abbreviation for “ante meridiem” and “PM”
is an abbreviation for “post meridiem”, wherein “meridiem” means midday (i.e., noon).

Conversion Table
Implement a function called convert that expects a str in any of the 12-hour formats below and returns the corresponding str in 24-hour format
(i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each.
Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM
Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid
(e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem;
someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).
Either before or after you implement convert in working.py, additionally implement a test code, three or more functions that collectively
test your implementation of convert thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
pytest test_working.py

Note that you can format an int with leading zeroes with code like
print(f"{n:02}")
wherein, if n is a single digit, it will be prefixed with one 0."""

import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{1,2}))? (AM|PM) to (\d{1,2})(?::(\d{1,2}))? (AM|PM)$"
    match = re.findall(pattern, s)

    if match:
        start = list(match[0][0:3])
        end = list(match[0][3:6])

        hrst = int(start[0])
        hret = int(end[0])
        minst = start[1]
        minet = end[1]

        if start[2] == "" or end[2] == "":
            raise ValueError

        if hrst > 12 or hrst <= 0:
            raise ValueError
        if hret > 12 or hret <= 0:
            raise ValueError

        if minst == "":
            minst = 0
        else:
            minst = int(start[1])
        if minst not in range(60):
            raise ValueError

        if minet == "":
            minet = 0
        else:
            minet = int(end[1])
        if minet not in range(60):
            raise ValueError

        if start[2] == "AM":
            if hrst == 12:
                hrst = 0
        elif start[2] == "PM":
            if hrst != 12:
                hrst += 12

        if end[2] == "AM":
            if hret == 12:
                hret = 0
        elif end[2] == "PM":
            if hret != 12:
                hret += 12

        return f"{hrst:02}:{minst:02} to {hret:02}:{minet:02}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()

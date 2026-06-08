"""Fuel gauges indicate, often with fractions, just how much fuel is in a tank.
For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

Implement a program that prompts the user for a fraction, formatted as X/Y, wherein X is a non-negative integer and Y is a positive integer,
and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
Be sure to catch any exceptions like ValueError or ZeroDivisionError."""

while True:
    try:
        fuel = input("Enter the fuel remaining in X/Y format: ")
        x, y = fuel.split("/")
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError
        if x < 0 or y < 0:
            raise ValueError
        if x > y:
            raise ValueError
        percentage = round((x / y) * 100)
        break

    except ValueError:
        print(
            "Value error either x is negative or grater than y or y is zero or negative"
        )
    except ZeroDivisionError:
        print("denominator can never be 0")

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")

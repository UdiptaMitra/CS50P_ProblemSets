"""And now for my Wizard tip calculator.
— Morty Seinfeld

In the United States, it's customary to leave a tip for your server after dining in a restaurant, typically an amount equal to
15% or more of your meal's cost.
dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit),
remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit),
remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
Assume that the user will input values in the expected formats."""


def dollars_to_float(d):
    dollars = int(d[1:-3]) + 0.01 * int(d[-2:])
    return dollars


def percent_to_float(p):
    percentage = int(p[:-1])
    return percentage * 0.01


dollars = dollars_to_float(input("How much was the meal? (in $xx.xx) "))
percent = percent_to_float(input("What percentage would you like to tip? (in xx%) "))
tip = dollars * percent
print(f"Leave ${tip:.2f}")

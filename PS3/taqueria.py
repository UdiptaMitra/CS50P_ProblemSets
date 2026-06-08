"""One of the most popular places to eat in Harvard Square is Felipe's Taqueria, which offers a menu of entrees, per the dict below,
wherein the value of each key is a price in dollars:

{
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
Implement a program that enables a user to place an order, prompting them for items, one per line,
until the user inputs control-d (which is a common way of ending one's input to a program).
After each inputted item, display the total cost of all items inputted thus far,
prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user's input case insensitively.
Ignore any input that isn't an item. Assume that every item on the menu will be titlecased.

Note that you can detect when the user has inputted control-d by catching an EOFError with code like:
try:
    item = input()
except EOFError:
    ...
You might want to print a new line so that the user's cursor (and subsequent prompt) doesn't remain on the same line as your program's own prompt.

Inputting control-d does not require inputting Enter as well, and so the user's cursor (and subsequent prompt)
might thus remain on the same line as your program's own prompt.
 You can move the user's cursor to a new line by printing \n yourself!
Be sure to avoid or catch any KeyError.
"""

items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}
amount = 0
while True:
    try:
        key = input("Item: ").title()
        if key == "":
            break
        price = items[key]
    except EOFError:
        print()
        break
    except KeyError:
        continue
    except Exception:
        break
    else:
        amount += price
        print(f"${amount:.2f}")

"""Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations:
25 cents, 10 cents, and 5 cents.
Implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input
integers, and ignore any integer that isnt an accepted denomination."""

due = 50
while due > 0:
    amount = int(input("Insert coin:"))
    if amount == 5 or amount == 10 or amount == 25:
        if amount < 50:
            due = due - amount
            if due < 0:
                pass
            else:
                print("Amount due:", due)
    else:
        print("Amount due:", due)
        continue
if due <= 0:
    print("Change owed:", -due)
else:
    pass

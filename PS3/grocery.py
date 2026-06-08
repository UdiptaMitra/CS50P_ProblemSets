"""Suppose that you are in the habit of making a list of items you need from the grocery store.
Implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one's input to a program).
Then output the user's grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.
No need to pluralize the items. Treat the user's input case-insensitively.

Note that you can detect when the user has inputted control-d by catching an EOFError with code like:
try:
    item = input()
except EOFError:
    ...
Odds are you'll want to store your grocery list as a dict.
Be sure to avoid or catch any KeyError.
Note that you can sort a dictionary's keys alphabetically by passing that dictionary as an argument to sorted.
"""

dict1 = {}
while True:
    try:
        item = input()
    except EOFError:
        break
    else:
        if item not in dict1.keys():
            dict1[item] = 1
        else:
            dict1[item] += 1
for key in sorted(dict1):
    print(dict1[key], key.upper())

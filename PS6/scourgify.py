"""“Ah, well,” said Tonks, slamming the trunk’s lid shut, “at least it’s all in. That could do with a bit of cleaning, too.” She pointed her wand at Hedwig’s cage.
 “Scourgify.” A few feathers and droppings vanished.
— Harry Potter and the Order of the Phoenix

Data, too, often needs to be “cleaned,” as by reformatting it, so that values are in a consistent, if not more convenient, format.
Source: en.wikipedia.org/wiki/List_of_Harry_Potter_characters

Even though each “row” in the file has three values (last name, first name, and house), the first two are combined into one “column” (name),
escaped with double quotes, with last name and first name separated by a comma and space.
Not ideal if Hogwarts wants to send a form letter to each student, as via mail merge, since it’d be strange to start a letter with:

Dear Potter, Harry,
Rather than with, for instance:
Dear Harry,

Implement a program that:
Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.
"""

import sys
import csv

hogwarts = []
new = []
if len(sys.argv) < 3:
    sys.exit("Too few arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a csv file")
before = sys.argv[1]
after = sys.argv[2]

try:
    with open(before, "r") as fp:
        reader = csv.DictReader(fp)
        for line in reader:
            hogwarts.append(line)
except FileNotFoundError:
    sys.exit("File not exist")

for item in hogwarts:
    lname, fname = item["name"].split(", ")
    new.append({"first": fname, "last": lname, "house": item["house"]})

try:
    with open(after, "w", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(new)
except FileNotFoundError:
    sys.exit("File not exist")

def yell(word):
    # one argument as str
    print(word.upper())


yell("This is CS50")
print()


def yell(words):
    # one argument as list
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


yell(["This", "is", "CS50"])
print()


def yell(*words):
    # multiple arguments
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


yell("This", "is", "CS50")
print()


def yell(*words):
    # using map()
    uppercased = map(str.upper, words)
    print(*uppercased)


yell("This", "is", "CS50")
print()


def yell(*words):
    # uding list comprehension
    uppercased = [arg.upper() for arg in words]
    print(*uppercased)


yell("This", "is", "CS50")
print()

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

gryffindors = []
# filter uising if else
for student in students:
    if student["house"] == "Gryffindor":
        gryffindors.append(student["name"])
for gryffindor in sorted(gryffindors):
    print(gryffindor)
print()

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]
# filter using list comprehension
for gryffindor in sorted(gryffindors):
    print(gryffindor)
print()


def is_gryffindor(s):
    return s["house"] == "Gryffindor"


# filter() with a user defined function
gryffindors = filter(is_gryffindor, students)
for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
print()

gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)
# filter() with a lambda function
for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
print()

students = ["Hermione", "Harry", "Ron"]

# list of dictionaries using loop
gryffindors = []
for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})
print(gryffindors)
print()

# list comprehension with dictionary elements
gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
print(gryffindors)
print()

# dictionary comprehension
gryffindors = {student: "Gryffindor" for student in students}
print(gryffindors)
print()

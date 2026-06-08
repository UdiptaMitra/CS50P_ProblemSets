"""In Massachusetts, home to Harvard University, it's possible to request a vanity license plate for your car,
with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable
vanity plate; AAA22A would not be acceptable. The first number used cannot be a 0.”
“No periods, spaces, or punctuation marks are allowed.”
Implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or
Invalid if it does not. Assume that any letters in the user input will be uppercase.
Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not.
Assume that s will be a str. You're welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    cond1 = cond2 = cond3 = cond4 = cond5 = 0
    if plate[0].isalpha() or plate[1].isalpha():
        cond1 = 1
    if len(plate) >= 2 and len(plate) <= 6:
        cond2 = 1
    if plate.isalnum():
        cond3 = 1
    plate_num = list(plate)
    num = []
    for i in plate_num:
        if i in "0123456789":
            num.append(i)
    cond5 = 1
    if len(num) == 0:
        cond5 = 1
    elif num[0] == "0":
        cond5 = 0
    for i in plate:
        if i in "0123456789":
            plate = plate.replace(i, " ")
        plate = plate.strip()
        cond4 = 1
        for j in plate:
            if j == " ":
                cond4 = 0
                break
    if cond1 * cond2 * cond3 * cond4 * cond5 == 1:
        return 1
    else:
        return 0


if __name__ == "__main__":
    main()

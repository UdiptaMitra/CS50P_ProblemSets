import re


locations = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}


def main():
    pattern = r"\+\d{1,3} \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    match = re.search(pattern, number)
    if match:
        print("Valid")
    else:
        print("Invalid")


main()

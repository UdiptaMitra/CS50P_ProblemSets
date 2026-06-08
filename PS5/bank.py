"""In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone who isn't greeted with a “hello.”
Kramer is instead greeted with a “hey,” which he insists isn't a “hello,” and so he asks for $100. The bank's manager proposes a compromise:
“You got a greeting that starts with an 'h' how does $20 sound?” Kramer accepts.
Implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0.
If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100.
Ignore any leading whitespace in the user's greeting, and treat the user's greeting case-insensitively.
"""


def main():
    greeting = input("Enter greeting: ")
    point = value(greeting)
    if point == 0:
        print("$0 given as u are greeted with 'hello'")
    elif point == 20:
        print("$20 given as u are greeted with 'h' word")
    else:
        print("$100 given as u are not greeted with 'hello' or any 'h' word")


def value(greeting):
    greeting = greeting.lower().strip()
    if greeting[0:5] == "hello":
        return 0
    elif greeting[0:1] == "h" and greeting[0:5] != "hello":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

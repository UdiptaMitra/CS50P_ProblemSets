"""When texting or tweeting, it's not uncommon to shorten words to save time or space, as by omitting vowels,
much like Twitter was originally called twttr. Implement a program that prompts the user for a str of text and then outputs that
same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""

text = input("Enter a text to shorten it: ")
print("The shortened text is: ")
for i in text:
    if i in "AEIOUaeiou":
        continue
    else:
        print(i, end="")

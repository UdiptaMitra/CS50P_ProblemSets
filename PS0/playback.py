"""Some people have a habit of lecturing speaking rather quickly, and it'd be nice to slow them down,
a la YouTube's 0.75 playback speed, or even by having them pause between words.
Implement a program in Python that prompts the user for input and then outputs that same input,
 replacing each space with ... (i.e., three periods)."""

text = input("Enter a quick speech: ")
print("The slowed down speech is ", text.replace(" ", "..."))

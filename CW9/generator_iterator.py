n = int(input("What's n? "))


def sheep(n):
    # generating huge data without generator will cause function to be terminated
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock


for s in sheep(n):
    print(s)


def sheep(n):
    # using generator with yeild keyword instead of return will release small data at once and it will work
    for i in range(n):
        yield "🐑" * i


for s in sheep(n):
    print(s)

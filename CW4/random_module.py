import random

state_before = random.getstate()
print("State saved:", state_before)

print("getrandbits(8):", random.getrandbits(8))

print("randrange(1, 10, 2):", random.randrange(1, 10, 2))

print("randint(1, 10):", random.randint(1, 10))

items = ["apple", "banana", "cherry"]
print("choice:", random.choice(items))

print("choices:", random.choices(items, weights=[10, 1, 1], k=3))

shuffle_list = [1, 2, 3, 4, 5]
random.shuffle(shuffle_list)
print("shuffle:", shuffle_list)

print("sample:", random.sample(items, k=2))

print("random:", random.random())

print("uniform:", random.uniform(10, 20))

print("triangular:", random.triangular(10, 20, 15))

print("normalvariate:", random.normalvariate(50, 5))

random.seed(10)

random.setstate(state_before)
print("State restored. Next getrandbits(8):", random.getrandbits(8))

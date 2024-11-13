import random

print("Welcome to the heads or tails game.")

coin = random.randint(0, 1)

if coin == 0:
    print("Heads")
else:
    print("Tails")


import random

names = input("Give me everyone's names, seperated by a comma.")
name = names.split(", ")

num = random.randint(0, len(name) - 1)

pay_bill = name[num]

# pay_bill = random.choice(name)

print(f"{pay_bill} is going to pay the meal today.")


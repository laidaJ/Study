print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want?S, M, L:")
add_pepperoni = input("Do you want pepperono?Y, N:")
extra_cheese = input("Do you want extra cheese?Y, N:")

price = 0

if size == "S":
    price += 15
    if add_pepperoni == "Y":
        price += 2
elif size == "M":
    if add_pepperoni == "Y":
        price += 3
    price += 20
elif size == "L":
    price += 25
    if add_pepperoni == "Y":
        price += 3
if extra_cheese == "Y":
    price += 1
print(f"Your final bill is {price}")

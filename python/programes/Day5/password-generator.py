import string
import random
letters = list(string.ascii_letters)
print(letters)
numbers = list(string.digits)
print(numbers)
symbols = list(string.punctuation)
print(symbols)
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

password = ""
for n in range(0, nr_letters):
    password += random.choice(letters) 
for n in range(0, nr_symbols):
    password += random.choice(symbols) 
for n in range(0, nr_numbers):
    password += random.choice(numbers) 

print(password)
password_list = list(password)
random.shuffle(password_list)
print(password_list)

final_password = ""
for char in password_list:
    final_password += char
print(final_password)

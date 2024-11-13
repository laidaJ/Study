def greet():
    print("Hello Python")
    print("Keep up")
    print("Have a nice day")
greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Keep up {name}")
greet_with_name("lesen")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"what is it like in {location}")
greet_with(location = "LongYou", name = "Lesen")

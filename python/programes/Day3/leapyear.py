print("Welcome to leap year calculator.")
year = int(input("Type the year you want to know if it is leap year."))

if year % 4 == 0:
    if year % 400 == 0:
        print(f"{year} year is leap year!")
    elif year % 100 == 0:
        print(f"{year} year is not leap year.")
    else:
        print(f"{year} year is leap year!")
else:
    print(f"{year} year is not leap year.")

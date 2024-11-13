print("Welcome to the tip caculator.")

bill = float(input("what was the total bill? "))
tip_percent = int(input("What percentage tip would you like ti give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_bill = bill + bill * (tip_percent / 100)
each_people_pay = round(total_bill / people, 2)
print(f"Each person should pay: ${each_people_pay}")

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = round(int(weight) / float(height) ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi},you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi},You are normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi},You are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi},You are obese.")
else:
    print(f"Your bmi is {bmi},You are clinically obese.")

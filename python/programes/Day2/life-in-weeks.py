age = input("What is your current age?")
age_int = int(age)
years_remaining = 90 - age_int
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")

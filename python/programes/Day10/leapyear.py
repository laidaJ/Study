print("Welcome to leap year calculator.")

def days_in_month(input_year, input_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if input_year % 4 == 0: 
        if input_year % 400 == 0: 
            month_days[1] = 29 
        elif input_year % 100 == 0:
            month_days[1] = 28
        else:
            month_days[1] = 29 
    output_days = month_days[input_month -1]
    return f"{input_year} {input_month} have {output_days}"

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


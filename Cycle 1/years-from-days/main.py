input_days = int(input("Enter the number of days: "))
years = input_days // 365
months = (input_days - (years * 365)) // 30
days = input_days - (years * 365) - (months * 30)
print(f"{input_days} days is {years} years, {months} months, and {days} days.")
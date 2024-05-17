hourlyWage = float(input("Hourly wage: "))
hoursWorked = float(input("Hourly wage: "))
dayOfTheWeek = input("Day of the week: ")
dailyWages = hourlyWage * hoursWorked

if dayOfTheWeek == 'Sunday':
    print(f"Daily wages: {dailyWages * 2} euros")
else:
    print(f"Daily wages: {dailyWages} euros")

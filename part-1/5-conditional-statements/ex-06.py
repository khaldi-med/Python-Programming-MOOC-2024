userInput = int(input("Please type in a temperature (F): "))
toCelsius = (userInput - 32) * 5/9

if toCelsius >= 0:
    print(f"{userInput} degrees Fahrenheit equals {toCelsius} degrees Celsius")
else:
    print(f"{userInput} degrees Fahrenheit equals {toCelsius} degrees Celsius")
    print("Brr! It's cold in here!")

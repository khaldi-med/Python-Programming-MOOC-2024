number1 = int(input("Enter Number1: "))
number2 = int(input("Enter Number2: "))
operation = input("Chose one Operation 'add' or 'multiply' or 'subtract': ")

if(operation == "add"):
    print(f"{number1} + {number2} = {number1 + number2}")

if(operation == "multiply"):
    print(f"{number1} * {number2} = {number1 * number2}")

if(operation == "subtract"):
    print(f"{number1} - {number2} = {number1 - number2}")

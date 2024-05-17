# Typecasting

number = float(input("Please type in a number: "))

if number < 0:
    input("Please type in a number great than 0: ")
print(f"Integer part: {int(number)}")
print(f"Decimal part: {int(number) - number}")

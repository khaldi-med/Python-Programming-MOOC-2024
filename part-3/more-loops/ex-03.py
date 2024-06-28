# Factorial

number = int(input("Please type in a number: "))

factorial = 1
i = 1
while number > 0:
    while i <= number:
        factorial *= i
        i += 1
        continue
    print(f"The factorial of the number {number} is {factorial}")
    break
if number <= 0:
    print("Thanks and bye!")

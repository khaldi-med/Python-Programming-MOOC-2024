# Factorial

while True:
    number = int(input("Please type in a number: "))
    factorial = 1
    i = 1

    if number <= 0:
        print("Thanks and bye!")
        break
    while i <= number:
        factorial *= i
        i += 1
        continue
    print(f"The factorial of the number {number} is {factorial}")


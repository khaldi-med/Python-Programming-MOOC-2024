# The next leap year

year = int(input("Please type in a year: "))
first_input = year + 1

while True:
    if first_input % 100 == 0:
        if first_input % 400 == 0:
            break
        elif first_input % 4 == 0:
            break
        first_input = first_input + 1

                            print(f"The next leap year after {year} is {first_input}")

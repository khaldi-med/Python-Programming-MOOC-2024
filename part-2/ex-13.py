# Alphabetically in the middle

letr1 = str(input("1st letter: "))
letr2 = str(input("2st letter: "))
letr3 = str(input("3st letter: "))

if letr1 > letr2 and letr1 > letr3:
    if letr2 > letr3:
        print(f"The letter in the middle is {letr3}")
elif letr2 > letr1 and letr2 > letr3:
    if letr1 > letr3:
        print(f"The letter in the middle is {letr1}")
elif letr3 > letr1 and letr3 > letr2:
    if letr1 > letr2:
        print(f"The letter in the middle is {letr1}")
else:
    print(f"The letter in the middle is {letr2}")

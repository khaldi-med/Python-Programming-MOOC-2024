# Underlining

dash = "-"
length = 0

while True:
    string = input("Please type in a string: ")
    length = len(string)

    if string == "":
        break
    print(string)
    print(length * dash)


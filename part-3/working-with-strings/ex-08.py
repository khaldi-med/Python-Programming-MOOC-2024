# Right-aligned

string = input("Please type in a string: ")
astric = "*"
length = 20 - len(string)
print(f"{length * astric}{string}")

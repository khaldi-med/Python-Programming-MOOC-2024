# Substrings, part 1

word = input("Please type in a string: ")
index = 0

while index <= len(word):
    print(word[:index])
    index += 1


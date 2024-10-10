# Substrings, part2

word = input("Please type in a string: ")
length = len(word)

while length >= 0:
    print(word[length:])
    length -= 1

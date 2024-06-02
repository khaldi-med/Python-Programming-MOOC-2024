# Find all the substring

word = input("Please type in a string: ")
substring = input("Please type in a substring: ")

index = 0
while True:
    index = word.find(substring)
    if index == -1:
        break
    word = word[index + 1:]


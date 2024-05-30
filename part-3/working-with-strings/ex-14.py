# Find all the substring

word = input("Word: ")
character = input("Please type in a character: ")

index = 0
while True:
    index = word.find(character)
    if index == -1 or len(word) < index + 3:
        break
    print(word[index:index + 3])
    word = word[index + 1:]

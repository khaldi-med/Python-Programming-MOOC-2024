# Find the first substring

word = input("Please type in a word: ")
character = input("Please type in a character: ")

find_char = word.find(character)

if (find_char != -1) and (len(word) <= find_char + 3):
    print(word[find_char:find_char + 3])

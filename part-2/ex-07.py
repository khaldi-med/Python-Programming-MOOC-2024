# Alphabetically last

word1 = str(input("Please type in the 1st word: "))
word2 = str(input("Please type in the 2st word: "))

if word1 > word2:
    print(f"{word1} comes alphabetically last.")
elif word1 < word2:
    print(f"{word2} comes alphabetically last.")
else:
    print("You gave the same word twice.")


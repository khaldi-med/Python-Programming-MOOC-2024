# Does it contain vowels

word = input("Please type in a string: ")

vowels = ["a", "e", "o"]
index = 0

while index < len(vowels):
    if vowels[index] in word:
        print(vowels[index] + " found")
    else:
        print(vowels[index] + " not found")
        index += 1

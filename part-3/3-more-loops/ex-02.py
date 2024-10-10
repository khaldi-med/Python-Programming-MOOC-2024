#First letters of words

sentence = input("Please type in a sentence: ")

print(sentence[0])
i = 1;
while i < len(sentence):
    if(sentence[i] == " "):
        print(sentence[i + 1])
    i += 1

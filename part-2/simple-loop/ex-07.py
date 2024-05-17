# Story

story = ""
last_word = ""
while True:
    word = input("Please type in a word: ")

                if word == "end":
                    print(story)
                    break
                if word == last_word:
                    print(story)
                    break

story += word + " "
last_word = word

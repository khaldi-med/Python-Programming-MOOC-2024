def first_word(sentence):
    i = 0
    word = ""
    while sentence[i] != " ":
        word += sentence[i]
        i += 1
    return word
    
def second_word(sentence):
    i = 0
    word = ""
    while i < len(sentence) and sentence[i] != " ":
        i += 1
        
    while i < len(sentence) and sentence[i] == " ":
        i += 1
        
    while i < len(sentence) and sentence[i] != " ":
        word += sentence[i]
        i += 1
    return word

def last_word(sentence):
    last = len(sentence) - 1
    revers = ""

    while sentence[last] != " ":
        revers += sentence[last]
        last -= 1
    return revers[::-1]

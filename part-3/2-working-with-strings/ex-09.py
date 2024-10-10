# A framed word

word = input("Word: ")
with_word = int(30 - len(word))
odd_length = int(with_word / 2) - 1
even_length = int(with_word / 2)

print("*" * 30)
if len(word) % 2 == 0:
      print("*" + odd_length * " " + word + odd_length * " " + "*")
else:
      print("*" + even_length * " " + word + odd_length * " " + "*")
      print("*" * 30)

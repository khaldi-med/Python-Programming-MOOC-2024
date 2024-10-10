# Second and second to last characters

user_input = input("Please type in a string: ")

after_last = user_input[len(user_input) - 2]
second_char = user_input[1]

if second_char == after_last:
    print(f"The second and the second to last characters are {second_char}")
else:
    print("The second and the second to last characters are different")

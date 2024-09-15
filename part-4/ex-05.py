# A shape


def line(num, str):
    if str == "":
        print("*" * num)
    else:
        print(str[0] * num)


def shape(num1, str1, num2, str2):
    i = 1
    while i <= num1:
        line(i, str1)
        i += 1
    i = 0
    while i < num2:
        line(num1, str2)
        i += 1

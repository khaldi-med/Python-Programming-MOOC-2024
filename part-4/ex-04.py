# A square of hashes


def line(num, str):
    if str == "":
        print("*" * num)
    else:
        print(str[0] * num)


def square_of_hashes(size):
    # You should call function line here with proper parameters
    i = 0
    while i < size:
        line(size, "#")
        i += 1

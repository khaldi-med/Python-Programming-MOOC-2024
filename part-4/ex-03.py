# A box of hashes


def line(num, str):
    if str == "":
        print("*" * num)
    else:
        print(str[0] * num)


def box_of_hashes(height):
    # You should call function line here with proper parameters*
    while height > 0:
        line(10, "#")
        height -= 1

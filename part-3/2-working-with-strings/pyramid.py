# number of layers in the pyramid
n = 10
row = "*"

while n > 0:
    print(" " * n + row)
    row += "**"
    n -= 1

# Multiplication

while True:
    number = int(input("Please type in a number: "))
    if number > 0:
        break

leftNum = 1
while leftNum <= number:
    rightNum = 1
    while rightNum <= number:
        product = leftNum * rightNum
        print(f"{leftNum} x {rightNum} = {product}")
        rightNum += 1
    leftNum += 1


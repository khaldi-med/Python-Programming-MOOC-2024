# A rectangle of hashes

width = int(input("Width: "))
height = int(input("Height: "))

index = 1

while index <= height:
    print(width * "#")
    index += 1

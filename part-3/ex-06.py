# The sum of consecutive numbers, version 1


limit = int(input("Limit: "))
number = 1
sum_num = 0

while number <= limit:
    if sum_num < limit:
        sum_num += number
        number += 1
        print(sum_num)

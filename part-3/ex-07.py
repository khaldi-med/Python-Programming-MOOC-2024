# The sum of consecutive numbers, version 2

limit = int(input("Limit: "))
number = 1
sum_num = 1
result = f"The consecutive sum: {number}"

while sum_num < limit:
    number += 1
    result = f"{result} + {number}"
    sum_num += number

print(f"{result} = {sum_num}")

# Write your solution here
typed_num = 0
sum_num = 0
mean_num = 0
negative_num = 0
positive_num = 0
while True:
    num = int(input("Number: "))

        if num == 0:
            print(f"Numbers typed in: {typed_num}")
            print(f"The sum of the numbers is: {sum_num}")
            print(f"The mean of the numbers is: {mean_num}")
            print(f"Positive numbers: {positive_num}")
            print(f"Negative numbers: {negative_num}")
            break
        if num < 0:
            negative_num += 1
            if num > 0:
                positive_num += 1
                typed_num += 1
                sum_num += num
                mean_num = sum_num / typed_num




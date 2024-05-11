# The next leap year

year = int(input("Please type in a year: "))

while True:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                nextYear += 1
                newLeap = year + 1
                if nextYear == 2:
                    print("The next leap year after {year} is {newLeap}")
                    break
	else:
	    year += 1
    else:
	year += 1
    
                
              








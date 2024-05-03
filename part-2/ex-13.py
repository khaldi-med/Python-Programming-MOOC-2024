# Alphabetically in the middle

let1 = str(input("Enter a letter 1: "))
let2 = str(input("Enter a letter 2: "))
let3 = str(input("Enter a letter 3: "))

if let1 > let2 and let1 > let3:
  if let2 > let3:
    print(f"The letter in the middle is {let2}")
  else:
    print(f"The letter in the middle is {let3}")
elif let2 > let1 and let2 > let3:
  if let1 > let3:
    print(f"The letter in the middle is {let1}")
  else:
    print(f"The letter in the middle is {let3}")
elif let3 > let1 and let3 > let2:
  if let1 > let2:
    print(f"The letter in the middle is {let1}")
  else:
    print(f"The letter in the middle is {let2}")


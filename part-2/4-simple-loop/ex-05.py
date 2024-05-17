# PIN and number of attempts

pinNum = 4321
triedNum = 0

while True:
    pin = int(input("PIN: "))
    triedNum += 1

    if pin != pinNum:
        print("Wrong")
    elif pin == pinNum:
        if triedNum == 1:
          print("Correct! It only took you one single attempt!")
          break
        else:
          print(f"Correct! It took you {triedNum} attempts")
          break


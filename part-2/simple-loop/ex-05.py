# PIN and number of attempts

while True:
pin = input("PIN: ")
pinNum = 4321
triedNum = 0

if pin != pinNum:
    triedNum +=1
    if pin == pinNum:
        if triedNum == 1:
            print("Correct! It only took you one single attempt!")
            break
        else:
            print(f"Correct! It took you {triedNum} attempts")
            break


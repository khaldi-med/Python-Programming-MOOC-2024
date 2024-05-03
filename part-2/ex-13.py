# Alphabetically in the middle

gift = int(input("Value of gift: "))
taxAmount = 0;

if 5000 <= gift < 25000:
    taxAmount = (100 + (gift - 5000) * 0.08)
    print(f"Amount of tax: {taxAmount} euros")

elif 25000 <= gift < 55000:
    taxAmount = (1700 + (gift - 25000) * 0.10)
    print(f"Amount of tax: {taxAmount} euros")

elif 55000 <= gift < 200000:
    taxAmount = (4700 + (gift - 55000) * 0.12)
    print(f"Amount of tax: {taxAmount} euros")
    
elif 200000 <= gift < 1000000:
    taxAmount = (22100 + (gift - 200000) * 0.15)
    print(f"Amount of tax: {taxAmount} euros")

elif gift >= 1000000:
    taxAmount = (142100 + (gift - 1000000) * 0.17)
    print(f"Amount of tax: {taxAmount} euros")

else:
    print("No tax!")

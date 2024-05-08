# Repeat password

passWord = input("Password: ")
while True:
    checkPass = input("Repeat password: ")
    if checkPass != passWord:
        print("They do not match!")
    else:
        print("User account created!")
        break



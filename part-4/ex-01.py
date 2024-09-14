# Hello Visual Studio Code

while True:
    user_iput = input("Editor: ")

    match user_iput.lower():
        case "emacs" | "atom" | "vim":
            print("not good")
        case "word" | "notepad":
            print("awful")
        case "visual studio code":
            print("an excellent choice!")
            break

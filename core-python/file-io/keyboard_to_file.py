def KeyboardToFileCopy():
    file = open("../files/keyboard.txt", "w")
    text = input('Enter your message = ')

    while (text != "quit"):
        file.write(text)
        file.write(" ")
        text = input('')
    file.close()


KeyboardToFileCopy()

def writeFile():
    file = open("../files/hii.txt", "w")
    file.write("Hi\n")
    file.write("This is Python file")
    file.close()


writeFile()

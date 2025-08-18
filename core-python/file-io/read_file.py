def readFile():
    file = open("../files/hello.txt", "r")
    text = file.read()  # Read all data
    print(text)
    file.close()  # Close a file


readFile()

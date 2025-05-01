def fileInfo():
    fo = open("../files/hello.txt", "r")
    print("File Name: ", fo.name)
    print("Mode of Opening: ", fo.mode)
    print("Is Closed: ", fo.closed)
    fo.close()
    print("Is Closed After Closing: ", fo.closed)

fileInfo()
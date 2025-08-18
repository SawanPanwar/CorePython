file = open("../files/hello.txt", "r")
print(file.tell())  # Print current file pointer position
file.seek(5)  # Move to position 5
str_data = file.read(3)  # Read 3 characters
print(str_data)  # Print the read string
print(file.tell())  # Print current file pointer position
file.close()

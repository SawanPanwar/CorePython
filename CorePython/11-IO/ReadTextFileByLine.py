import re
#Read a file line by line
def readLine():
    # Iterate over the lines of the File
    file = open("C:\\Users\\Sawan\\Desktop\\Add.py", "r") #Open a file
    file1 = open("C:\\Users\\Sawan\\Desktop\\Ad.txt", "w")
    for line in file :
        if (re.search("@gmail.com", line)):
           file1.write(line)
    file.close() # Close a file
    file1.close()
  
readLine()

import os
s = open("C:\\Users\\Sawan\\Desktop\\Ad1.txt")
position = s.seek(5)
str = s.read(3)
print(str)
print(s.tell())
#position = s.seek(5)



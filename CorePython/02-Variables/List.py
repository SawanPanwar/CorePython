# Example of  List
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

#List Example
a = [5,10,15,20,25,30,35,40]
#print("a[2] = ", a[2])
#a[1] = 20
a1 = (5,10,15,20,25,30,35,40)
print(a.__sizeof__())
print(a1.__sizeof__())
a.append(11)
print(a)
print("length = ",len(a))
del a[1]
print(a)





b = ['ram', 'shyam', 1, 2 , 'a']
print(a[-1])
#print(b[0])
# Example of Creating Tuple
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

#creating tuple 
my_tuple = ()
print(my_tuple)

#tuple of int, float, string
tuple_list1 = (1, 2.8, "Hello Ram")
#print(tuple_list1)
#print(len(tuple_list1))

# tuple of string and list
tuple_list2 = ("Book", [1, 2, 3])
#print(tuple_list2)

print(tuple_list2[0:1])

t = tuple_list1 + tuple_list2
t1 = tuple_list1 * 2

print(t1)

#Accessing elements from nested tuples
tuple_list4 = (1, "Balram", (11, 22, 33))  #1 represented the second element of that tuple.

#print(tuple_list4[1][2])
#print(tuple_list4[2][1])
list = ['a', 100, "abc", 100.10, True]

print(list)

print(list[1])

list[1] = 200

print(list)

print(list[1:4])

print(list[1:])

print(list[:4])

print(list[:])

new_list = list * 2

print(new_list)

del (new_list[1])

print(new_list)

print(len(new_list))

new_list.append("xyz")

print(new_list)
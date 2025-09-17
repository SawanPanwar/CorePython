list_of_list = [[1, 'abc', 1000], [2, 'xyz', 1100], [1, 'pqr', 500], [1, 'klm', 700]]

for i in range(0, len(list_of_list)):
    for j in range(i + 1, len(list_of_list)):
        if list_of_list[i][2] > list_of_list[j][2]:
            temp = list_of_list[i][2]
            list_of_list[i][2] = list_of_list[j][2]
            list_of_list[j][2] = temp
    print(list_of_list[i], end=" ")

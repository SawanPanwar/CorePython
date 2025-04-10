arr = [100, 10, 11, 5, 13, 17, 88]

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    print(arr[i], end=" ")

numbers = [100, 10, 11, 5, 13, 17, 88]

highest = 0
second_highest = 0

for n in numbers:
    if n > highest:
        second_highest = highest
        highest = n
    elif n > second_highest and n != highest:
        second_highest = n

print("Highest number is:", highest)
print("Second highest number is:", second_highest)

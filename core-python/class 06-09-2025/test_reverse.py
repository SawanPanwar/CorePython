number = 153  # 1 + 125 + 27 = 153
sum = 0
rem = 0
n = number  # n = 153

while n > 0:
    rem = n % 10  # rem = 153 % 10 = 3
    sum = (sum * 10) + rem  # sum = (0 * 10) + 3 = 3
    n = n // 10  # n = 153 // 10 = 15

print('reverse number of', number, 'is', sum)

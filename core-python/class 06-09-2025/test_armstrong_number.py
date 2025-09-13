number = 153  # 1 + 125 + 27 = 153
sum = 0
rem = 0
n = number  # n = 153

while n > 0:
    rem = n % 10  # rem = 153 % 10 = 3
    sum = sum + (rem * rem * rem)  # sum = 0 + (3 * 3 * 3) = 27
    n = n // 10  # n = 153 // 10 = 15

if sum == number:
    print(number, 'is a armstrong number')
else:
    print('not armstrong number')

number = 11
count = 0

for i in range(2, number):
    if number % i == 0:
        count += 1

if count == 0:
    print("Prime Number:", number)
else:
    print("Not Prime Number:", number)
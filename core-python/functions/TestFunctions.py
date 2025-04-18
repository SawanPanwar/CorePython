def test_function():
    print('my first function')


def sum(a=0, b=10):
    c = a + b
    print('sum:', c)
    return c


def armstrong_number(number):
    n = number
    sum = 0
    rem = 0

    while n > 0:
        rem = n % 10
        sum = sum + (rem * rem * rem)
        n = n // 10

    if sum == number:
        print("Armstrong Number:", number)
    else:
        print("Not Armstrong Number:", number)


def changeList(list):
    list.append(6)


def sumnum(a, *varg):
    t = a
    for n in varg:
        t += n
    return t;


# test_function()

# s = sum(40, 50)

# armstrong_number(11)

# list = [1, 2, 3, 4, 5]
# print(list)
# changeList(list)
# print(list)

total = sumnum(2, 2, 3, 4, 5)
print('Total:', total)
def sum1():
    'it is a sum function'
    print('sum function')


def sum2(a, b):
    c = a + b
    print('sum:', c)


def sum3(a=0, b=0):
    c = a + b
    print('sum:', c)


def sum4(a=0, b=0):
    c = a + b
    print('sum:', c)
    return c


# sum1()
# print(sum1.__doc__)

# sum2(10, 20)

# sum3(10, 20)

# s = sum4(20, 20)


def changeList(list):
    list.append(6)


# list = [1, 2, 3, 4, 5]
# print('before changeList:', list)
# changeList(list)
# print('after changeList:', list)

def sum_all_01(a, *varg):
    sum = a
    for n in varg:
        sum += n
    return sum

# sum1 = sum_all_01(2, 2, 3, 4, 5)
# print('sum1:', sum1)


def sum_all_02(a, **varg):
    sum = a
    for value in varg.values():
        sum += value
    return sum

sum2 = sum_all_02(2, b=1, c=2, d=3)
# print('sum2:', sum2)
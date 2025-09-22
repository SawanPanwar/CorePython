def sum1():
    'it is a sum function'
    print('sum function')


# sum1()
# print(sum1.__doc__)


def sum2(a, b):
    c = a + b
    print('sum:', c)


# sum2(20, 30)


def sum3(a=0, b=0):
    c = a + b
    print('sum:', c)


# sum3(10, 20)


def sum4(a=0, b=0):
    c = a + b
    return c


# s = sum4(20, 20)
# print('s:', s)


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


sum1 = sum_all_01(2, 5, 6, 7, 8)
# print('sum1:', sum1)


def sum_all_02(a, **varg):
    sum = a
    for value in varg.values():
        sum += value
    return sum


sum2 = sum_all_02(2, b=1, c=2, d=3)
# print('sum2:', sum2)

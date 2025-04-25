def sum1():
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
    total = a
    for n in varg:
        total += n
    return total


def sum_all_02(a, **varg):
    total = a
    for value in varg.values():
        total += value
    return total


total1 = sum_all_01(2, 2, 3, 4, 5)
total2 = sum_all_02(2, b=1, c=2, d=3)

print('Total1:', total1)
print('Total2:', total2)

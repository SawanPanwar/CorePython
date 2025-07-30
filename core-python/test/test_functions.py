# function # method

var = 100

def test():
    print('test function 1')
    print('test function 2')
    print('test function 3')


def sum1():
    a = 10
    b = 20
    c = a + b
    print('sum:', c)


def sum2(a, b):
    c = a + b
    print('sum:', c)


def sum3(a, b):
    c = a + b
    print('sum:', c)
    return c


def sum4(a=0, b=0):
    c = a + b
    print('sum:', c)
    return c


# test()

# sum1()

# sum2(10, 20)

# d = sum3(10, 20)
# print('d:', d)

sum4(10, 30)

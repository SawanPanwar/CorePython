a = 10
b = 2

try:
    c = a / b
    print('division:', c)
except ZeroDivisionError as e:
    print('exception:', e)
else:
    print('in else block')
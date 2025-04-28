a = 10
b = 0

try:
    c = a / b
except ZeroDivisionError as e:
    print('exception:', e)
else:
    print('division:', c)
finally:
    print('finally block executed')
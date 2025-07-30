print('before')

a = 10

b = 0

try:
    c = a / b
    print('division:', c)
except Exception as e:
    print('exception:', e)

print('after')

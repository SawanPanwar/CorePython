try:
    number = int(input("Enter your Number:"))

    if number >= 10:
        raise Exception('invalid number')
except Exception as e:
    print('exception:', e)

print('after')
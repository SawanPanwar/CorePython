class LoginException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


login_id = input('enter login_id: ')
password = input('enter password: ')

try:
    if login_id == 'admin' and password == 'admin':
        print('Valid user')
    else:
        raise LoginException('Invalid user')
except LoginException as e:
    print('exception:', e)

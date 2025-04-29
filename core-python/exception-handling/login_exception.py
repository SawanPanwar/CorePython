class LoginException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


login_id = 'admin'
password = 'admin'

try:
    if login_id == 'admin' and password == 'admin':
        print('Valid user')
    else:
        raise LoginException('Invalid user')
except LoginException as e:
    print('LoginException:', e)

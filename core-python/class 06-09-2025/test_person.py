class Person:

    def __init__(self):
        print('person constructor')

    def change_address(self, address):
        print('your new address is', address)

    def change_name(self, name):
        print('your updated name is', name)


p = Person()
p.change_address('indore')
p.change_name('raghav')

p1 = Person()
p1.change_address('82, jaora compound, indore')
p1.change_name('vivek')

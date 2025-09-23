class Person:

    def __init__(self):
        self.first_name = 'abc'
        self.last_name = 'xyz'


p = Person()
p.first_name = 'vishal'
p.last_name = 'jain'

print(p.first_name, p.last_name)

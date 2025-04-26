class Person:
    count = 0  # Class variable shared among all instances

    def __init__(self):
        self.name = ''
        self.address = ''
        Person.count += 1  # Increment count every time a new Person is created

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address


# Create first Person object
p = Person()
p.set_name('abc')
print('Name:', p.get_name())
print('Count:', Person.count)
print('Memory address of p:', id(p))

# Create second Person object
p1 = Person()
p1.set_name('xyz')
print('Name:', p1.get_name())
print('Count:', Person.count)
print('Memory address of p1:', id(p1))

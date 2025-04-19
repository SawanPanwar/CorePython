class Person:
    count = 0  # class variable

    def __init__(self):  # constructor
        self.name = ''  # instance variable
        Person.count += 1

    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name


p = Person()
p.setName('abc')
print('name:', p.getName())
print('count:', Person.count)
print('p memory address:', id(p))

p1 = Person()
p1.setName('xyz')
print('name:', p1.getName())
print('count:', Person.count)
print('p1 memory address:', id(p1))

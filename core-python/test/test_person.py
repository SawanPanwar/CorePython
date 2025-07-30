class Person:
    count = 0

    def __init__(self):
        self.__name = ''
        self.__address = ''
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def change_count(self):
        Person.count += 50
        print(Person.count)


p = Person()
p.set_name('abc')
p.set_address('indore')
p.set_age(18)
Person.count = 100
print(Person.count)

# print(p.get_name())
# print(p.get_address())
# print(p.get_age())

p1 = Person()
p1.change_count()


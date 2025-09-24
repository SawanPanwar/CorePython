class Person:

    def __init__(self, fname, lname):
        self.__first_name = fname
        self.__last_name = lname

    def set_first_name(self, fname):
        self.__first_name = fname

    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, lname):
        self.__last_name = lname

    def get_last_name(self):
        return self.__last_name


p = Person('abc', 'xyz')
p.set_first_name('vishal')
# p.set_last_name('gupta')

print(p.get_first_name())
print(p.get_last_name())

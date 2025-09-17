class Person:
    count = 100

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

    @staticmethod
    def address():
        print("Person Address Method")

    def __str__(self):
        return "Person: first_name = %s, last_name = %s" % (self.__first_name, self.__last_name)

    def __del__(self):
        className = self.__class__.__name__
        print("Destroying...", className)


p = Person('vivek', 'gupta')
# p.set_first_name('vivek')
# p.set_last_name('gupta')
print(p.get_first_name(), p.get_last_name())
print('memory address p:', id(p))

print(p)

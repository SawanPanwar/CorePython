class Person:
    'i am person class'

    def __init__(self):
        self.__id = 0
        self.name = ''
        self.salary = 0.0

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.name = name

    def set_salary(self, salary):
        self.salary = salary

    # Getter methods
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary


print(Person.__doc__)
print(Person.__name__)
print(Person.__module__)
print(Person.__dict__)

class Employee:
    'I am Employee'

    def __init__(self, salary):
        self.salary = salary

    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary


emp = Employee(2000)

print(emp)

print(id(emp))

print(emp.__doc__)


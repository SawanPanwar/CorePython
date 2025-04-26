class Employee:

    def __init__(self):
        print('Employee Deafult Constructor')

    def get_salary(self, salary):
        print('Employee salary:', salary)

    def get_address(address=''):
        print('Employee Address:', address)


emp = Employee()

print(emp)

print(id(emp))

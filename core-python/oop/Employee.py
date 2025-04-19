class Employee:

    def __init__(self):
        self.name = 'samay'
        self.address = 'indore'

    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def setAddress(self, a):
        self.address = a

    def getAddress(self):
        return self.address

e = Employee()

print(e.getName())
print(e.getAddress())

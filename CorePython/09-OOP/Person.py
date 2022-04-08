class Person:

    count = 0

    def __del__(self):
        print("I am destructor")

    def __init__(self, name, address):
        self.name = name
        self.address= address
        Person.count += 1

    def __init__(self, name, address, g):
        self.name = name
        self.address = address
        self.g = g
        Person.count += 1

    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def setAddress(self, a):
        self.address = a

    def getAddress(self):
        return self.address

    def __str__(self):
        return "Name = %s \n Address = %s" % (self.name, self.address)



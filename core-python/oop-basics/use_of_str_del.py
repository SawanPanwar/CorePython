class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        className = self.__class__.__name__
        print("Destroying ", className)

    def __str__(self):
        return "Person: name = %s, age = %s" % (self.name, self.age)


# Create an instance of Person
person1 = Person("abc", 30)

# Print the string representation of the object
print(person1)

# Delete the object explicitly (triggers the __del__ method)
del person1

# The destructor message will be printed when the object is destroyed

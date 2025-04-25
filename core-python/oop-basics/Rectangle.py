class Rectangle:

    def __init__(self):
        self.length = 0
        self.width = 0

    def set_length(self, l):
        self.length = l

    def get_length(self):
        return self.length

    def set_width(self, w):
        self.width = w

    def get_width(self):
        return self.width

    def area(self):
        return self.length * self.width


# Example usage
r = Rectangle()
r.set_length(10)
r.set_width(5)

print("Length:", r.get_length())
print("Width:", r.get_width())
print("Area:", r.area())

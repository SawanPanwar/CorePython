class Shape:
    def __init__(self):
        self.color = ''
        self.border_width = 0

    def set_color(self, c):
        self.color = c

    def get_color(self):
        return self.color

    def set_border_width(self, bw):
        self.border_width = bw

    def get_border_width(self):
        return self.border_width


class Rectangle(Shape):

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


class Circle(Shape):

    def __init__(self):
        self.radius = 0

    def set_radius(self, r):
        self.radius = r

    def get_radius(self):
        return self.radius


# Test Rectangle and Circle

# Creating a Rectangle object
r = Rectangle()
print("Rectangle:")
print("Length:", r.get_length())
print("Width:", r.get_width())
print("Color:", r.get_color())
print("Border Width:", r.get_border_width())

# Creating a Circle object
c = Circle()
print("\nCircle:")
print("Radius:", c.get_radius())
print("Color:", c.get_color())
print("Border Width:", c.get_border_width())

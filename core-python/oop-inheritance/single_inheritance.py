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


# Test
r = Rectangle()
r.set_length(10)
r.set_width(20)
r.set_color("red")
r.set_border_width(100)

print("Length:", r.get_length())
print("Width:", r.get_width())
print("Color:", r.get_color())
print("Border Width:", r.get_border_width())

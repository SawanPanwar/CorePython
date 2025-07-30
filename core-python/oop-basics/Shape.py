class Shape:

    def __init__(self):
        self.color = ''
        self.borderWidth = 0

    def set_color(self, c):
        self.color = c

    def get_color(self):
        return self.color

    def set_borderwidth(self, bw):
        self.borderWidth = bw

    def get_borderwidth(self):
        return self.borderWidth


s = Shape()
s.set_color("Red")
s.set_borderwidth(5)

print("Color:", s.get_color())
print("Border Width:", s.get_borderwidth())

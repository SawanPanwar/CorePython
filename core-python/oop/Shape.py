class Shape:

    def __init__(self):
        print("Shape Class Constructor")

    def area(self):
        print("area method")

    def sum(self, a, b):
        c = a + b
        print('sum:', c)


s1 = Shape()  # object
s1.area()
s1.sum(10, 20)

Shape.sum(10, 20)

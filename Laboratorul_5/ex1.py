
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self,side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

circle = Circle(radius=2)
print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")

rectangle = Rectangle(length=4, width=8)
print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")

triangle = Triangle(5, 4, 3)
print(f"Triangle area: {triangle.area()}")
print(f"Triangle perimeter: {triangle.perimeter()}")

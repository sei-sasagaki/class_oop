import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        pass

    def area(self):
        self.area = round(self.radius * self.radius * math.pi, 2)
        return self.area

    def perimeter(self):
        self.perimeter = round(2 * self.radius * math.pi, 2)
        return self.perimeter


# 半径1の円
circle1 = Circle(radius=1)
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 18.85

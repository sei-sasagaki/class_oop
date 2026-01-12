import math


class Rectangle():
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width
        pass

    def area(self):
        self.area = format(self.height * self.width, '.2f')
        return self.area

    def diagonal(self):
        self.diagonal = format(math.hypot(self.height, self.width), ".2f")
        return self.diagonal


rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24

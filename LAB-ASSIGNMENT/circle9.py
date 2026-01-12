import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = center    
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius
    
center_point = Point(5, 7)
circle_obj = Circle(center_point, 10)

print("Circle center:", circle_obj.center.x, circle_obj.center.y)
print("Area:", circle_obj.area())
print("Circumference:", circle_obj.circumference())


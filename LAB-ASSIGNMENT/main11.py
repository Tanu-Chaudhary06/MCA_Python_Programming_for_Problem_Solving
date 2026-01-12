from Shapes_.Circle import Circle
from Shapes_.Rectangle import Rectangle
from Shapes_.helper import calculate

print("=== Absolute Import ===")
c1 = Circle(5)
r1 = Rectangle(4, 6)
print("Circle Area:", c1.area())
print("Rectangle Area:", r1.area())

print("\n=== Using Relative Import inside Package ===")
calculate()



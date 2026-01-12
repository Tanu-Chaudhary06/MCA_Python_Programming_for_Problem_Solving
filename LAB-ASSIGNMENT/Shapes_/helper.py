#Realtive import 
from .Circle import Circle
from .Rectangle import Rectangle

def calculate():
    c = Circle(3)
    r = Rectangle(2, 5)

    print("Circle Area:", c.area())
    print("Rectangle Area:", r.area())

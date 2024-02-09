#Define a class named Rectangle which inherits from Shape class from task 2.
#Class instance can be constructed by a length and width. 
#The Rectangle class has a method which can compute the area.
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self):
        self.length = float(input())
        self.width = float(input())
    def area(self):
        return self.length * self.width

y = Rectangle()
print("Area of Rectangle:", y.area())

x = Shape()
print("Area of Shape:", x.area())
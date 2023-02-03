class Shape:
    def __init__(self,a,b,c):
        self.color=a
        self.l=b
        self.b=c
    def area(self):
        return self.l*self.b
    def colour(self):
        return self.color

class Square(Shape):
    def __init__(self,a,b):
        super().__init__(a,b,b)

class Rectangle(Shape):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)

x=Square("Red",5)
y=Rectangle("Green",5,10)
print(x.area())
print(x.colour())
print(y.area())
print(y.colour())
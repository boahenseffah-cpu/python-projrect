class Circle():
    def __init__(self,radius):
        self.radius=radius

    def display(self):
        print(self.radius)

    def area(self):
        print(3.14*self.radius*self.radius)
    
    def perimeter(self):
        print(2*3.14*self.radius)
    def totalcost(self,price):
        a=3.14*self.radius*self.radius
        print(a*price)

circle1=Circle(5)
circle1.display()
circle1.area()
circle1.perimeter()

circle2=Circle(4)   
circle2.display()
circle2.perimeter()
circle2.area()
circle2.totalcost(5)
        
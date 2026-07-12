class Rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print(self.length*self.width)
        
    
rectangle1=Rectangle(8,16)
rectangle1.area()

class square():
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def perimeter(self):
        print((self.length+self.width)*2)
        
    
square1=square(8,16)
square1.perimeter()






class computer():
    def __init__(self,mark,resolution,hz):
        self.mark=mark
        self.resolution=resolution
        self.hz=hz

    def display(self):
        print(self.mark,self.resolution,self.hz)

    
    
computer1=computer("samsung",1800,140)
computer1.display()

computer2=computer("apple",720,60)
computer2.display()

computer3=computer("asus","4K",240)
computer3.display()


        
    
    

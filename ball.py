import pygame
pygame.init()
screen=pygame.display.set_mode((400,522))
class Ball():
    def __init__(self,color,xposition,yposition,radius,width):
        self.color=color
        self.xposition=xposition
        self.yposition=yposition
        self.radius=radius
        self.width=width

    def display(self):
        print(self.color,self.xposition,self.yposition,self.radius,self.width)
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.xposition,self.yposition),self.radius,self.width)


ball1=Ball("blue",110,20,12,0)
ball1.display()
ball2=Ball("black",100,60,12,0)
ball2.display()
ball3=Ball("pink",30,10,12,0)
ball3.display()
ball4=Ball("green",60,80,12,0)
ball4.display()
ball5=Ball("red",45,100,12,0)
ball5.display()
while True:
    screen.fill("yellow")
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    ball1.draw()
    ball2.draw()
    ball3.draw()
    ball4.draw()
    ball5.draw()
    pygame.display.update()





        
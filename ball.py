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


ball1=Ball("blue",45,20,12,0)
ball1.display()
while True:
    screen.fill("yellow")
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    ball1.draw()
    pygame.display.update()





        
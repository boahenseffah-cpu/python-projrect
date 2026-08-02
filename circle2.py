import pygame
pygame.init()
screen=pygame.display.set_mode((400,522))
clock=pygame.time.Clock()
class Circle():
    def __init__(self,color,xposition,yposition,radius):
        self.color=color
        self.xposition=xposition
        self.yposition=yposition
        self.radius=radius

    def draw(self):
        pygame.draw.circle(screen,self.color,(self.xposition,self.yposition),self.radius,0)
    
    def move(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.yposition-=2
        elif key[pygame.K_DOWN]:
            self.yposition+=2
        elif key[pygame.K_LEFT]:
            self.xposition-=2
        elif key[pygame.K_RIGHT]:
            self.xposition+=2


circle1=Circle("blue",100,40,20)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    screen.fill("black")
    circle1.draw()
    circle1.move()
    pygame.display.update()




        

        

import pgzrun
import random
WIDTH=852
HEIGHT=533
spaceship1=Actor("spaceship1")
spaceship1.pos=(400,470)
alienlist=[]
def alien():
    for i in range(5):
        ship=Actor("ship")
        ship.pos=(100+i *155,50)
        alienlist.append(ship)

def goto():
    x=random.randint(0,800)
    y=random.randint(0,300)
    

def draw():
    screen.blit("backgroundspace",(0,0))
    spaceship1.draw()
    for alien in alienlist:
        alien.draw()

def update():
    if keyboard.left:
        spaceship1.x-=5
    elif keyboard.right:
        spaceship1.x+=5
    for alien in alienlist:
        alien.y+=1

        

goto()              
alien()
pgzrun.go()

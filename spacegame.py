import pgzrun
import random
WIDTH=852
HEIGHT=533
spaceship1=Actor("spaceship1")
spaceship1.pos=(400,470)
alienlist=[]
bulletlist=[]
def alien():
    for i in range(5):
        ship=Actor("ship")
        ship.pos=(100+i *155,50)
        alienlist.append(ship)
        
def goto():
    x=random.randint(0,800)
    y=random.randint(0,300)
    alien.pos=(x,y)

def draw():
    screen.blit("backgroundspace",(0,0))
    spaceship1.draw()
    for alien in alienlist:
        alien.draw()
    for bullet1 in bulletlist:
        bullet1.draw()

def on_key_down(key):
    if key==keys.SPACE:
        bullet1=Actor("bullet")
        bullet1.pos=(spaceship1.pos)
        bulletlist.append(bullet1)
def update():
    if keyboard.left:
        spaceship1.x-=5
    elif keyboard.right:
        spaceship1.x+=5
    for alien in alienlist:
        alien.y+=1


        if spaceship1.colliderect(alien):
            x=random.randint(0,800)
            y=0

            alien.pos=(x,y)
        if alien.y>522:
            x=random.randint(0,800)
            y=0
            alien.pos=(x,y)
    for bullet1 in bulletlist:
        bullet1.y-=3
        

goto()              
alien()
pgzrun.go()

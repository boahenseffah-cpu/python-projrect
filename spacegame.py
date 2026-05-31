import pgzrun
import random
gameover=False
WIDTH=852
HEIGHT=533
spaceship1=Actor("spaceship1")
spaceship1.pos=(400,470)
alienlist=[]
bulletlist=[]
life=3
score=0
def alien():
    for i in range(5):
        ship=Actor("ship")
        ship.pos=(100+i *155,50)
        alienlist.append(ship)
    clock.schedule(alien,5)    
def goto():
    x=random.randint(0,800)
    y=random.randint(0,300)
    alien.pos=(x,y)

def draw():
    if gameover==True:
        screen.blit("gameover",(100,0))
        return
    screen.blit("backgroundspace",(0,0))
    spaceship1.draw()
    for alien in alienlist:
        alien.draw()
    for bullet1 in bulletlist:
        bullet1.draw()
    screen.draw.text("life="+str(life),(25,25))
    screen.draw.text("score="+str(score),(10,10))
def on_key_down(key):
    if key==keys.SPACE:
        bullet1=Actor("bullet")
        bullet1.pos=(spaceship1.pos)
        bulletlist.append(bullet1)
def update():
    global life
    global score
    global gameover
    if keyboard.left:
        spaceship1.x-=5
    elif keyboard.right:
        spaceship1.x+=5
    if life<=0:
            gameover=True  
    for alien in alienlist:
        alien.y+=1



        if spaceship1.colliderect(alien):
           alienlist.remove(alien)
          
        if alien.y>522:
           alienlist.remove(alien)
           life-=1
    for bullet1 in bulletlist:
        bullet1.y-=3
        if bullet1.y<0:
            bulletlist.remove(bullet1)

        for alien in alienlist:
            if alien.colliderect(bullet1):
                alienlist.remove(alien)
                bulletlist.remove(bullet1)
                score+=1
        
    
        


goto()              
alien()
pgzrun.go()

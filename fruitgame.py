import pgzrun
import random
gameover=False
HEIGHT=522
WIDTH=800
basket=Actor("basket")
apple=Actor("apple")
orange=Actor("orange")
mango=Actor("mango")
basket.pos=(400,470)
score=0
life=3
def draw():
    if gameover==True:
        screen.blit("gameover",(100,0))
        return
    screen.blit("backgroundfruit",(0,0))
    basket.draw()
    apple.draw()
    mango.draw()
    orange.draw() 
    screen.draw.text("score="+str(score),(10,10))
    screen.draw.text("life="+str(life),(25,25))
def update():
    global score
    global gameover
    global life
    if keyboard.left:
        basket.x-=5
    elif keyboard.right:
        basket.x+=5
    apple.y+=3
    orange.y+=3
    mango.y+=3
    if basket.colliderect(apple):
         x=random.randint(0,800)
         y=0
         apple.pos=(x,y)
         score+=1
         
         
    if apple.y>522:
        x=random.randint(0,800)
        y=0
        apple.pos=(x,y)
        life-=1
        
    if basket.colliderect(orange):
        x=random.randint(0,800)
        y=0
        orange.pos=(x,y)
        score+=1

    if orange.y>522:
        x=random.randint(0,800)
        y=0
        orange.pos=(x,y)
        life-=1

    if basket.colliderect(mango):
        x=random.randint(0,800)
        y=0
        mango.pos=(x,y)
        score+=1

    if mango.y>522:
        x=random.randint(0,800)
        y=0
        mango.pos=(x,y)
        life-=1

    if life==0:
        gameover=True




    
def goto():
    x=random.randint(0,800)
    y=0
    apple.pos=(x,y)
    orange.pos=(x,y)
    mango.pos=(x,y)
goto()
pgzrun.go()
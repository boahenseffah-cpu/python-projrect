import pgzrun
import random
HEIGHT=522
WIDTH=800
basket=Actor("basket")
apple=Actor("apple")
basket.pos=(400,470)
score=0
def draw():
    screen.blit("backgroundfruit",(0,0))
    basket.draw()
    apple.draw() 
    screen.draw.text("score="+str(score),(10,10))
def update():
    global score
    if keyboard.left:
        basket.x-=5
    elif keyboard.right:
        basket.x+=5
    apple.y+=5
    if basket.colliderect(apple):
         x=random.randint(0,800)
         y=0
         apple.pos=(x,y)
         score+=1
    if apple.y>522:
        x=random.randint(0,800)
        y=0
        apple.pos=(x,y)
        
    
def goto():
    x=random.randint(0,800)
    y=0
    apple.pos=(x,y)
goto()
pgzrun.go()
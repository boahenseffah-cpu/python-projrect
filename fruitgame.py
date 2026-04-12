import pgzrun
import random
HEIGHT=522
WIDTH=800
basket=Actor("basket")
apple=Actor("apple")
basket.pos=(400,470)

def draw():
    screen.blit("backgroundfruit",(0,0))
    basket.draw()
    apple.draw()
def update():
    if keyboard.left:
        basket.x-=5
    elif keyboard.right:
        basket.x+=5
    apple.y+=5
def goto():
    x=random.randint(0,800)
    y=0
    apple.pos=(x,y)
goto()




    
        

pgzrun.go()
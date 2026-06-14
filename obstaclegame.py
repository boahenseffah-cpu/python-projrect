import pgzrun
import random
gameover=False
life=3
HEIGHT=522
WIDTH=696
mario=Actor("mario")
mario.pos=(50,400)
obstacleimages=["bombe","cactus","rock","spike"]
obstaclelist=[]
def newobstacle():
    obstacle=Actor(random.choice(obstacleimages))
    obstacle.pos=(670,400)
    obstaclelist.append(obstacle)
    clock.schedule(newobstacle,2)
def draw():
    if gameover==True:
        screen.blit("gameover",(50,-20))
        return
    screen.blit("mariobackground",(0,0))
    screen.draw.text("life="+str(life),(10,10))
    mario.draw()
    for obstacle in obstaclelist:
        obstacle.draw()
def on_key_down(key):
    if key==keys.SPACE and mario.y>350:
        mario.y-=180

def update():
    global life
    global gameover
    if mario.y<400:
        mario.y+=2   
    for obstacle in obstaclelist: 
        obstacle.x-=2
        if mario.colliderect(obstacle):
            life-=1

            obstaclelist.remove(obstacle)

        if life==0:
            gameover=True



    

   

    




























newobstacle()
pgzrun.go()
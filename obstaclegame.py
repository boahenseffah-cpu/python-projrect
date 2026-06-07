import pgzrun
import random
HEIGHT=522
WIDTH=696
mario=Actor("mario")
mario.pos=(50,400)
obstacleimages=["bombe","cactus","rock","spike"]
obstaclelist=[]
def newobstacle():
    obstacle=Actor(random.choice(obstacleimages))
    obstacle.pos=(670,470)
    obstaclelist.append(obstacle)
    clock.schedule(newobstacle,2)
def draw():
    screen.blit("mariobackground",(0,0))
    mario.draw()
    for obstacle in obstaclelist:
        obstacle.draw()

def update():
    for obstacle in obstaclelist:
        obstacle.x-=2


    

   

    




























newobstacle()
pgzrun.go()
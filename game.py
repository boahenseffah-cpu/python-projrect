import pgzrun
WIDTH=811
HEIGHT=450
boy=Actor("child")
boy.pos=(700,350)
mom=Actor("mom")
mom.pos=(620,350)
def draw():
    screen.blit("background",(0,0))
    boy.draw()
    mom.draw()
def update():
    if keyboard.up:
        mom.y-=5
    elif keyboard.down:
        mom.y+=5
    elif keyboard.left:
        mom.x-=5
    elif keyboard.right:
        mom.x+=5
pgzrun.go()



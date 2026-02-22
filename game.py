import pgzrun
WIDTH=811
HEIGHT=450
boy=Actor("child")
boy.pos=(700,350)
def draw():
    screen.blit("background",(0,0))
    boy.draw()




pgzrun.go()


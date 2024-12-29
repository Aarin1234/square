import pgzrun
HEIGHT=500
WIDTH=500
TITLE="A SAMPLE"
RED=(200,0,0)
GREEN=(0,200,0)
BLUE=(0,0,200)
BOX1=Rect((120,120),(100,100))
BOX2=Rect((310,250),(150,170))
def draw():
    screen.clear()
    screen.fill("white")
    screen.draw.line((30,30),(200,30),("green"))
    screen.draw.line((200,30),(200,200),("green"))
    screen.draw.line((200,200),(30,200),("green"))
    screen.draw.line((30,200),(30,30),("green"))
    screen.draw.circle((200,250),110,(200,0,0))
    screen.draw.filled_circle((200,250),100,(200,0,0))
    screen.draw.filled_circle((200,250),90,(0,200,0))
    screen.draw.filled_circle((200,250),80,(0,0,200))
    screen.draw.rect(BOX1,RED)
    screen.draw.filled_rect(BOX1,GREEN)
    screen.draw.filled_rect(BOX2,BLUE)
    screen.draw.text("hello sdasjsfjn", (50, 30), color="orange")
    screen.draw.text("sdfsshdjdhashyu", (20, 100),color="blue", fontsize=60)
def update():
    BOX1.x=BOX1.x+2
    BOX2.y=BOX2.y+2
    if BOX1.x>WIDTH:
        BOX1.x=0
    if BOX2.y>HEIGHT:
        BOX2.y=0
pgzrun.go() 

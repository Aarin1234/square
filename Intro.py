import pgzrun
HEIGHT=500
WIDTH=500
TITLE="A SAMPLE"
def draw():
    screen.clear()
    screen.fill("white")
    screen.draw.line((30,30),(200,30),("green"))
    screen.draw.line((200,30),(200,200),("green"))
    screen.draw.line((200,200),(30,200),("green"))
    screen.draw.line((30,200),(30,30),("green"))
pgzrun.go() 
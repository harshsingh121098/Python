import math
import random
import pygments.lexers.python


def drawGrid(w,rows, surface):
    sizebetween =w// rows
    x=0
    y=0
    for l in range(rows):
        x+=sizebetween
        y+=sizebetween

        pygame.draw.line(surface,(255,255,255)),(x,0),(x,w)
        pygame.draw.line(surface,(255,255,255)),(0,y),(w,y)


def redrawWindow(surface):
    global rows, width
    surface.fill((0,0,0))
    drawGrid(width,rows,surface)
    pygame.display.update()
    win.fill((0,0,0))




def main():
    global width, rows
    width=500
    height=500
    rows=20
    win=pygame.display.set_mode((width,width))
    s=snake((255,0,0),(10,10))
    flag=True
    clock =pygame.time.Clock()
    while flag:
        pygame.time.delay(50)
        clock.tick(10)

        redrawWindow(win)
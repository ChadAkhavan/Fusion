import sys, pygame
import backgamonsetup as b
import configbackgamon as c
import dragging as d

#pygame.init()
#Variables
pygame.font.init()


b.drawBlackPieces()
b.drawTri()

b.CreateSpaces()
b.drawWhitePieces()
b.reRoll()
b.checkTurn()
c.myScreen.fill(c.white)

while c.running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            sys.exit()

        elif event.type==pygame.MOUSEBUTTONDOWN:
            d.CheckDragClick()

        elif event.type==pygame.MOUSEBUTTONUP:
            d.CheckDragRelease()
        elif event.type==pygame.MOUSEMOTION:
            d.CheckDragging()



    c.myScreen.fill(c.white)
    

    b.DrawEverything()

    pygame.display.flip()
pygame.quit()
sys.exit()

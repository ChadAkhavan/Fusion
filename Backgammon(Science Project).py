import random
import sys
import pygame
from pygame.locals import*

rolledNums = []
pygame.init()
def diceroll():
    diceroll = random.randint(1,6)
    rolledNums.append(diceroll)

    if (diceroll==1):
        return pygame.image.load("dice1.png")

    if (diceroll==2):
        return pygame.image.load("dice2.png")

    if (diceroll==3):
        return pygame.image.load("dice3.png")

    if (diceroll==4):
        return pygame.image.load("dice4.png")

    if (diceroll==5):
        return pygame.image.load("dice5.png")

    if (diceroll==6):
        return pygame.image.load("dice6.png")


roll1 = diceroll()
roll2 = diceroll()
    
width=1500
height=800
size=(width, height)
myScreen=pygame.display.set_mode(size)
white=(255,255,255)

black=(0,0,0)
mouse_position=(0,0)
drawing=False

myScreen.fill(white)
Spacing=62.5
Tri=[]

def DrawTri():
    
    V1=(0,0)
    V2=(125,0)
    V3=(62.5,300)
    for i in range (12): 
            pygame.draw.polygon(myScreen, black, (V1,V2,V3), 10)
            
            

            

running=True
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            pygame.quit() 
            sys.exit()
        
        elif event.type==MOUSEBUTTONDOWN:
            drawing=True

        elif event.type==MOUSEMOTION:
            if (drawing):
                mouse_position=pygame.mouse.get_pos()
                #pygame.draw.line(myScreen, black, mouse_position, mouse_position, 10)
                pygame.draw.circle(myScreen, black, mouse_position, 10)

        elif event.type==MOUSEBUTTONUP:
            mouse_position=(0,0)
            drawing=False
        
        myScreen.blit(roll1, (600, 400))
        myScreen.blit(roll2, (750, 400))
        DrawTri()

        


    pygame.display.update()





pygame.quit()
sys.exit()
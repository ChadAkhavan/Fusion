import sys, pygame
white=255,255,255
tri=[]
pieces=[]
blackpieces=[]
whitepieces=[]
color=0,0,0
gray=156, 153, 146
draggingColor=color
mouse_position=(0,0)
drawing=False
dragging=False
running=True
dragPieces=[]
width = 1500
height = 1100
radius=height/24
diameter=height/12
spacing1=width/14
spacing2=height/6
center=spacing1/2
size = (width,height)
myScreen=pygame.display.set_mode(size)
rolledNums = []
Roll=pygame.image.load("images/diceroll.png")
Roll=pygame.transform.scale(Roll,(200,200))
rollRect = Roll.get_rect(topleft=(649,649))
roll1=[pygame.image.load("images/dice1.png"),0]
roll2=[pygame.image.load("images/dice1.png"),0]
totalRoll=0
intial_pos=[]
#These are the imagineary rectatgles that make up spaces on the board
spaces=[]
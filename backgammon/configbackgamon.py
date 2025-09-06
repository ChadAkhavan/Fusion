import sys, pygame
pygame.font.init()
white=255,255,255
tri=[]
blackpieces=[]
whitepieces=[]
whitedeadpieces=[]
blackdeadpieces=[]
whitedeadrectangles=[]
blackdeadrectangles=[]
color=0,0,0
gray=156, 153, 146
draggingColor=color
draggingPos=-1
mouse_position=(0,0)
drawing=False
dragging=False
running=True
dragPieces=[]
intialdrag=[]
width = 750
height = 550
radius=height/24
diameter=height/12
spacing1=width/14
spacing2=height/6
center=spacing1/2
size = (width,height)
myScreen=pygame.display.set_mode(size)
rolledNums = []
Roll=pygame.image.load("images/diceroll.png")
Roll=pygame.transform.scale(Roll,(100,100))
rollRect = Roll.get_rect(topleft=(200,200))
roll1=[pygame.image.load("images/dice1.png"),0]
roll2=[pygame.image.load("images/dice1.png"),0]
totalRoll=0
intial_pos=[]
#These are the imagineary rectatgles that make up spaces on the board
spaces=[]
secondSpace=-1
movesLeft=[roll1[1],roll2[1]]
alerts=[]
whiteTurn=False
blackTurn=False
isResummoningW=False
isResummoningB=False
resummonSpot=-1

#Alerts

font= pygame.font.Font(None,32)
alert_text='clicked space to resummon'
Text=font.render(alert_text, True, (255,255,255), (0,0,0))
resummonBlackAlert=[Text,alert_text]


alert_text='clicked space to resummon'
Text=font.render(alert_text, True, (255,255,255), (0,0,0))
resummonWhiteAlert=[Text,alert_text]


alert_text='black\'s turn'
Text=font.render(alert_text, True, (255,255,255), (0,0,0))
BlackTurnAlert=[Text,alert_text]


alert_text='white\'s turn'
Text=font.render(alert_text, True, (255,255,255), (0,0,0))
WhiteTurnAlert=[Text,alert_text]


alert_text='dead piece'
Text=font.render(alert_text, True, (255,255,255), (0,0,0))
deadPieceAlert=[Text,alert_text]

alert_text='Turn Skipped'
Text=font.render(alert_text, True, (255,255,255), (0,0,0))
turnSkippedAlert=[Text,alert_text]

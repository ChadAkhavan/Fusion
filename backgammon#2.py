import sys, pygame
import random

pygame.init()
#Variables
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
Roll=pygame.image.load("diceroll.png")
Roll=pygame.transform.scale(Roll,(200,200))
rollRect = Roll.get_rect(topleft=(649,649))
roll1=[pygame.image.load("dice1.png"),0]
roll2=[pygame.image.load("dice1.png"),0]
totalRoll=0

def diceroll():
    diceroll = random.randint(1,6)
    rolledNums.append(diceroll)

    if (diceroll==1):
        return [pygame.image.load("dice1.png"),1]

    if (diceroll==2):
        return [pygame.image.load("dice2.png"),2]

    if (diceroll==3):
        return [pygame.image.load("dice3.png"),3]

    if (diceroll==4):
        return [pygame.image.load("dice4.png"),4]

    if (diceroll==5):
        return [pygame.image.load("dice5.png"),5]

    if (diceroll==6):
        return [pygame.image.load("dice6.png"),6]

def reRoll():
    global roll1
    global roll2
    global totalRoll
    roll1 = diceroll()
    roll2 = diceroll()
    totalRoll=roll1[1]+roll2[1]
    if roll1[1]==roll2[1]:
        totalRoll*=2

def CircleClick(circle_x, circle_y, radius, mouse_x, mouse_y):
     
     distance=((circle_x-mouse_x)**2+(circle_y-mouse_y)**2)**0.5

     return distance <=radius

def drawTri():
    start= [0,0]
    end= [spacing1/2,spacing2]
    NOL=12
    for i in range (2):
        for j in range(NOL):
             tri.append([start.copy(),end.copy()])
             if j+1<NOL:
                start=end.copy()
                if j%2==0:
                    end[0]+=spacing1/2
                    end[1]-=spacing2
                else:
                    end[1]+=spacing2
                    end[0]+=spacing1/2

        
        #moving to the right
        tri.append([end.copy(),(end.copy()[0], height)])

        tri.append([(end.copy()[0]+spacing1,end.copy()[1]),(end.copy()[0]+spacing1,height)])

        start=end.copy()
        start[0]+=spacing1*2
        end=start.copy()
        end[0]+=spacing1/2
        end[1]+=spacing2
        tri.append([start.copy(),(start.copy()[0], height)])

        
        

    for j in range(NOL):
        tri.append([start.copy(),end.copy()])
        if j+1<NOL:
            start=end.copy()
            if j%2==0:
                end[0]+=spacing1/2
                end[1]-=spacing2
            else:
                end[1]+=spacing2
                end[0]+=spacing1/2

    start= [0,height]
    end= [spacing1/2,height-spacing2]
    NOL=12
    for i in range (2):
        for j in range(NOL):
             tri.append([start.copy(),end.copy()])
             if j+1<NOL:
                start=end.copy()
                if j%2==0:
                    end[0]+=spacing1/2
                    end[1]+=spacing2
                else:
                    end[1]-=spacing2
                    end[0]+=spacing1/2

        
        #moving to the right
        start=end.copy()
        start[0]+=spacing1*2
        end=start.copy()
        end[0]+=spacing1/2
        end[1]-=spacing2

    for j in range(NOL):
        tri.append([start.copy(),end.copy()])
        if j+1<NOL:
            start=end.copy()
            if j%2==0:
                end[0]+=spacing1/2
                end[1]+=spacing2
            else:
                end[1]-=spacing2
                end[0]+=spacing1/2


def drawBlackPieces():
   #Drawing far left black pieces
    diameter=2*radius
    center= [spacing1/2,1.3*radius]
    blackpieces.append((center,radius))
    newY=1.3*radius+diameter
    newCenter= [spacing1/2,newY]
    for i in range(4):
            blackpieces.append([newCenter, radius])
            newY=1.3*radius+diameter*(i+2)
            newCenter=[spacing1/2,newY]
        #drawing middle left black pieces
    Center=[spacing1*4.5, height-1.3*radius]
    blackpieces.append([Center, radius])
    newY=height-1.3*radius-diameter
    newCenter=[spacing1*4.5,newY]
    for i in range(2):
            blackpieces.append([newCenter,radius])
            newY=height-1.3*radius-diameter*(i+2)
            newCenter=[spacing1*4.5,newY]
#drawing middle right black pieces
    Center=[spacing1*8.5, height-1.3*radius]
    blackpieces.append([Center, radius])
    newY=height-1.3*radius-diameter
    newCenter=[spacing1*8.5,newY]
    for i in range(4):
            blackpieces.append([newCenter,radius])
            newY=height-1.3*radius-diameter*(i+2)
            newCenter=[spacing1*8.5,newY]
    #drawing far right pieces
    center= [width-spacing1/2,1.3*radius]
    blackpieces.append((center,radius))
    newY=1.3*radius+diameter
    newCenter= [width-spacing1/2,newY]
    blackpieces.append([newCenter, radius])
    newY=1.3*radius+diameter*(3)
    newCenter=[width-spacing1/2,newY]
    '''for i in range (6):
        if i==0:
            pass
        else:
             pieces.append(((spacing1/2,i*1.972*radius), radius))
        #pieces.append(((spacing1/2,i*2*radius), radius))'''


def drawWhitePieces():
    center= [spacing1/2,height-1.3*radius]
    whitepieces.append((center,radius))
    newY=height-1.3*radius-diameter
    newCenter= [spacing1/2,newY]
    for i in range(4):
            whitepieces.append([newCenter, radius])
            newY=height-1.3*radius-diameter*(i+2)
            newCenter=[spacing1/2,newY]
        #drawing middle left white pieces
    Center=[spacing1*4.5, 1.3*radius]
    whitepieces.append([Center, radius])
    newY=1.3*radius+diameter
    newCenter=[spacing1*4.5,newY]
    for i in range(2):
            whitepieces.append([newCenter,radius])
            newY=1.3*radius+diameter*(i+2)
            newCenter=[spacing1*4.5,newY]
#drawing middle right white pieces
    Center=[spacing1*8.5, 1.3*radius]
    whitepieces.append([Center, radius])
    newY=1.3*radius+diameter
    newCenter=[spacing1*8.5,newY]
    for i in range(4):
            whitepieces.append([newCenter,radius])
            newY=1.3*radius+diameter*(i+2)
            newCenter=[spacing1*8.5,newY]
    #drawing far right white pieces
    center= [width-spacing1/2,height-1.3*radius]
    whitepieces.append((center,radius))
    newY=height-1.3*radius-diameter
    newCenter= [width-spacing1/2,newY]
    whitepieces.append([newCenter, radius])
    newY=height-1.3*radius-diameter*(3)
    newCenter=[width-spacing1/2,newY]

def DrawEverything():
    pygame.draw.rect(myScreen, color, pygame.Rect((0,0),(width,height)), 7)

    for line in tri:
        pygame.draw.line(myScreen,color,line[0], line[1], 3 )

    for piece in blackpieces:
        pygame.draw.circle(myScreen, color, piece[0], piece[1])

    for piece in whitepieces:
         pygame.draw.circle(myScreen, gray, piece[0], piece[1])
    
    for piece in dragPieces:
         pygame.draw.circle(myScreen, piece[0], piece[1], piece[2])
         

    myScreen.blit(roll1[0], (6.10*spacing1, height/2.75))
    myScreen.blit(roll2[0], (7.13*spacing1, height/2.75))
    myScreen.blit(Roll, (649,649))
drawBlackPieces()
drawTri()
drawWhitePieces()
reRoll()
myScreen.fill(white)
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            sys.exit()

        elif event.type==pygame.MOUSEBUTTONDOWN:
            dragPieces=[]
            mouse_x, mouse_y=pygame.mouse.get_pos()
            pieceClicked=False
            if rollRect.collidepoint(mouse_x,mouse_y):
                reRoll()
                print("totalRoll = "+str(totalRoll))
            for piece in blackpieces:
                 if CircleClick(piece[0][0],piece[0][1],piece[1],mouse_x,mouse_y):
                      dragging=True
                      draggingColor=color
                      blackpieces.remove(piece)
                      dragPieces.append([draggingColor, piece[0], piece[1]])
                      pieceClicked=True
                      break
            if(not pieceClicked):
                for piece in whitepieces:
                    if CircleClick(piece[0][0],piece[0][1],piece[1],mouse_x,mouse_y):
                        dragging=True
                        draggingColor=gray
                        whitepieces.remove(piece)
                        dragPieces.append([draggingColor, piece[0], piece[1]])
                        break
        elif event.type==pygame.MOUSEBUTTONUP:
            #drawing=False
            dragging=False
            if(len(dragPieces)>0):
                FinalPos=dragPieces.pop(0)
                if (FinalPos[0]==gray):
                    FinalPos.pop(0)
                    whitepieces.append(FinalPos)
                else:
                    FinalPos.pop(0)
                    blackpieces.append(FinalPos)

        elif event.type==pygame.MOUSEMOTION:
            mouse_position=pygame.mouse.get_pos()
                
            if (dragging):
                 dragPieces.append([draggingColor,mouse_position,radius])


            if(len(dragPieces)>1):
                
                dragPieces.pop(0)
            #elif (drawing):
               # pygame.draw.circle(myScreen, color, mouse_position, 10)


    myScreen.fill(white)
    

    DrawEverything()

    pygame.display.flip()
pygame.quit()
sys.exit()

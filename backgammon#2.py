import sys, pygame
import random

pygame.init()

width = 1500
height = 1100
size = (width,height)
myScreen=pygame.display.set_mode(size)


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


white=255,255,255
tri=[]
pieces=[]
blackpieces=[]
whitepieces=[]
spacing1=width/14
spacing2=height/6
color=0,0,0
mouse_position=(0,0)
drawing=False

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

#def columb 
radius=height/24
diameter=height/12
center=spacing1/2

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
running=True

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
drawBlackPieces()
drawTri()
drawWhitePieces()
myScreen.fill(white)
while running:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            sys.exit()


        elif event.type==pygame.MOUSEBUTTONDOWN:
            drawing=True

        elif event.type==pygame.MOUSEMOTION:
            if (drawing):
                mouse_position=pygame.mouse.get_pos()
                #pygame.draw.line(myScreen, black, mouse_position, mouse_position, 10)
                pygame.draw.circle(myScreen, color, mouse_position, 10)

        elif event.type==pygame.MOUSEBUTTONUP:
            mouse_position=(0,0)
            drawing=False

    

    pygame.draw.rect(myScreen, color, pygame.Rect((0,0),(width,height)), 7)

    for line in tri:
        pygame.draw.line(myScreen,color,line[0], line[1], 3 )

    for piece in blackpieces:
        pygame.draw.circle(myScreen, color, piece[0], piece[1])

    for piece in whitepieces:
         pygame.draw.circle(myScreen, (156, 153, 146), piece[0], piece[1])

    myScreen.blit(roll1, (6.10*spacing1, height/2.75))
    myScreen.blit(roll2, (7.13*spacing1, height/2.75))

    pygame.display.flip()
pygame.quit()
sys.exit()

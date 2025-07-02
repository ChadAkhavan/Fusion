import sys, pygame
import configbackgamon as c
import random

def diceroll():
    diceroll = random.randint(1,6)
    c.rolledNums.append(diceroll)

    if (diceroll==1):
        return [pygame.image.load("images/dice1.png"),1]

    if (diceroll==2):
        return [pygame.image.load("images/dice2.png"),2]

    if (diceroll==3):
        return [pygame.image.load("images/dice3.png"),3]

    if (diceroll==4):
        return [pygame.image.load("images/dice4.png"),4]

    if (diceroll==5):
        return [pygame.image.load("images/dice5.png"),5]

    if (diceroll==6):
        return [pygame.image.load("images/dice6.png"),6]

def reRoll():
    if c.movesLeft==0:
        print("No moves left switching turns")
        if(c.whiteTurn):
            c.whiteTurn=False
            c.blackTurn=True
            font= pygame.font.Font(None,32)
            alert_text='black\'s turn'
            Text=font.render(alert_text, True, (255,255,255), (0,0,0))
            c.alerts.append([Text,alert_text])
        elif(c.blackTurn):
            c.whiteTurn=True
            c.blackTurn=False
            font= pygame.font.Font(None,32)
            alert_text='white\'s turn'
            Text=font.render(alert_text, True, (255,255,255), (0,0,0))
            c.alerts.append([Text,alert_text])
    c.roll1 = diceroll()
    c.roll2 = diceroll()
    c.totalRoll=c.roll1[1]+c.roll2[1]
    if c.roll1[1]==c.roll2[1]:
        c.totalRoll*=2
    c.movesLeft = c.totalRoll
    if (len(c.whitedeadrectangles) !=0):
        c.whitedeadpiece=True
        font= pygame.font.Font(None,32)
        alert_text='dead piece'
        Text=font.render(alert_text, True, (255,255,255), (0,0,0))
        c.alerts.append([Text,alert_text])
        c.whitedeadpiece=True
    if (len(c.blackdeadrectangles) !=0):
        c.Blackdeadpiece=True
        font= pygame.font.Font(None,32)
        alert_text='dead piece'
        Text=font.render(alert_text, True, (255,255,255), (0,0,0))
        c.alerts.append([Text,alert_text])
def checkTurn():
    if c.roll1[1]>c.roll2[1]:
        c.blackTurn=True
        font= pygame.font.Font(None,32)
        alert_text='black\'s turn'
        Text=font.render(alert_text, True, (255,255,255), (0,0,0))
        c.alerts.append([Text,alert_text])
        return c.blackTurn
    elif c.roll2[1]>c.roll1[1]:
        c.whiteTurn=True
        font= pygame.font.Font(None,32)
        alert_text='white\'s turn'
        Text=font.render(alert_text, True, (255,255,255), (0,0,0))
        c.alerts.append([Text,alert_text])
        return c.whiteTurn
    else:
        reRoll()
        checkTurn()


def CircleClick(circle_x, circle_y, radius, mouse_x, mouse_y):
     
     distance=((circle_x-mouse_x)**2+(circle_y-mouse_y)**2)**0.5

     return distance <=radius

def drawTri():
    start= [0,0]
    end= [c.spacing1/2,c.spacing2]
    NOL=12
    for i in range (2):
        for j in range(NOL):
             c.tri.append([start.copy(),end.copy()])
             if j+1<NOL:
                start=end.copy()
                if j%2==0:
                    end[0]+=c.spacing1/2
                    end[1]-=c.spacing2
                else:
                    end[1]+=c.spacing2
                    end[0]+=c.spacing1/2

        
        #moving to the right
        c.tri.append([end.copy(),(end.copy()[0], c.height)])

        c.tri.append([(end.copy()[0]+c.spacing1,end.copy()[1]),(end.copy()[0]+c.spacing1,c.height)])

        start=end.copy()
        start[0]+=c.spacing1*2
        end=start.copy()
        end[0]+=c.spacing1/2
        end[1]+=c.spacing2
        c.tri.append([start.copy(),(start.copy()[0], c.height)])

        
        

    for j in range(NOL):
        c.tri.append([start.copy(),end.copy()])
        if j+1<NOL:
            start=end.copy()
            if j%2==0:
                end[0]+=c.spacing1/2
                end[1]-=c.spacing2
            else:
                end[1]+=c.spacing2
                end[0]+=c.spacing1/2

    start= [0,c.height]
    end= [c.spacing1/2,c.height-c.spacing2]
    NOL=12
    for i in range (2):
        for j in range(NOL):
             c.tri.append([start.copy(),end.copy()])
             if j+1<NOL:
                start=end.copy()
                if j%2==0:
                    end[0]+=c.spacing1/2
                    end[1]+=c.spacing2
                else:
                    end[1]-=c.spacing2
                    end[0]+=c.spacing1/2

        
        #moving to the right
        start=end.copy()
        start[0]+=c.spacing1*2
        end=start.copy()
        end[0]+=c.spacing1/2
        end[1]-=c.spacing2

    for j in range(NOL):
        c.tri.append([start.copy(),end.copy()])
        if j+1<NOL:
            start=end.copy()
            if j%2==0:
                end[0]+=c.spacing1/2
                end[1]+=c.spacing2
            else:
                end[1]-=c.spacing2
                end[0]+=c.spacing1/2


def drawBlackPieces():
   #Drawing far left black pieces
    diameter=2*c.radius
    center= [c.spacing1/2,1.3*c.radius]
    c.blackpieces.append([center,c.radius,12])
    newY=1.3*c.radius+diameter
    newCenter= [c.spacing1/2,newY]
    for i in range(4):
            c.blackpieces.append([newCenter, c.radius,12])
            newY=1.3*c.radius+diameter*(i+2)
            newCenter=[c.spacing1/2,newY]
        #drawing middle left black pieces
    Center=[c.spacing1*4.5, c.height-1.3*c.radius]
    c.blackpieces.append([Center, c.radius,7])
    newY=c.height-1.3*c.radius-diameter
    newCenter=[c.spacing1*4.5,newY]
    for i in range(2):
            c.blackpieces.append([newCenter,c.radius,7])
            newY=c.height-1.3*c.radius-diameter*(i+2)
            newCenter=[c.spacing1*4.5,newY]
#drawing middle right black pieces
    Center=[c.spacing1*8.5, c.height-1.3*c.radius]
    c.blackpieces.append([Center, c.radius,5])
    newY=c.height-1.3*c.radius-diameter
    newCenter=[c.spacing1*8.5,newY]
    for i in range(4):
            c.blackpieces.append([newCenter,c.radius,5])
            newY=c.height-1.3*c.radius-diameter*(i+2)
            newCenter=[c.spacing1*8.5,newY]
    #drawing far right pieces
    center= [c.width-c.spacing1/2,1.3*c.radius]
    c.blackpieces.append([center,c.radius,23])
    newY=1.3*c.radius+diameter
    newCenter= [c.width-c.spacing1/2,newY]
    c.blackpieces.append([newCenter, c.radius,23])
    newY=1.3*c.radius+diameter*(3)
    newCenter=[c.width-c.spacing1/2,newY]
    '''for i in range (6):
        if i==0:
            pass
        else:
             pieces.append(((spacing1/2,i*1.972*radius), radius))
        #pieces.append(((spacing1/2,i*2*radius), radius))'''


def drawWhitePieces():
    center= [c.spacing1/2,c.height-1.3*c.radius]
    c.whitepieces.append([center,c.radius,11])
    newY=c.height-1.3*c.radius-c.diameter
    newCenter= [c.spacing1/2,newY]
    for i in range(4):
            c.whitepieces.append([newCenter, c.radius,11])
            newY=c.height-1.3*c.radius-c.diameter*(i+2)
            newCenter=[c.spacing1/2,newY]
        #drawing middle left white pieces
    Center=[c.spacing1*4.5, 1.3*c.radius]
    c.whitepieces.append([Center, c.radius,16])
    newY=1.3*c.radius+c.diameter
    newCenter=[c.spacing1*4.5,newY]
    for i in range(2):
            c.whitepieces.append([newCenter,c.radius,16])
            newY=1.3*c.radius+c.diameter*(i+2)
            newCenter=[c.spacing1*4.5,newY]
#drawing middle right white pieces
    Center=[c.spacing1*8.5, 1.3*c.radius]
    c.whitepieces.append([Center, c.radius,18])
    newY=1.3*c.radius+c.diameter
    newCenter=[c.spacing1*8.5,newY]
    for i in range(4):
            c.whitepieces.append([newCenter,c.radius,18])
            newY=1.3*c.radius+c.diameter*(i+2)
            newCenter=[c.spacing1*8.5,newY]
    #drawing far right white pieces
    center= [c.width-c.spacing1/2,c.height-1.3*c.radius]
    c.whitepieces.append([center,c.radius,0])
    newY=c.height-1.3*c.radius-c.diameter
    newCenter= [c.width-c.spacing1/2,newY]
    c.whitepieces.append([newCenter, c.radius,0])
    newY=c.height-1.3*c.radius-c.diameter*(3)
    newCenter=[c.width-c.spacing1/2,newY]

def CreateSpaces():
    y=c.height/2
    x=c.width-c.spacing1
    for i in range(6):
        c.spaces.append(pygame.Rect(x,y,c.spacing1,c.height/2))
        x-=c.spacing1

    x=c.spacing1*5
    for i in range(6):
        c.spaces.append(pygame.Rect(x,y,c.spacing1,c.height/2))
        x-=c.spacing1

    x,y=0,0
    for i in range(6):
        c.spaces.append(pygame.Rect(x,y,c.spacing1,c.height/2))
        x+=c.spacing1
    
    x=c.spacing1*8
    for i in range(6):
        c.spaces.append(pygame.Rect(x,y,c.spacing1,c.height/2))
        x+=c.spacing1
def DrawEverything():
    pygame.draw.rect(c.myScreen, c.color, pygame.Rect((0,0),(c.width,c.height)), 7)

    for line in c.tri:
        pygame.draw.line(c.myScreen,c.color,line[0], line[1], 3 )

    for piece in c.blackpieces:
        pygame.draw.circle(c.myScreen, c.color, piece[0], piece[1])

    for piece in c.whitepieces:
         pygame.draw.circle(c.myScreen, c.gray, piece[0], piece[1])
    
    for piece in c.dragPieces:
         pygame.draw.circle(c.myScreen, piece[0], piece[1], piece[2])
    DrawDeadPieces()
    for rect in c.whitedeadrectangles:
        pygame.draw.rect(c.myScreen,rect[1],rect[0])
    '''for rectangle in c.spaces:
        pygame.draw.rect(c.myScreen, c.color,rectangle)'''
    for rect in c.blackdeadrectangles:
        pygame.draw.rect(c.myScreen,rect[1],rect[0])

    for alert in c.alerts:
        alert_rect=alert[0].get_rect()
        if alert[1]=='dead piece':
            alert_rect.center=(100,40)

        if alert[1]=='black\'s turn' or alert[1]=='white\'s turn':
            alert_rect.center=(c.width-100,40)
        #alert_rect.center=(c.width//2, c.height//2)
        if alert[1]=='clicked space to resummon':
            alert_rect.center=(c.width/2,c.height/2)
        c.myScreen.blit(alert[0],alert_rect)
    
    c.myScreen.blit(c.roll1[0], (6.10*c.spacing1, c.height/2.75))
    c.myScreen.blit(c.roll2[0], (7.13*c.spacing1, c.height/2.75))
    c.myScreen.blit(c.Roll, (649,649))

def DrawDeadPieces():
    Wleft=c.spacing1*6
    ctop=10
    btop=10
    width=c.spacing1/2
    hieght=20
    c.whitedeadrectangles=[]
    for piece in c.deadpieces:
        if piece[1]==c.gray:
            c.whitedeadrectangles.append((pygame.Rect(Wleft,ctop,width,hieght),piece[1]))
            ctop +=30

    Bleft=Wleft+width
    c.blackdeadrectangles=[]
    for piece in c.deadpieces:
         if piece[1]==c.color:
            c.blackdeadrectangles.append((pygame.Rect(Bleft,btop,width,hieght),piece[1]))
            btop+=30
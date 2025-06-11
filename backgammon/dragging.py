import pygame, sys
import configbackgamon as c
import backgamonsetup as b
import math

def CheckDragClick():
    mouse_x, mouse_y=pygame.mouse.get_pos()
    pieceClicked=False
    if c.rollRect.collidepoint(mouse_x,mouse_y):
        b.reRoll()
        print("totalRoll = "+str(c.totalRoll))
    for piece in c.blackpieces:
            if b.CircleClick(piece[0][0],piece[0][1],piece[1],mouse_x,mouse_y):
                c.dragging=True
                c.draggingColor=c.color
                c.draggingPos = piece[2]
                c.blackpieces.remove(piece)
                c.dragPieces.append([c.draggingColor, piece[0], piece[1],piece[2]])
                c.intial_pos=[c.draggingColor, piece[0], piece[1], piece[2]]
                pieceClicked=True
                break
    if(not pieceClicked):
        for piece in c.whitepieces:
            if b.CircleClick(piece[0][0],piece[0][1],piece[1],mouse_x,mouse_y):
                c.dragging=True
                c.draggingColor=c.gray
                c.draggingPos = piece[2]
                c.whitepieces.remove(piece)
                c.dragPieces.append([c.draggingColor, piece[0], piece[1],piece[2]])
                c.intial_pos=[c.draggingColor, piece[0], piece[1], piece[2]]
                break
                
def CheckDragRelease():
    #drawing=False
    c.dragging=False
    if(len(c.dragPieces)>0):
        FinalPos=c.dragPieces.pop(0)
        if(c.movesLeft == 0):
            print("NO MOVES LEFT")
            if (FinalPos[0]==c.gray):
                    c.whitepieces.append([c.intial_pos[1],c.intial_pos[2],c.intial_pos[3]])
            else:
                c.blackpieces.append([c.intial_pos[1],c.intial_pos[2],c.intial_pos[3]])
            return
        print("the piece is being moved from"+str(FinalPos[3]))
        #calc first closest space
        FinalSpot=getFirstSpot(FinalPos)
        #calc space the piece is closest to if touching 2, redefining final spot
        if c.secondSpace != -1:
            FinalSpot=findclosestspace(FinalPos,FinalSpot)
        #find if that's a valid move
        NewSpace=isValidMove(FinalSpot,FinalPos)
        print("The space you are moving to is : "+str(NewSpace))
        if (NewSpace>=0):
            print("valid move")
            NewSpaceX=c.spaces[NewSpace].center[0]
            NewSpaceY=findY(NewSpace)
            if (FinalPos[0]==c.gray):
                c.whitepieces.append([[NewSpaceX, NewSpaceY],FinalPos[2],NewSpace])
            else:
                c.blackpieces.append([[NewSpaceX, NewSpaceY],FinalPos[2],NewSpace])
        else:
            print("not valid ")
            if (FinalPos[0]==c.gray):
                c.whitepieces.append([c.intial_pos[1],c.intial_pos[2],c.intial_pos[3]])
            else:
                c.blackpieces.append([c.intial_pos[1],c.intial_pos[2],c.intial_pos[3]])
def CheckDragging():
    mouse_position=pygame.mouse.get_pos()
                
    if (c.dragging):
            c.dragPieces.append([c.draggingColor,mouse_position,c.radius,c.draggingPos])

    if(len(c.dragPieces)>1):
        
        c.dragPieces.pop(0)

def getFirstSpot(pos):
    newSpot=None
    for space in c.spaces:
        if space.collidepoint(pos[1]):
            newSpot=c.spaces.index(space)
            print("the piece is being moved to (first spot the piece touches) "+str(newSpot))
            print("the piece is being moved to (second spot the piece touches) "+str(newSpot+1))
            c.secondSpace=newSpot+1
            break

    if (newSpot==None):
        return False
    return newSpot

def isValidMove(newSpot,pos):
    print("roll 1: "+str(c.roll1[1]))
    print("roll 2: "+str(c.roll2[1]))
    color=pos[0]
    oldspot=pos[3]
    print("total roll = "+str(c.totalRoll))
    print("moves left = "+str(c.movesLeft))
    
    if color==c.color:
        print("oldspot - newSpot = "+str((oldspot-newSpot)))
        wp=[]
        for piece in c.whitepieces:
            if piece[2] == newSpot:
                wp.append(piece)
        print("there are "+str(len(wp))+" white pieces already there")
        if ((oldspot-newSpot)>0) and (oldspot-newSpot <= c.movesLeft) and (oldspot-newSpot== c.roll1[1] or oldspot-newSpot==c.roll2[1]) and (len(wp)<2) and (len(c.blackdeadrectangles)==0):
            c.movesLeft -= oldspot-newSpot
            if len(wp)==1:
                capture(wp[0],color)
            return newSpot
        else:
            if (len(c.blackdeadrectangles) !=0):
                font= pygame.font.Font(None,32)
                Text=font.render('Dead Piece', True, (255,255,255), (0,0,0))
                c.alerts.append(Text)
            return -1
    elif color==c.gray:
        print("newspot - oldspot = "+str((newSpot-oldspot)))
        bp=[]
        for piece in c.blackpieces:
            if piece[2] == newSpot:
                bp.append(piece)
        print("there are "+str(len(bp))+" black pieces already there")
        if ((newSpot-oldspot)>0) and (newSpot-oldspot <= c.movesLeft)and (newSpot-oldspot== c.roll1[1] or newSpot-oldspot==c.roll2[1]) and (len(bp)<2) and (len(c.whitedeadrectangles)==0):
            c.movesLeft -= newSpot-oldspot
            if len(bp)==1:
                capture(bp[0],color)
            return newSpot
        else:
            if (len(c.whitedeadrectangles) !=0):
                font= pygame.font.Font(None,32)
                Text=font.render('Dead Piece', True, (255,255,255), (0,0,0))
                c.alerts.append(Text)
            return -1
    else:
        return -1
        
def findclosestspace(piece,space):
#takes the given piece and returns the space it is closest to, the first spot the piece is touching or the one after
    range=c.height/48
    centerOfPiece= piece[1]
    centerSpace1= c.spaces[space].center
    if(len(c.spaces)> c.secondSpace):
        centerspace2=c.spaces[c.secondSpace].center
        if math.dist(centerOfPiece,centerSpace1)>math.dist(centerOfPiece,centerspace2):
            print("closer to the higher piece")
            return c.secondSpace
        else:
            print("closer to the lower piece")
            return space
    return space

def findY(space):
    count=0
    for piece in c.whitepieces:
        if(piece[2]==space):
            count+=1
    for piece in c.blackpieces:
        if(piece[2]==space):
            count+=1

    if (space <= 11):
        return c.height-c.diameter*count-c.radius
    elif (space>11):
        return c.diameter*count+c.radius
    else:
        return 0
    
def capture(piece,color):
    if color==c.color:
        c. whitepieces.remove(piece)
        c.deadpieces.append((piece,c.gray))
    elif color==c.gray:
        c.blackpieces.remove(piece)
        c.deadpieces.append((piece,c.color))

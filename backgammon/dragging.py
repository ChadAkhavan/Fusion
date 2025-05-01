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
        firstspace=getFirstSpot(FinalPos)
        print("the piece is being moved from"+str(FinalPos[3]))
        FinalSpot=findclosestspace(FinalPos,firstspace)
        NewSpace=isValidMove(FinalSpot,FinalPos)
        if (NewSpace):
            print("valid move")
            if (FinalPos[0]==c.gray):
                findclosestspace(FinalPos,NewSpace)
                c.whitepieces.append([FinalPos[1],FinalPos[2],NewSpace])
            else:
                c.blackpieces.append([FinalPos[1],FinalPos[2],NewSpace])
        else:
            print("not avlid ")
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
        if space.collidepoint(pos[1][0],pos[1][1]):
            print("the piece is being moved to"+str(c.spaces.index(space)))
            newSpot=c.spaces.index(space)
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
    
    if color==c.color:
        print("newspot - oldspot = "+str((oldspot-newSpot)))
        if ((oldspot-newSpot)==c.roll1[1]) or ((oldspot-newSpot)==c.roll2[1]) or ((oldspot-newSpot)==c.totalRoll):
            print("ye")
            return newSpot
    elif color==c.gray:
        print("oldspot - newspot = "+str((newSpot-oldspot)))
        if ((newSpot-oldspot)==c.roll1[1]) or ((newSpot-oldspot)==c.roll2[1]) or ((newSpot-oldspot)==c.totalRoll):
            print("YES!")
            return newSpot
        else:
            return False
def findclosestspace(piece,space):
#takes the given piece and returns the space it is closest to
    range=c.height/48
    centerOfPiece= piece[1]
    centerSpace1= c.spaces[space].center
    centerspace2=c.spaces[c.secondSpace].center
    if math.dist(centerOfPiece,centerSpace1)>math.dist(centerOfPiece,centerspace2):
        print("closer to the lower piece")
        return c.secondSpace
    else:
        print("closer ot the higher piece")
        return space
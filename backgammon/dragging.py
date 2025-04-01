import pygame, sys
import configbackgamon as c
import backgamonsetup as b

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
                c.blackpieces.remove(piece)
                c.dragPieces.append([c.draggingColor, piece[0], piece[1]])
                c.intial_pos=[c.draggingColor, piece[0], piece[1]]
                pieceClicked=True
                break
    if(not pieceClicked):
        for piece in c.whitepieces:
            if b.CircleClick(piece[0][0],piece[0][1],piece[1],mouse_x,mouse_y):
                c.dragging=True
                c.draggingColor=c.gray
                c.whitepieces.remove(piece)
                c.dragPieces.append([c.draggingColor, piece[0], piece[1]])
                break
                
def CheckDragRelease():
    #drawing=False
    c.dragging=False
    if(len(c.dragPieces)>0):
        FinalPos=c.dragPieces.pop(0)
        if (isValidMove(FinalPos)):
             
            if (FinalPos[0]==c.gray):
                FinalPos.pop(0)
                c.whitepieces.append(FinalPos)
            else:
                FinalPos.pop(0)
                c.blackpieces.append(FinalPos)

def CheckDragging():
    mouse_position=pygame.mouse.get_pos()
                
    if (c.dragging):
            c.dragPieces.append([c.draggingColor,mouse_position,c.radius])


    if(len(c.dragPieces)>1):
        
        c.dragPieces.pop(0)

def isValidMove(pos):
    return True

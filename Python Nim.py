import extracode
import sys
import pygame



width = 1500
height = 1100
size = (width,height)
myScreen=pygame.display.set_mode(size)

matches=[]

def drawlines():
    start= [225, 1000]
    end= [225, 850]
    NOL=1
    move = False
    for i in range (4):
        for j in range(NOL):
             matches.append([start.copy(),end.copy(), False])
             if j+1<NOL:
                start[1]-=spacing
                end[1]-=spacing
        start[1]=1000
        end[1]=850
        NOL+=1
        #moving to the right
        start[0]+=spacing
        end[0]+=spacing
    NOL = 3
    for i in range (3):
        for j in range(NOL):
             matches.append([start.copy(), end.copy(), False])
             if j+1<NOL:
                start[1]-=spacing
                end[1]-=spacing
        start[1]=1000
        end[1]=850
        NOL-=1
        #moving to the right
        start[0]+=spacing
        end[0]+=spacing


    '''  
        pygame.draw.line(screen, lineColor, start, end, 5)
    '''
    

pygame.init()
white=255,255,255
color=(0,0,0)
color2=(255,0,0)
spacing= 175
drawing=False
hasdrawn=False
start_pos=None
end_pos=None
playerlines=[]

#Var for Bounderies
y1=837.5
y2=662.5
y3=487.5

running= True
drawlines()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            drawing=True
            start_pos=event.pos
            if(hasdrawn):
                end_pos=None
        elif event.type==pygame.MOUSEBUTTONUP:
            drawing=False
            hasdrawn=True
            end_pos=event.pos
            if not (extracode.calculateIntersectPoint(start_pos, end_pos, (0,y1), (1500, y1))) and not (extracode.calculateIntersectPoint(start_pos, end_pos, (0, y2), (1500, y2))) and not (extracode.calculateIntersectPoint(start_pos, end_pos, (0,y3), (1500,y3))):
                potentialLine=(start_pos,end_pos)
                crossing=False
                crossedmatches=[]
                
                draw=True
                for match in matches: 
                    if (extracode.calculateIntersectPoint(start_pos,end_pos,match[0],match[1])):
                            crossedmatches.append(match)
                if(len(crossedmatches))<1:
                    draw=False
                for match in crossedmatches:
                    if match[2]:
                        draw=False 
                if draw:
                    playerlines.append(potentialLine)
                    for match in crossedmatches:
                        match[2]=True
                            
        elif event.type==pygame.MOUSEMOTION and drawing:
            end_pos=event.pos
    myScreen.fill(white)
    #pygame.draw.line(screen, (0,0,0), starting, ending, 5)
    pygame.draw.line(myScreen, color2, (0,837.5), (1500,837.5), 3)
    pygame.draw.line(myScreen, color2, (0,662.5), (1500,662.5), 3)
    pygame.draw.line(myScreen, color2, (0,487.5), (1500,487.5), 3)
    for line in matches:
        pygame.draw.line(myScreen,color,line[0], line[1], 3 )
    for line in playerlines:
        pygame.draw.line(myScreen,color,line[0], line[1], 3 )
    if start_pos and end_pos:
        pygame.draw.line(myScreen, color, start_pos, end_pos, 3)
    pygame.display.update()
pygame.quit()
sys.exit()






















































    


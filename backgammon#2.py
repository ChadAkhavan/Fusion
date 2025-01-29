import sys, pygame

pygame.init()

width = 1500
height = 1100
size = (width,height)
myScreen=pygame.display.set_mode(size)

white=255,255,255
tri=[]
spacing1=width/14
spacing2=height/6
color=0,0,0

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
        start=end.copy()
        start[0]+=spacing1*2
        end=start.copy()
        end[0]+=spacing1/2
        end[1]+=spacing2

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



running=True
drawTri()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: sys.exit()

    myScreen.fill(white)

    for line in tri:
        pygame.draw.line(myScreen,color,line[0], line[1], 3 )

    pygame.display.flip()
pygame.quit()
sys.exit()

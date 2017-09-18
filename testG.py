import numpy
import pygame
import sys
from random import randint

n=input("ENTER DIM: ") #width and height
pygame.font.init()
font2=pygame.font.SysFont("monospace",500/(n*2))
font=pygame.font.SysFont("monospace",500/(n))
pygame.init()
pygame.display.set_caption('puzzle')
window=pygame.display.set_mode((700,700)) #set window size
bgc=(0,0,0) #set background color number
window.fill(bgc)
g=numpy.zeros([n,n,3]) #make grid array of feilds (box val, moves to box, visited (1=y, 0=n))
bs=700/n

#INITIALIZATION AND GRAPHICS STUFF====================================================

def grid(): #draw the nxn grid and print 2d arr values for each square
	for x in range(n):
		for y in range(n):
			g[x][y][0]=int(randint(1,max([n-x-1,x-1,n-y-1,y-1])))#init vals
			rect=pygame.Rect(x*bs,y*bs,bs,bs)
			pygame.draw.rect(window,((23*x)%255,(17*y)%255,(x*y)%255),rect)
			char=str(int(g[x][y][0])) #print the move value for each square
			char2=str(int(g[x][y][1])) #To print num of moves 
			text=font.render(char,1,(255,255,255))
			window.blit(text,(x*bs+2,y*bs+2))
			text=font2.render(char2,1,(255,255,0)) #to print num of moves
			window.blit(text,(x*bs+bs/2+(500/(n*3.5)),y*bs+bs/2+(500/(n*3.5))))
	g[n-1][n-1]=0
	rect=pygame.Rect((n-1)*bs,(n-1)*bs,bs,bs)
	pygame.draw.rect(window,(255,255,255),rect)
	pygame.display.update()
	text=font.render("G",1,(0,0,0))
	window.blit(text,((n-1)*bs+2,(n-1)*bs+2))
	char2=str(int(g[x][y][1]))
	text=font2.render(char2,1,(5,5,255))
	window.blit(text,(x*bs+bs/2+(500/(n*3.5)),y*bs+bs/2+(500/(n*3.5))))
	pygame.display.update()
#=======================================================================================
#(box val,num moves,visited?)
def bfs(x,y): #takes a point defined by x pos and y pos
	fifo=[] #use fifo.pop(0) to get first, fifo.append(#) to put at end
	move=g[x][y][0]
	if g[x+move][y][2]==0 and x+move in range(n):#move right
		fifo.append((x+move,y))
	if g[x-move][y][2]==0 and x-move in range(n):#move left
		fifo.append((x-move,y))
	if g[x][y+move][2]==0 and y+move in range(n):#move down
		fifo.append((x,y+move))
	if g[x][y-move][2]==0 and y-move in range(n):#move up
		fifo.append((x,y-move))
	while fifo:#list not empty
		new=fifo.pop(0)
		#add to tree
		bfs(new[0],new[1])




#======================================================================================
grid()
#bfs(0,0)
while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			sys.exit()










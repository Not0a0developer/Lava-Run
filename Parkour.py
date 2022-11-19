import pygame, sys
import time
from pygame.locals import *
from pygame import mixer
pygame.init()

CLOCK=pygame.time.Clock()
reverse=0

#jump
Isjumping=False
JumpCount=7
maxStep=7
Jumpstep=maxStep

#Screen Management
font = pygame.font.SysFont(pygame.font.get_default_font(),40)
width = 1400
h = 800
screen = pygame.display.set_mode((width, h))
tilel = []
getin=[]
score = 0
level = 1

#Background
bgImage = pygame.image.load('Lava.png') 
bgImage = pygame.transform.scale(bgImage,(width,h)) 
backX = 0
backX2 = width

#Rect
r1 = pygame.Rect(0, 0, 50, 71)
r3 = pygame.Rect(0,150,50,50)
r4 = pygame.Rect(650,80,120,120)
r5 = pygame.Rect(0,0,100,120)
#pygame.draw.rect(screen,(255,255,255),r3)
pygame.display.update()
onair=True

#images
image1 = pygame.image.load('walk.png')
image1 = pygame.transform.scale(image1, (50, 80))

image2 = pygame.image.load('jump.png')
image2 = pygame.transform.scale(image2, (50, 80))

image3=pygame.transform.flip(image1,True,False)

image4=pygame.transform.flip(image2,True,False)

image5=pygame.image.load('Portal.gif')
image5=pygame.transform.scale(image5,(120,120))

image6=pygame.image.load('Step.png')
image6=pygame.transform.scale(image6,(50,50))

image7=pygame.image.load('Reverse.jpg')
image7=pygame.transform.scale(image7,(100,120))
bear = image1

#Tiles
for i in range(5):
	polygon1=pygame.Rect(135,150,50,50)
	polygon1.x=polygon1.x + 135*i
	tilel.append(polygon1)

#BG Music
mixer.music.load('BG.mp3')
mixer.music.play()
#Game
pygame.display.update()
while True:
	time.sleep(0.01)
	text = font.render('Hello!',True,(255,255,255))
	if r1.colliderect(r4):
		mixer.music.pause()
		r1.x = r4.x
		r1.y = r4.y
		r1.x = 0
		r1.y = 30
		score += 5
		level += 1
		mixer.music.load('BG.mp3')
		mixer.music.play()
	#QUIT
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	#THIS TOOK SOOOOO MUCH TIME OMG JUMPPPPPPPPPPP
	onair=True
	for erect in tilel:
		if (r1.colliderect(r3) or r1.colliderect(erect)) and r1.bottom >= erect.top:
			onair = False

	if onair:
		r1.y += 30
	#Moving
	keyInput = pygame.key.get_pressed()
	if reverse == 0:
		if keyInput[K_LEFT] and r1.left >= 0:
			r1.left -= 5
			backX += 1.5
			backX2 += 1.5
			bear=image3

		if keyInput[K_RIGHT] and r1.right <= width:
			r1.right += 5
			backX -= 1.5
			backX2 -= 1.5
			bear=image1
	if reverse == 1:
		if keyInput[K_RIGHT] and r1.left >= 0:
			r1.left -= 5
			backX += 1.5
			backX2 += 1.5
			bear=image3

		if keyInput[K_LEFT] and r1.right <= width:
			r1.right += 5
			backX -= 1.5
			backX2 -= 1.5
			bear=image1
	#Jumping
	if keyInput[K_SPACE] and onair == False:
		Isjumping=True
		bear=image2

		if keyInput[K_LEFT] and r1.left >= 0:
			bear=image4
		if keyInput[K_RIGHT] and r1.right <= width:
			bear=image2
	
	if Isjumping:
		if Jumpstep>= 0 :
			r1.top-= Jumpstep*10
			Jumpstep -= 1
		else:
			Isjumping = False
			Jumpstep = maxStep
			bear=image1

	#Draw
	screen.blit(bgImage, (backX, 0))
	screen.blit(bgImage, (backX2, 0))

	#Clone
	if r1.bottom == (h-(h*2)):
		r1.bottom = -200

	#Death
	if r1.y >= 650:
		r1.x = 0
		r1.y = 30

	#Tile Management
	if level == 2:
		tilel.clear()
		for i in range(5):
			polygon1=pygame.Rect(135,180,50,50)
			polygon1.x=polygon1.x + 135*i
			polygon1.y=polygon1.y + 30*i
			tilel.append(polygon1)
			r4.y = 210
		text = font.render('I see you are pretty good!',True,(255,255,255))
	if level == 3:
		tilel.clear()
		for i in range(5):
			polygon1=pygame.Rect(135,180,50,50)
			polygon1.x=polygon1.x + 135*i
			polygon1.y=polygon1.y + 30*i
			tilel.append(polygon1)
		for i in range(5):
			polygon1=pygame.Rect(710,300,50,50)
			polygon1.x+=135*i
			polygon1.y-=30*i
			tilel.append(polygon1)
		r4.x = 1225
		r4.y = 100
		text = font.render('Up and Down',True,(255,255,255))
	if level == 4:
		tilel.clear()
		for i in range(10):
			polygon1=pygame.Rect(135,500,50,50)
			polygon1.x += 135*i
			polygon1.y -= 30*i
			tilel.append(polygon1)
		text = font.render('Hmm...That 1st block is a trick.',True,(255,255,255))
	if level == 5:
		tilel.clear()
		text = font.render('The end',True,(255,255,255))

	#FPS
	CLOCK.tick(60)

	#Background
	screen.blit(bgImage, (0, 0))
	screen.blit(bear, r1)
	screen.blit(image6, r3)
	screen.blit(image5, r4)
	screen.blit(text,((width - text.get_width()) / 2, 10))
	if reverse == 1:
		screen.blit(image7, r5)

	for poly in tilel:
		screen.blit(image6,poly)
	pygame.display.update()
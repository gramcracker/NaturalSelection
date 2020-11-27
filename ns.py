#import libraries
import pygame
#randomized vairiables
import random
#math functions
import math
#brain class from other file
from brain import logic

import numpy as np

#start a pygame session
pygame.init()


#window parameters
displayWidth = 800
displayHeight = 800
windowClosed = False
black = (0,0,0) #will be background color
white = (255,255,255) #color of walls
backgroundColor = (40, 30, 57)
wallColor = (66, 65, 87)
timerLength = 5
timer = timerLength
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Natural Selection')
clock = pygame.time.Clock()
clockSpeed = 30
font = pygame.font.SysFont('Consolas', 30)

#load the data for the bots
redTriangle = pygame.image.load('redTriangle.png')
greenTriangle = pygame.image.load('greenTriangle.png')
numTeamMembers = 6
redTeam = pygame.sprite.Group()
greenTeam = pygame.sprite.Group()
walls = pygame.sprite.Group()
allSprites = pygame.sprite.Group()
greenTeamsTurn = False
Logic = logic()
Logic.logicSequence = np.load('logic.npy')
resetFlag = False
numberOfSteps = 50
collisionThreshold = 10



#this function determines who's turn it is and displays it with a timer
def turnHandler():
	team = ''

	global  resetFlag, redTeam, greenTeam, greenTeamsTurn, gameDisplay, timer, redLogic, greenLogic, numTeamMembers

	if(len(redTeam) == 0 ):
		if timer == 0 and resetFlag == True:

			timer = timerLength
			resetFlag = False
			eraseAllObjects()
			Logic.avgLogic(greenTeam)
			initAllObjects()
		else:
			gameDisplay.blit(font.render("Green wins!", True, (255,255,255)), (displayWidth/2, displayHeight/2))
			resetFlag = True

	elif(len(greenTeam) == 0 ):
		if timer == 0 and resetFlag == True:
			timer = timerLength
			resetFlag = False
			eraseAllObjects()
			Logic.avgLogic(redTeam)
			initAllObjects()
		else:
			gameDisplay.blit(font.render("Red wins!", True, (255,255,255)), (displayWidth/2, displayHeight/2))
			resetFlag = True




	#set the team string based on boolean value
	if greenTeamsTurn == True:
		team = 'green'
	else:
		team = 'red'

	#when timer hits 0 switch team
	if timer == 0:
		allSprites.remove(walls)
		walls.empty()
		generateWalls()

		if greenTeamsTurn:
			greenTeamsTurn = False
		else:
			greenTeamsTurn = True
		timer = timerLength


	#create string with the information
	text = (" {} // Turn: {}".format(timer, team))
	#display the text
	gameDisplay.blit(font.render(text, True, (255,255,255)), (32, 32))


#define wall class
class wall(pygame.sprite.Sprite): #inherits sprite class
	x = 0
	y = 0
	blockSize = displayHeight/25
	def __init__(self):
		#init parent
		pygame.sprite.Sprite.__init__(self)
		self.length = self.blockSize*random.randint(1,5)
		self.image = pygame.Surface([self.length, self.blockSize])
		self.rect = self.image.get_rect()
		self.image.fill(wallColor)
		self.rect.x = (random.randint(0, displayWidth) % displayWidth) - self.length
		self.rect.y = (random.randint(0, displayHeight) %displayHeight) - self.blockSize


#define bot class
class bot(pygame.sprite.Sprite): #inherites sprite class

	global Logic
	angle = 90
	speed = 1
	radius = 100
	score = 1
	changeX = 0
	changeY = 0
	sensoryArray = np.zeros(8)
	logic = Logic
	#enemy angle
    #enemy X distance
	#enemy Y distance
    #detect wall angle
    #detect wall X distance
	#detect wall Y distance
    #get turn boolean
	sensoryArray[7] = 1#bias

	def __init__(self, color):
		#init parent
		pygame.sprite.Sprite.__init__(self)
		self.color = color
		if self.color == 'green':
			self.png = greenTriangle
		else:
			self.png = redTriangle
		self.image = self.png
		self.rect = self.png.get_rect()
		self.rect.x = random.randint(0, displayWidth)
		self.rect.y = random.randint(0, displayHeight)
		
		self.angle = random.randint(0, 359)
		self.logic.mutateRandom()
		self.update()
		
	
	def getNextStep(self):

		global greenTeamsTurn

		if self.color == 'green':
			self.sensoryArray[6] = 1 if greenTeamsTurn else 0
		elif self.color == 'red':
			self.sensoryArray[6] = 1 if not greenTeamsTurn else 0

		return self.logic.step(self.sensoryArray) 

	#define rotate function
	def rotate(self, change):
		self.angle += change
		self.angle = self.angle % 360
		self.center = self.rect.center
		self.image = pygame.transform.rotozoom(self.png, self.angle, 1)
		#self.rect = self.image.get_rect(center = self.center)

	#if its this bots turn then it wont die otherwise it will die when tagged
	def detectEnemy(self, ):
		
		if self.color == 'green':
			enemiesNearby = pygame.sprite.spritecollide(self, redTeam, False, pygame.sprite.collide_circle)
			numEnemies = len(enemiesNearby)
			if numEnemies > 0:
				diffPosX = abs(enemiesNearby[0].rect.centerx-self.rect.centerx)
				diffPosY = abs(enemiesNearby[0].rect.centery-self.rect.centery)	
				for i in enemiesNearby:
					if (abs(diffPosY) <= collisionThreshold) and (abs(diffPosX) <= collisionThreshold):
						if greenTeamsTurn == False:
							self.kill()
							for i in greenTeam:
								i.logic.mutateRandom()
						else:
							self.score += 1
				self.sensoryArray[0] = 2*math.atan2(diffPosY, diffPosX)/math.pi
				self.sensoryArray[1] = (self.radius - diffPosX) - self.radius
				self.sensoryArray[2] = (self.radius - diffPosY) - self.radius
			else: self.sensoryArray[0:3] = 0


											
		elif self.color == 'red':
			enemiesNearby = pygame.sprite.spritecollide(self, greenTeam, False, pygame.sprite.collide_circle)
			numEnemies = len(enemiesNearby)
			if numEnemies > 0:
				diffPosX = abs(enemiesNearby[0].rect.centerx-self.rect.centerx)
				diffPosY = abs(enemiesNearby[0].rect.centery-self.rect.centery)	
				for i in enemiesNearby:
					if (abs(diffPosY) <= collisionThreshold) and (abs(diffPosX) <= collisionThreshold):
						if greenTeamsTurn == True:
							self.kill()
							for i in redTeam:
								i.logic.mutateRandom()
						else:
							self.score += 1
				self.sensoryArray[0] = 2*math.atan2(diffPosY, diffPosX)/math.pi
				self.sensoryArray[1] = (self.radius - diffPosX) - self.radius
				self.sensoryArray[2] = (self.radius - diffPosY) - self.radius
			else: self.sensoryArray[0:3] = 0

	#if the sprite bumps a wall the change in movement in that direction will be zero
	def detectWall(self, _wall):
		wallHitList = pygame.sprite.spritecollide(self, walls, False)
		walldetectList = pygame.sprite.spritecollide(self, walls, False, pygame.sprite.collide_circle)
		if len(walldetectList) > 0:

			diffPosX = walldetectList[0].rect.centerx - self.rect.centerx
			diffPosY = walldetectList[0].rect.centery - self.rect.centery
			angle = math.radians(math.atan2(diffPosY, diffPosX))

			# set sensory array
			self.sensoryArray[3] = diffPosX
			self.sensoryArray[4] = diffPosY
			self.sensoryArray[5] = angle

			if len(wallHitList) > 0:
				for w in wallHitList:
					if (self.changeX > 0 and (self.rect.center[0] < w.rect.left )) or (self.changeX < 0 and (self.rect.center[0] > w.rect.right)):
						self.changeX = 0

					if (self.changeY > 0 and (self.rect.center[1] < w.rect.top )) or (self.changeY < 0 and (self.rect.center[1] > w.rect.bottom)):
						self.changeY = 0

		else: self.sensoryArray[3:6] = 0

	#function for keeping sprites on screen
	def detectEdge(self):
		#if position + change in posistion is outside screen, then change in position = 0
			# if((self.rect.x+self.changeX) >= displayWidth-self.rect.width) or  ((self.rect.x+self.changeX) <= 0):
			# 		self.changeX = 0
			# if((self.rect.y+self.changeY) >= displayHeight-self.rect.height) or  ((self.rect.y+self.changeY) <= 0):
			# 	self.changeY = 0

		# comment above and uncomment this to have sprites roll over position on screen instead
		self.rect.x = self.rect.x%displayWidth
		self.rect.y = self.rect.y%displayHeight

					

	#update function (the main logic for a bot)
	def update(self):

		nextStep = self.getNextStep()

		self.speed = 3 + nextStep[0]  *10
		# self.rotate( np.tanh(nextStep[1])*self.speed )
		self.rotate( nextStep[1]*nextStep[2])
		self.changeX = -math.sin(math.radians(self.angle))*self.speed
		self.changeY = -math.cos(math.radians(self.angle))*self.speed
		for i in walls:
			self.detectWall(i)
		#keep sprites in play area
		self.detectEdge()
		#detect collisions with enemy
		self.detectEnemy()

		self.rect.x += self.changeX 
		self.rect.y += self.changeY

	#define function to add the sprite to the game surface
		# def display(self):
		# 	gameDisplay.blit(self.tempSprite, (self.centerX, self.centerY))

def generateWalls():
	#set random number of walls 3 <= numWalls <=15
	numWalls = random.randint(3,15)
	for i in range(numWalls):
		#create one of each member
		w = wall()
		walls.add(w)
		allSprites.add(w)

#Main algorithm of the simulator
def initAllObjects():
	#initialise objects
	for i in range(numTeamMembers):
		#create one of each member
		g = bot('green')
		r = bot('red')
		greenTeam.add(g)
		redTeam.add(r)
		allSprites.add(g)
		allSprites.add(r)

	
	generateWalls()

def eraseAllObjects():
	allSprites.empty()
	redTeam.empty()
	greenTeam.empty()
	walls.empty()

initAllObjects()

#set timer to trigger event once every 1000 milliseconds
pygame.time.set_timer(pygame.USEREVENT , 1000)

#Main game loop
while not windowClosed:
	#get events
	for event in pygame.event.get():
		if event.type == pygame.USEREVENT:
			timer -= 1
		if event.type == pygame.QUIT:
			windowClosed = True
		#type q to quit
		# type m to mutate
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				windowClosed = True
			if event.key == pygame.K_m:
				Logic.mutateRandom()
			if event.key == pygame.K_r:
				timer = timerLength
				eraseAllObjects()
				initAllObjects()


	#update sprites and draw display
	gameDisplay.fill(backgroundColor)
	allSprites.update()
	allSprites.draw(gameDisplay)
	turnHandler()
	pygame.display.flip()
	clock.tick(clockSpeed)

np.save('logic', Logic.logicSequence)
pygame.quit()
quit() 

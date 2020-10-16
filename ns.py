import pygame
import random
import math

#start a pygame session
pygame.init()

#window parameters
displayWidth = 800
displayHeight = 600
windowClosed = False
black = (0,0,0) #will be background color
timer = 15
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Natural Selection')

#load the images for the bots
redTriangle = pygame.image.load('redTriangle.png')
greenTriangle = pygame.image.load('greenTriangle.png')
numTeamMembers = 5
redTeam = []
greenTeam = []

clock = pygame.time.Clock()

#used to fix bad rotation function in pygame
def rotate(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


class wall:
	x = 0
	y = 0
	def __init__(self):
		self.x = random.randint(0, displayWidth)
		self.y = random.randint(0, displayHeight)
		self.angle = random.randint(0, 359)

	#def update():
	#def display():


class bot:

	x = 0
	y = 0
	angle = 90
	color = 'green'
	sprite = greenTriangle
	tempSprite = sprite
	moving = False


	def __init__(self, color):
		self.color = color
		if self.color == 'green':
			self.sprite = greenTriangle
		else:
			self.sprite = redTriangle
		self.x = random.randint(0, displayWidth)
		self.y = random.randint(0, displayHeight)
		self.changeInAngle = random.randint(0, 359)
		self.update()

	def update(self):
		#get input
			#object position in periferal
			#enemy in position periferal
			#attack/flee mode( switches every 15 seconds)

		#predict next move using DQN probably
		
		#TODO: fix sprites getting locked off screen
		# add some type of delay based on clock speed

		#temporary random movements
		self.moving = random.randint(0,1)
		self.changeInAngle = (self.angle+random.randint(0, 359))*self.moving
		self.tempSprite = rotate(self.sprite, self.changeInAngle%360)
		self.angle = (self.angle+self.changeInAngle)%360
		self.x = (self.x+math.cos(self.angle))*self.moving
		self.y = (self.y+math.sin(self.angle))*self.moving

		self.x = self.x%displayWidth-5

		self.y = self.y%displayHeight-5

		print(self.x, self.y)

	def display(self):
		gameDisplay.blit(self.tempSprite, (self.x,self.y))



for i in range(numTeamMembers):
	#create one of each member
	greenTeam.append(bot('green'))
	redTeam.append(bot('red'))

#Main game loop
while not windowClosed:
	#get events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			windowClosed = True

	gameDisplay.fill(black)




	for i in greenTeam:
		i.update()
		i.display()

	for i in redTeam:
		i.update()
		i.display()

	pygame.display.flip()
	clock.tick(6)

pygame.quit()
quit() 

# how a recurrent neural network works
# https://www.youtube.com/watch?v=UNmqTiOnRfg
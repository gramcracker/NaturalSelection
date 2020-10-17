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
	speed = 10
	#rect = sprite.get_rect(center = (15,15))

	def __init__(self, color):
		self.color = color
		if self.color == 'green':
			self.sprite = greenTriangle
		else:
			self.sprite = redTriangle
		self.x = random.randint(0, displayWidth)
		self.y = random.randint(0, displayHeight)
		self.angle = random.randint(0, 359)
		self.update()
		

	def rotate(self, change):
		self.angle += change
		self.angle = self.angle % 360
		self.tempSprite = pygame.transform.rotozoom(self.sprite, self.angle, 1)

	def update(self):
		#get input
			#object position in periferal
			#enemy in position periferal
			#attack/flee mode( switches every 15 seconds)

		#predict next move using DQN probably
		
		#TODO: fix sprites getting locked off screen
		# add some type of delay based on clock speed

		#temporary random movements
		self.speed = random.randint(1,10)
		self.rotate( random.randint(-1*self.speed, self.speed))
		self.x -= math.sin(math.radians(self.angle))*self.speed
		self.y -= math.cos(math.radians(self.angle))*self.speed

		self.x = self.x%displayWidth
		self.y = self.y%displayHeight



	def display(self):
		gameDisplay.blit(self.tempSprite, (self.x - self.tempSprite.get_width() / 2 , self.y - self.tempSprite.get_height() / 2))



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
		#type q to quit
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				windowClosed = True
	gameDisplay.fill(black)



	pygame.time.wait(100)
	for i in greenTeam:
		i.update()
		i.display()

	for i in redTeam:
		i.update()
		i.display()

	pygame.display.flip()
	clock.tick(60)

pygame.quit()
quit() 

# how a recurrent neural network works
# https://www.youtube.com/watch?v=UNmqTiOnRfg
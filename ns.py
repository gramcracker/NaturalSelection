import pygame
import random

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
	angle = 0
	color = 'green'
	sprite = greenTriangle


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

	def update(self):
		#get input
			#object position in periferal
			#enemy in position periferal
			#attack/flee mode( switches every 15 seconds)

		#predict next move using DQN probably

		#update position
			#position += position node
		#update angle
			#angle += angle node
		#
		self.sprite = pygame.transform.rotate(self.sprite, self.angle)

	def display(self):
		gameDisplay.blit(self.sprite, (self.x,self.y))


#Main game loop
while not windowClosed:
	#get events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			windowClosed = True

	gameDisplay.fill(black)


	for i in range(numTeamMembers):
		#create one of each member
		greenTeam.append(bot('green'))
		greenTeam[i].display()
		redTeam.append(bot('red'))
		redTeam[i].display()



	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit() 

# how a recurrent neural network works
# https://www.youtube.com/watch?v=UNmqTiOnRfg
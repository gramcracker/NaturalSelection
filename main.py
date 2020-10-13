import pygame


pygame.init()


display_width = 800
display_height = 600
windowClosed = False
timer = 15


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Purge')



black = (0,0,0)
white = (255,255,255)
red = (255, 80, 80)
blue = (51, 133, 255)

clock = pygame.time.Clock()


class wall:
	x = 0
	y = 0
	def _init_(self):
		self.x = random.randint(0, display_width)
		self.y = random.randint(0, display_height)
		self.angle = random.randint(0, 359)

	def update():


	def display():

class organism:
	x = 0
	y = 0
	color = blue
	def _init_(self, color):
		self.color = color
		self.x = random.randint(0, display_width)
		self.y = random.randint(0, display_height)
		self.angle = random.randint(0, 359)

	def update():


	def display():



while not windowClosed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True

    gameDisplay.fill(black)
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit() 

# how a recurrent neural network works
# https://www.youtube.com/watch?v=UNmqTiOnRfg
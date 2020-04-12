# Modules

import sys, pygame
from pygame.locals import *

# Constants

WIDTH = 640
HEIGHT = 480

# Classes

class Ball(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image('images/ball.png')
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH / 2
		self.rect.centery = HEIGHT / 2
		self.speed = [0.5, -0.5]

# Functions

def load_image(filename, transparent = False):
	try: image = pygame.image.load(filename)
	except (pygame.error, message):
		raise (SystemExit, message)

	image = image.convert()

	if transparent:
		color = image.get_at((0, 0))
		image.set_colorkey(color, RLEACCEL)
	return image

def main():
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Pong game")
	
	bg = load_image('images/pong_bg.png')
	screen.blit(bg, (0, 0))

	# Draw the ball
	ball = Ball()
	screen.blit(ball.image, ball.rect)
	
	pygame.display.flip()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit(0)

if __name__ == '__main__':
	pygame.init()
	main()
	

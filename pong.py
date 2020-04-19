# Modules

import sys, pygame
from pygame.locals import *

# Constants

WIDTH = 640
HEIGHT = 480

# Classes

class Pala(pygame.sprite.Sprite):
	def __init__(self, x):
		self.image = load_image("images/pala.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = HEIGHT / 2
		self.speed = 0.5
	def move(self, time, keys):
		if self.rect.top >= 0:
			if keys[K_UP]:
				self.rect.centery -= self.speed * time
		if self.rect.bottom <= HEIGHT:
			if keys[K_DOWN]:
				self.rect.centery += self.speed * time

class Ball(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image('images/ball.png', True)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH / 2
		self.rect.centery = HEIGHT / 2
		self.speed = [0.5, -0.5]

	def update(self, time):
		self.rect.centerx += self.speed[0] * time
		self.rect.centery += self.speed[1] * time
		if self.rect.left <= 0 or self.rect.right >= WIDTH:
			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0] * time
		if self.rect.bottom >= HEIGHT or self.rect.top <= 0:
			self.speed[1] = -self.speed[1]
			self.rect.centery += self.speed[1] * time

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

	# Draw the ball
	ball = Ball()
	pala_player = Pala(30)

	clock = pygame.time.Clock()

	while True:
		# Exit the program
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit(0)

		
		time = clock.tick(60)
		keys = pygame.key.get_pressed()
		ball.update(time)
		pala_player.move(time, keys)

		screen.blit(bg, (0, 0))
		screen.blit(ball.image, ball.rect)
		screen.blit(pala_player.image, pala_player.rect)
		pygame.display.flip()

if __name__ == '__main__':
	pygame.init()
	main()
	

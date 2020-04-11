# -*- coding: utf-8 -*-

# Modules

import sys, pygame
from pygame.locals import *

# Constants

WIDTH = 640
HEIGHT = 480

# Classes

# Functions 

def load_image(filename, transparent=False):
	try:image = pygame.image.load(filename)
	except (pygame.error, message):
		raise (SystemExit, message)

	image = image.convert()
	
	if transparent:
		color = image.get_at((0, 0))
		image.set_colorkey(color, RLEACCEL)
	return image



def main():
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("TEST PYGAME")

	background_image = load_image('images/background.jpg')

	screen.blit(background_image, (0, 0))
	pygame.display.flip()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit(0)


if __name__ == '__main__':
	pygame.init()
	main()

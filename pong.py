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
		self.speed = 0.4

	def move(self, time, keys):
		if self.rect.top >= 0:
			if keys[K_UP]:
				self.rect.centery -= self.speed * time
		if self.rect.bottom <= HEIGHT:
			if keys[K_DOWN]:
				self.rect.centery += self.speed * time

	def ia(self, time, ball):
		if ball.speed[0] and ball.rect.centerx >= WIDTH / 2:
			if ball.rect.centery > self.rect.centery:
					self.rect.centery += time * self.speed
			if  ball.rect.centery < self.rect.centery:
					self.rect.centery -= time * self.speed


class Ball(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image('images/ball.png', True)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH / 2
		self.rect.centery = HEIGHT / 2
		self.speed = [0.5, -0.5]

	def update(self, time, pala_player, pala_cpu, scoreboard):
		self.rect.centerx += self.speed[0] * time
		self.rect.centery += self.speed[1] * time

		if self.rect.left <= 0:
			scoreboard[1] += 1
		if self.rect.right >= WIDTH:
			scoreboard[0] += 1

		if self.rect.left <= 0 or self.rect.right >= WIDTH:
			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0] * time
		if self.rect.bottom >= HEIGHT or self.rect.top <= 0:
			self.speed[1] = -self.speed[1]
			self.rect.centery += self.speed[1] * time

		if pygame.sprite.collide_rect(self, pala_player):
				self.speed[0] = -self.speed[0]
				self.rect.centerx += self.speed[0] * time

		if pygame.sprite.collide_rect(self, pala_cpu):
				self.speed[0] = -self.speed[0]
				self.rect.centerx += self.speed[0] * time

		return scoreboard
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

def text(text, posx, posy, color=(255, 255, 255)):
	fuente = pygame.font.Font('fonts/DroidSans.ttf', 25)
	salida = pygame.font.Font.render(fuente, text, 1, color)
	salida_rect = salida.get_rect()
	salida_rect.centerx = posx
	salida_rect.centery = posy
	return salida, salida_rect
	

def main():
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Pong game")
	
	bg = load_image('images/pong_bg.png')

	# Draw the ball
	ball = Ball()
	pala_player = Pala(30)
	pala_cpu = Pala(WIDTH -30)
	clock = pygame.time.Clock()

	# Define the scoreboard
	scoreboard = [0, 0]

	while True:
		# Exit the program
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit(0)

		
		time = clock.tick(60)
		keys = pygame.key.get_pressed()
		scoreboard = ball.update(time, pala_player, pala_cpu, scoreboard)
		pala_player.move(time, keys)
		pala_cpu.ia(time, ball)

		p_player, p_player_rect = text(str(scoreboard[0]), WIDTH/4, 40)
		p_cpu, p_cpu_rect = text(str(scoreboard[1]), WIDTH-WIDTH/4, 40)

		screen.blit(bg, (0, 0))
		screen.blit(p_player, p_player_rect)
		screen.blit(p_cpu, p_cpu_rect)
		screen.blit(ball.image, ball.rect)
		screen.blit(pala_player.image, pala_player.rect)
		screen.blit(pala_cpu.image, pala_cpu.rect)
		pygame.display.flip()

if __name__ == '__main__':
	pygame.init()
	main()
	

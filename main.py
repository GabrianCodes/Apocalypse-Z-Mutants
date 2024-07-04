import pygame
from settings import *
import sys
from character import Character



class Game:
	def __init__(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption('Survive')
		self.clock = pygame.time.Clock()

		#groups
		self.all_sprites = pygame.sprite.Group()

		self.setup()

	def setup(self):
		Character((200,200),self.all_sprites,PATHS['character'],None)


	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			delta_time = self.clock.tick()/1000

			#update
			self.all_sprites.update(delta_time)

			#draw

			self.display_surface.fill('black')
			self.all_sprites.draw(self.display_surface)

			
			pygame.display.update()
if __name__ == '__main__':
	game = Game()
	game.run()
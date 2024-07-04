import pygame
from pygame.math import Vector2 as vector2
from settings import *
import sys
from character import Character


class AllSprites(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.offset = vector2()
		self.display_surface = pygame.display.get_surface()
		self.background = pygame.image.load('./assets/environment/background/level1.png').convert()

	def customize_draw(self,character):
		
		self.offset.x = character.rect.centerx - WINDOW_WIDTH / 2
		self.offset.y = character.rect.centery - WINDOW_HEIGHT / 2

		self.display_surface.blit(self.background,-self.offset)

		for sprite in self.sprites():
			offset_rect = sprite.image.get_rect(center = sprite.rect.center)
			offset_rect.center -= self.offset
			self.display_surface.blit(sprite.image,offset_rect)

class Game:
	def __init__(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption('Survive')
		self.clock = pygame.time.Clock()

		#groups
		self.all_sprites = AllSprites()
		self.setup()

	def setup(self):
		self.character = Character((200,200),self.all_sprites,PATHS['character'],None)


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
			self.all_sprites.customize_draw(self.character)

			
			pygame.display.update()
if __name__ == '__main__':
	game = Game()
	game.run()
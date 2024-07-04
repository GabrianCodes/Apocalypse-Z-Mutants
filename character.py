import pygame
from pygame.math import Vector2 as vector2
from os import walk
from settings import *


class Character(pygame.sprite.Sprite):
	def __init__(self,position,groups,path,collision_sprites):
		super().__init__(groups)
		self.import_assets(path)
		self.image = pygame.Surface((100,100))
		self.image.fill('red')
		self.rect = self.image.get_rect(center = position)

		#movement
		self.position = vector2(self.rect.center)
		self.direction = vector2()
		self.speed = 200

		#collisions
		self.hitbox = self.rect
		self.collision_sprites = collision_sprites

	def import_assets(self,path):
		self.animations = {}

		for index, folder in enumerate(walk(path)):
			if index == 0:
				for name in folder[1]:
					self.animations[name] = []
		print(self.animations)


	def input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_d]:
			self.direction.x = 1
		elif keys[pygame.K_a]:
			self.direction.x = -1
		else:
			self.direction.x = 0

		if keys[pygame.K_w]:
			self.direction.y = -1
		elif keys[pygame.K_s]:
			self.direction.y = 1
		else:
			self.direction.y = 0

	def move(self,delta_time):


		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()
		self.position += self.direction *  self.speed * delta_time
		self.hitbox.center = (round(self.position.x), round(self.position.y))
		self.rect.center = self.hitbox.center

	def update(self,delta_time):
		self.input()
		self.move(delta_time)





	



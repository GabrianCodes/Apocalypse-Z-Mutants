import pygame
from pygame.math import Vector2 as vector2
from os import walk
from settings import *
import math


class Character(pygame.sprite.Sprite):
	def __init__(self,position,groups,path,collision_sprites):
		super().__init__(groups)
		self.import_assets(path)
		self.frame_index = 0
		self.status = 'idle'
		self.image = self.animations[self.status][self.frame_index]
		self.rect = self.image.get_rect(center = position)

		#movement
		self.position = vector2(self.rect.center)
		self.direction = vector2()
		self.speed = 200

		#collisions
		self.hitbox = self.rect
		self.collision_sprites = collision_sprites

		#attacking
		self.melee = False
		self.ranged1 = False
		self.ranged2 = False 

	def get_status(self):
		if self.ranged1:
			self.status = 'ranged'
		if self.melee:
			self.status = 'melee'

	def import_assets(self,path):
		self.animations = {}

		for index, folder in enumerate(walk(path)):
			if index == 0:
				for name in folder[1]:
					self.animations[name] = []
			else:
				for file_name in sorted(folder[2]):
					path = folder[0].replace('\\','/') + '/' + file_name
					surface = pygame.image.load(path).convert_alpha()
					key = folder[0].split('\\')[1]
					self.animations[key].append(surface)


	def input(self):
		if pygame.mouse.get_pressed()[0]:
			self.ranged1 = True
		keys = pygame.key.get_pressed()

		if keys[pygame.K_v]:
			self.melee = True


		if keys[pygame.K_d]:
			self.direction.x = 1
			self.status = 'walk'
		elif keys[pygame.K_a]:
			self.direction.x = -1
			self.status = 'walk'
		elif keys[pygame.K_w]:
			self.direction.y = -1
			self.status = 'walk'
		elif keys[pygame.K_s]:
			self.direction.y = 1
			self.status = 'walk'
		else:
			self.direction.x = 0
			self.direction.y = 0
			self.status = 'idle'


	def rotate(self):
	    mouse_x, mouse_y = pygame.mouse.get_pos()
	    rel_x, rel_y = mouse_x - self.position.x, mouse_y - self.position.y
	    angle = (180 / math.pi) * math.atan2(-rel_y, rel_x) + 90
	    self.image = pygame.transform.rotozoom(self.image, int(angle),0.85)
	    self.rect = self.image.get_rect(center=self.position)

	def move(self,delta_time):

		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()
		self.position += self.direction *  self.speed * delta_time
		self.hitbox.center = (round(self.position.x), round(self.position.y))
		self.rect.center = self.hitbox.center

	def animate(self,delta_time):
		current_animation = self.animations[self.status]
		self.frame_index += 10 * delta_time
		if self.frame_index >= len(current_animation):
			self.frame_index = 0
			if self.ranged1 or self.ranged2 or self.melee:
				self.ranged1 = False
				self.ranged2 =  False
				self.melee = False
		self.image = current_animation[int(self.frame_index)]

	def update(self,delta_time):
		self.input()
		self.get_status()
		self.move(delta_time)

		self.animate(delta_time)
		self.rotate()
		
		




	



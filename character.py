import pygame
from pygame.math import Vector2 as vector2
from settings import *
import math
from entities import Entity


class Character(Entity):
	def __init__(self,position,groups,path,collision_sprites,create_bullet):
		super().__init__(position,groups,path,collision_sprites)
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

		self.create_bullet = create_bullet
		self.bullet_shot = False

	def get_status(self):
		if self.ranged1:
			self.status = 'ranged'
		if self.melee:
			self.status = 'melee'




	def input(self):
		if pygame.mouse.get_pressed()[0]:
			self.ranged1 = True
			self.frame_index = 0
			self.bullet_shot = False
		keys = pygame.key.get_pressed()

		if keys[pygame.K_v]:
			self.melee = True


		
		if keys[pygame.K_d]:
			self.direction.x = 1
			self.status = 'walk'
		elif keys[pygame.K_a]:
			self.direction.x = -1
			self.status = 'walk'
		if not any(pygame.key.get_pressed()):
			self.direction.x = 0
			self.status = 'idle'
		
		if keys[pygame.K_w]:
			self.direction.y = -1
			self.status = 'walk'
		elif keys[pygame.K_s]:
			self.direction.y = 1
			self.status = 'walk'
		if not any(pygame.key.get_pressed()):
			self.direction.y = 0
			self.status = 'idle'







	def rotate(self):
	    mouse_x, mouse_y = pygame.mouse.get_pos()
	    rel_x, rel_y = mouse_x - (WINDOW_WIDTH/2), mouse_y - (WINDOW_HEIGHT/2)
	    angle = (180 / math.pi) * math.atan2(-rel_y, rel_x) + 90
	    self.image = pygame.transform.rotozoom(self.image, int(angle),0.5)
	    self.rect = self.image.get_rect(center=self.position)


	def animate(self,delta_time):
		current_animation = self.animations[self.status]
		self.frame_index += 10 * delta_time


		if int(self.frame_index) == 1 and self.ranged1 and not self.bullet_shot:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			rel_x, rel_y = mouse_x - (WINDOW_WIDTH/2), mouse_y - (WINDOW_HEIGHT/2)
			angle = math.atan2(rel_y, rel_x)
			
			x,y = math.cos(angle), math.sin(angle)
			self.create_bullet(self.rect.center,vector2(x,y))
			self.bullet_shot = True

		if self.frame_index >= len(current_animation):
			self.frame_index = 0
			if self.ranged1 or self.ranged2 or self.melee:
				self.ranged1 = False
				self.ranged2 =  False
				self.melee = False
		self.image = current_animation[int(self.frame_index)]

	def collision(self,direction):
		for sprite in self.collision_sprites.sprites():
			if sprite.hitbox.colliderect(self.hitbox):
				if direction == 'horizontal':
					if self.direction.x > 0:
						self.hitbox.right = sprite.hitbox.left
						self.rect.centerx = self.hitbox.centerx
						self.position.x = self.hitbox.centerx
					if self.direction.x < 0:
						self.hitbox.left = sprite.hitbox.right
						self.rect.centerx = self.hitbox.centerx
						self.position.x = self.hitbox.centerx
				else:
					if self.direction.y > 0:
						self.hitbox.bottom = sprite.hitbox.top
						self.rect.centery = self.hitbox.centery
						self.position.y = self.hitbox.centery
					if self.direction.y < 0:
						self.hitbox.top = sprite.hitbox.bottom
						self.rect.centery = self.hitbox.centery
						self.position.y = self.hitbox.centery



	def update(self,delta_time):
		self.input()
		self.get_status()
		self.move(delta_time)

		self.animate(delta_time)
		self.rotate()
		
		




	



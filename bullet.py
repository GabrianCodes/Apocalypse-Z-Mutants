
import pygame
import math
from settings import *

class Bullet(pygame.sprite.Sprite):
	def __init__(self,position,direction,surface,groups):
		super().__init__(groups)

		mouse_x, mouse_y = pygame.mouse.get_pos()
		rel_x, rel_y = mouse_x - (WINDOW_WIDTH/2), mouse_y - (WINDOW_HEIGHT/2)
		angle = (180 / math.pi) * math.atan2(-rel_y, rel_x) + -90
		self.image = pygame.transform.rotozoom(surface,angle,1)
		self.rect = self.image.get_rect(center = position)
		self.hitbox = self.rect
		self.position = pygame.math.Vector2(self.rect.center)
		self.direction = direction
		self.speed = 900

	def move(self,delta_time):
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()
		self.position.x += self.direction.x *  self.speed * delta_time
		self.hitbox.centerx = round(self.position.x)
		self.rect.centerx = self.hitbox.centerx

		self.position.y += self.direction.y *  self.speed * delta_time
		self.hitbox.centery = round(self.position.y)
		self.rect.centery = self.hitbox.centery

	def update(self,delta_time):
		self.position += self.direction * self.speed * delta_time
		self.rect.center = (round(self.position.x),round(self.position.y))
		self.move(delta_time)
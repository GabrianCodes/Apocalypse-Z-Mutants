import pygame

class Sprite(pygame.sprite.Sprite):
	def __init__(self,position,surface,groups):
		super().__init__(groups)
		self.image = surface
		self.rect = self.image.get_rect(topleft = position)
		self.hitbox = self.rect

class Bullet(pygame.sprite.Sprite):
	def __init__(self,position,direction,surface,groups):
		super().__init__(groups)
		self.image = surface
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


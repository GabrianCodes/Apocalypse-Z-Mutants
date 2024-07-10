import pygame
import math
from settings import *


class Sprite(pygame.sprite.Sprite):
	def __init__(self,position,surface,groups):
		super().__init__(groups)
		self.image = surface
		self.rect = self.image.get_rect(topleft = position)
		self.hitbox = self.rect
		






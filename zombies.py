import pygame
from pygame.math import Vector2 as vector2
from settings import *
import math
from entities import Entity

class Zombieboss(Entity):
	def __init__(self,position,groups,path,collision_sprites):
		super().__init__(position,groups,path,collision_sprites)

class Zombie1(Entity):
	def __init__(self,position,groups,path,collision_sprites):
		super().__init__(position,groups,path,collision_sprites)

class Zombie2(Entity):
	def __init__(self,position,groups,path,collision_sprites):
		super().__init__(position,groups,path,collision_sprites)

class Zombie3(Entity):
	def __init__(self,position,groups,path,collision_sprites):
		super().__init__(position,groups,path,collision_sprites)
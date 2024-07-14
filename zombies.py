import pygame
from pygame.math import Vector2 as vector2
from settings import *
import math
from entities import Entity

class Zombie(Entity):
    def __init__(self, position, groups, path, collision_sprites, player):
        super().__init__(position, groups, path, collision_sprites)
        self.player = player  # Reference to the player character
        self.speed = 100  # Adjust speed as needed

    def update(self, delta_time):
        # Calculate the direction vector towards the player
        player_position = vector2(self.player.rect.center)
        direction = player_position - self.position

        if direction.magnitude() != 0:
            direction = direction.normalize()

        self.direction = direction
        super().update(delta_time)  # Call the update method from Entity

class Zombieboss(Zombie):
    def __init__(self, position, groups, path, collision_sprites, player):
        super().__init__(position, groups, path, collision_sprites, player)

class Zombie1(Zombieboss):
    def __init__(self, position, groups, path, collision_sprites, player):
        super().__init__(position, groups, path, collision_sprites, player)

class Zombie2(Zombieboss):
    def __init__(self, position, groups, path, collision_sprites, player):
        super().__init__(position, groups, path, collision_sprites, player)

class Zombie3(Zombieboss):
    def __init__(self, position, groups, path, collision_sprites, player):
        super().__init__(position, groups, path, collision_sprites, player)
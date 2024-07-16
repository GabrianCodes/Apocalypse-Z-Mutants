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

        # Resize zombie sprite
        for key in self.animations:
            self.animations[key] = [pygame.transform.scale(surface, (int(surface.get_width() * 0.5), int(surface.get_height() * 0.5))) for surface in self.animations[key]]

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=position)

    def update(self, delta_time):
       
        player_position = vector2(self.player.rect.center)
        direction = player_position - self.position

        if direction.magnitude() != 0:
            direction = direction.normalize()
            self.status = 'walk'  

        self.direction = direction
        super().update(delta_time)  # Call the update method from Entity

        # Rotate zombie to face the player
        self.rotate(player_position)

class Zombieboss(Zombie):
    def __init__(self, position, groups, path, collision_sprites, player):
        super().__init__(position, groups, path, collision_sprites, player)

class Zombie1(Zombie):
    def __init__(self, position, groups, path, collision_sprites, player):
        super().__init__(position, groups, path, collision_sprites, player)

class Zombie2(Zombie):
    def __init__(self, position, groups, path, collision_sprites, player):
        super().__init__(position, groups, path, collision_sprites, player)

class Zombie3(Zombie):
    def __init__(self, position, groups, path, collision_sprites, player):
        super().__init__(position, groups, path, collision_sprites, player)
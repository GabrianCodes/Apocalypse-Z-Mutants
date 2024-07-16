import pygame
from os import walk
from pygame.math import Vector2 as vector2
import math

class Entity(pygame.sprite.Sprite):
    def __init__(self, position, groups, path, collision_sprites):
        super().__init__(groups)
        self.import_assets(path)
        self.frame_index = 0
        self.status = 'idle'

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=position)

        # movement
        self.position = vector2(self.rect.center)
        self.direction = vector2()
        self.speed = 200

        # collisions
        self.hitbox = self.rect
        self.collision_sprites = collision_sprites

        # attacking
        self.melee = False
        self.ranged1 = False
        self.ranged2 = False

    def import_assets(self, path):
        self.animations = {}

        for index, folder in enumerate(walk(path)):
            if index == 0:
                for name in folder[1]:
                    self.animations[name] = []
            else:
                for file_name in sorted(folder[2]):
                    path = folder[0].replace('\\', '/') + '/' + file_name
                    surface = pygame.image.load(path).convert_alpha()
                    key = folder[0].split('\\')[1]
                    self.animations[key].append(surface)

    def move(self, delta_time):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.position.x += self.direction.x * self.speed * delta_time
        self.hitbox.centerx = round(self.position.x)
        self.rect.centerx = self.hitbox.centerx
        self.collision('horizontal')

        self.position.y += self.direction.y * self.speed * delta_time
        self.hitbox.centery = round(self.position.y)
        self.rect.centery = self.hitbox.centery
        self.collision('vertical')

    def collision(self, direction):
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

    def animate(self, delta_time):
        current_animation = self.animations[self.status]
        self.frame_index += 10 * delta_time
        if self.frame_index >= len(current_animation):
            self.frame_index = 0
        self.image = current_animation[int(self.frame_index)]

    def rotate(self, target_position):
        direction = target_position - self.position
        angle = math.degrees(math.atan2(-direction.y, direction.x)) + 90
        self.image = pygame.transform.rotozoom(self.image, angle, 0.5)
        self.rect = self.image.get_rect(center=self.position)

    def update(self, delta_time):
        self.move(delta_time)
        self.animate(delta_time)
import pygame
from pygame.math import Vector2 as vector2
from settings import *
import sys
from character import Character
from pytmx.util_pygame import load_pygame
from sprite import Sprite
from bullet import Bullet
from zombies import Zombieboss, Zombie1, Zombie2, Zombie3


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = vector2()
        self.display_surface = pygame.display.get_surface()
        self.background = pygame.image.load('./assets/environment/background/level1.png').convert()

    def customize_draw(self, character):
        self.offset.x = character.rect.centerx - WINDOW_WIDTH / 2
        self.offset.y = character.rect.centery - WINDOW_HEIGHT / 2
        self.display_surface.blit(self.background, -self.offset)
        for sprite in self.sprites():
            offset_rect = sprite.image.get_rect(center=sprite.rect.center)
            offset_rect.center -= self.offset
            self.display_surface.blit(sprite.image, offset_rect)


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Survive')
        self.clock = pygame.time.Clock()
        self.bullet_surface = pygame.image.load('./assets/images/projectiles/bullet.png').convert_alpha()
        self.paused = False  # Track pause state

        # Groups
        self.all_sprites = AllSprites()
        self.obstacles = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self.setup()

    def create_bullet(self, position, direction):
        Bullet(position, direction, self.bullet_surface, [self.all_sprites, self.bullets])

    def setup(self):
        tmx_map = load_pygame('./levels/level1/level1.tmx')
        for obj in tmx_map.get_layer_by_name('Objects'):
            Sprite((obj.x, obj.y), obj.image, [self.all_sprites, self.obstacles])

        for obj in tmx_map.get_layer_by_name('Entities'):
            if obj.name == 'Character':
                self.character = Character(
                    position=(obj.x, obj.y),
                    groups=self.all_sprites,
                    path=PATHS['character'],
                    collision_sprites=self.obstacles,
                    create_bullet=self.create_bullet
                )

            if obj.name == 'zombieboss':
                Zombieboss(position=(obj.x, obj.y),
                           groups=self.all_sprites,
                           path=PATHS['zombieboss'],
                           collision_sprites=self.obstacles,
                           player=self.character)
            if obj.name == 'zombie1':
                Zombie1(position=(obj.x, obj.y),
                        groups=self.all_sprites,
                        path=PATHS['zombie1'],
                        collision_sprites=self.obstacles,
                        player=self.character)
            if obj.name == 'zombie2':
                Zombie2(position=(obj.x, obj.y),
                        groups=self.all_sprites,
                        path=PATHS['zombie2'],
                        collision_sprites=self.obstacles,
                        player=self.character)
            if obj.name == 'zombie3':
                Zombie3(position=(obj.x, obj.y),
                        groups=self.all_sprites,
                        path=PATHS['zombie3'],
                        collision_sprites=self.obstacles,
                        player=self.character)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:  # Press P to pause/unpause
                        self.paused = not self.paused

            delta_time = self.clock.tick() / 1000

            if not self.paused:
                # Update
                self.all_sprites.update(delta_time)
            
            # Draw
            self.display_surface.fill('black')
            self.all_sprites.customize_draw(self.character)

            if self.paused:
                self.display_pause_menu()

            pygame.display.update()

    def display_pause_menu(self):
        font = pygame.font.Font(None, 74)
        resume_text = font.render('Resume (R)', True, 'white')
        quit_text = font.render('Quit (Q)', True, 'white')

        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(128)  # Set transparency level
        overlay.fill((0, 0, 0))  # Set overlay color

        self.display_surface.blit(overlay, (0, 0))
        self.display_surface.blit(resume_text, (WINDOW_WIDTH // 2 - resume_text.get_width() // 2, WINDOW_HEIGHT // 2 - 100))
        self.display_surface.blit(quit_text, (WINDOW_WIDTH // 2 - quit_text.get_width() // 2, WINDOW_HEIGHT // 2 + 50))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.paused = False
        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    game = Game()
    game.run()
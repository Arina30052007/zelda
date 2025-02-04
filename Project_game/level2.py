import pygame

from Project_game.settings import WORLD_MAP2
from player2 import Player2
from debug import debug
from others import Rock2, Princess
from enemy import Enemy

class Setup2:
    def __init__(self):
        self.world = WORLD_MAP2
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites =  CameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()
        self.m = pygame.sprite.Group()
        self.d = pygame.sprite.Group()
        self.place()

    def place(self):
        for r_index, row in enumerate(self.world):
            for c_index, column in enumerate(row):
                x = c_index * 60
                y = r_index * 60
                if column == 'x':
                    Rock2((x, y), [self.visible_sprites, self.obstacles_sprites])
                if column == 'p':
                    self.player = Player2((x, y), [self.visible_sprites], self.obstacles_sprites, self.m, self.d)
                if column == 'm':
                    self.enemy = Enemy((x, y), [self.m, self.visible_sprites], self.m, self.obstacles_sprites)
                if column == 'd':
                    self.enemy = Princess((x, y), [self.visible_sprites, self.d], self.d)


    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
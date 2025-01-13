import pygame

from Project_game.settings import WORLD_MAP
from rock import Rock
from player import Player
from debug import debug

class Setup:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites =  CameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()
        self.place()

    def place(self):
        for r_index, row in enumerate(WORLD_MAP):
            for c_index, column in enumerate(row):
                x = c_index * 50
                y = r_index * 50
                if column == 'x':
                    Rock((x, y), [self.visible_sprites, self.obstacles_sprites])
                if column == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacles_sprites)


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
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

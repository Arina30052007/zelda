import pygame

from Project_game.settings import WORLD_MAP
from rock import Rock
from player import Player
from debug import debug

class Setup:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites =  pygame.sprite.Group()
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
                    self.player = Player((x, y), [self.visible_sprites])


    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.movement)
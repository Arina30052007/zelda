import pygame
from settings import *

class Sword(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        print(pos)
        colorkey = -1
        self.image = pygame.image.load('data\\mech-Photoroom.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)



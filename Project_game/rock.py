import pygame
from settings import *

class Rock(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        colorkey = -1
        self.image = pygame.image.load('data\\rock-Photoroom.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.image.convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
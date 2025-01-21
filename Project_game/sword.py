import pygame
from pygame.examples.go_over_there import running
import sys
import os

from settings import *


class Sword(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        colorkey = -1
        self.image = pygame.image.load('data\\mech-Photoroom.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)


class Stars(pygame.sprite.Sprite):

    image_str = 'data\\star-Photoroom.png'
    image_1 = "data\\1.png"
    def __init__(self, pos, groups, z):
        super().__init__(groups)
        self.z = z
        self.image = pygame.image.load(Stars.image_str)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_1

class Grass(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('data\\grass.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.image.convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)



#

import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('data\\player1,1_processed.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.image.convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.movement = pygame.math.Vector2()
        self.v = 5

    def keyboard(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.movement.y = -1
        elif keys[pygame.K_DOWN]:
            self.movement.y = 1
        else:
            self.movement.y = 0
        if keys[pygame.K_RIGHT]:
            self.movement.x = 1
        elif keys[pygame.K_LEFT]:
            self.movement.x = -1
        else:
            self.movement.x = 0

    def go(self, v):
        self.rect.center += self.movement * v


    def update(self):
        self.keyboard()
        self.go(self.v)

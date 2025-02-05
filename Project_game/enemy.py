import pygame
from pygame import USEREVENT

from player2 import Player2

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups, m, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('data\\enemy-Photoroom.png')
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.image.convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -26)
        self.pos = pos
        self.v = 7
        self.m = m
        self.coin = 0
        self.obstacle_sprites = obstacle_sprites
        self.direction = 0
        self.movement = pygame.math.Vector2()

    def go(self):
        self.movement.x = 0.00000000000001
        if self.movement.magnitude() != 0:
            self.movement = self.movement.normalize()
        if self.rect.right >= 1050:
            self.direction = -1
        elif self.rect.left <= 0:
            self.direction = 1
        self.hitbox.x += self.direction * self.movement.x * self.v


        self.rect.center = self.hitbox.center

    def collision(self, movement):
        if movement == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.movement.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.movement.x < 0:
                        self.hitbox.left = sprite.hitbox.right
        if movement == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.movement.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.movement.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom




    def update(self):
        self.go()


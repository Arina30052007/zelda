import pygame
from settings import *
from level import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, visible_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('data\\player1,1_processed.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.image.convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -26)
        self.pos = pos
        self.movement = pygame.math.Vector2()
        self.v = 5
        self.obstacle_sprites = obstacle_sprites



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
        if self.movement.magnitude() != 0:
            self.movement = self.movement.normalize()

        self.hitbox.x += self.movement.x * v
        self.collision('horizontal')
        self.hitbox.y += self.movement.y * v
        self.collision('vertical')
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
        self.keyboard()
        self.go(self.v)

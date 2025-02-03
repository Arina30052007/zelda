import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups, m, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('data\\enemy-Photoroom.png')
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.image.convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -26)
        self.pos = pos
        self.movement = pygame.math.Vector2()
        self.v = 5
        self.m = m
        self.coin = 0
        self.obstacle_sprites = obstacle_sprites

    def go(self, v):
        for e in self.m:
            self.movement.x += 1
            self.movement.y += 1
            if self.movement.magnitude() != 0:
                self.movement = self.movement.normalize()


            self.hitbox.x += self.movement.x
            self.collision('horizontal')
            self.hitbox.y += self.movement.y
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
        self.go(self.v)


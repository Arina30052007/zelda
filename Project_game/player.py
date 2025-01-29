import pygame
from settings import *
from Project_game.settings import WORLD_MAP2
from main2 import Game2

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, m, z):
        super().__init__(groups)
        self.image = pygame.image.load('data\\player1,1_processed.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.image.convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -26)
        self.pos = pos
        self.movement = pygame.math.Vector2()
        self.v = 5
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None
        self.obstacle_sprites = obstacle_sprites
        self.m = m
        self.z = z
        self.coin = 0
        self.import_player_assets()
        self.status = 'down'

    def import_player_assets(self):
        character_path = '/data/player1,1_processed.png'
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'right_attack': [], 'left_attack': [], 'up_attack': [], 'down_attack': []}

    def keyboard(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.movement.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.movement.y = 1
            self.status = 'down'
        else:
            self.movement.y = 0
        if keys[pygame.K_RIGHT]:
            self.movement.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.movement.x = -1
            self.status = 'left'
        else:
            self.movement.x = 0
        #attack
        if keys[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            print('attack')

    def get_status(self):
        if self.movement.x == 0 and self.movement.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'
        if self.attacking:
            self.movement.x = 0
            self.movement.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack', '')


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

    def col(self):
        for sprite in self.m:
            if sprite.hitbox.colliderect(self.hitbox):
                Game2()
        for star in self.z:
            if star.hitbox.colliderect(self.hitbox):
                self.coin += 1
                star.kill()

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False

    def update(self):
        self.keyboard()
        self.cooldowns()
        self.get_status()
        self.go(self.v)
        self.col()
import pygame
from main3 import Game3

class Player2(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, m, d):
        super().__init__(groups)
        self.image = pygame.image.load('data\\player1,1_processed.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.image.convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -26)
        self.pos = pos
        self.d = d
        self.movement = pygame.math.Vector2()
        self.v = 5
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None
        self.obstacle_sprites = obstacle_sprites
        self.m = m
        self.coin = 0
        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.mcount = 0
        self.s = pygame.mixer.music.load("data\\fight.mp3")

    def import_player_assets(self):
        character_path = '/data/player1,1_processed.png'
        p = pygame.image.load('data\\char.png')
        p = pygame.transform.scale(p, (60, 60))
        p1 = pygame.image.load('data\\d1.png')
        p1 = pygame.transform.scale(p1, (60, 60))
        p2 = pygame.image.load('data\\d2.png')
        p2 = pygame.transform.scale(p2, (60, 60))
        p3 = pygame.image.load('data\\d3.png')
        p3 = pygame.transform.scale(p3, (60, 60))
        p4 = pygame.image.load('data\\d4.png')
        p4 = pygame.transform.scale(p4, (60, 60))
        p5 = pygame.image.load('data\\d5.png')
        p5 = pygame.transform.scale(p5, (60, 60))
        p6 = pygame.image.load('data\\d6.png')
        p6 = pygame.transform.scale(p6, (60, 60))
        p7 = pygame.image.load('data\\d7.png')
        p7 = pygame.transform.scale(p7, (60, 60))
        p8 = pygame.image.load('data\\d8.png')
        p8 = pygame.transform.scale(p8, (60, 60))
        p9 = pygame.image.load('data\\d9.png')
        p9 = pygame.transform.scale(p9, (60, 60))
        b1 = pygame.image.load('data\\b1.png')
        b1 = pygame.transform.scale(b1, (60, 60))
        b2 = pygame.image.load('data\\b2.png')
        b2 = pygame.transform.scale(b2, (60, 60))
        b3 = pygame.image.load('data\\b3.png')
        b3 = pygame.transform.scale(b3, (60, 60))
        b4 = pygame.image.load('data\\b4.png')
        b4 = pygame.transform.scale(b4, (60, 60))
        b5 = pygame.image.load('data\\b5.png')
        b5 = pygame.transform.scale(b5, (60, 60))
        b6 = pygame.image.load('data\\b6.png')
        b6 = pygame.transform.scale(b6, (60, 60))
        b7 = pygame.image.load('data\\b7.png')
        b7 = pygame.transform.scale(b7, (60, 60))
        b8 = pygame.image.load('data\\b8.png')
        b8 = pygame.transform.scale(b8, (60, 60))
        b9 = pygame.image.load('data\\b9.png')
        b9 = pygame.transform.scale(b9, (60, 60))
        b10 = pygame.image.load('data\\b10.png')
        b10 = pygame.transform.scale(b10, (60, 60))
        r1 = pygame.image.load('data\\r1.png')
        r1 = pygame.transform.scale(r1, (60, 60))
        r2 = pygame.image.load('data\\r2.png')
        r2 = pygame.transform.scale(r2, (60, 60))
        r3 = pygame.image.load('data\\r3.png')
        r3 = pygame.transform.scale(r3, (60, 60))
        r4 = pygame.image.load('data\\r4.png')
        r4 = pygame.transform.scale(r4, (60, 60))
        r5 = pygame.image.load('data\\r5.png')
        r5 = pygame.transform.scale(r5, (60, 60))
        r6 = pygame.image.load('data\\r6.png')
        r6 = pygame.transform.scale(r6, (60, 60))
        r7 = pygame.image.load('data\\r7.png')
        r7 = pygame.transform.scale(r7, (60, 60))
        r8 = pygame.image.load('data\\r8.png')
        r8 = pygame.transform.scale(r8, (60, 60))
        r9 = pygame.image.load('data\\r9.png')
        r9 = pygame.transform.scale(r9, (60, 60))
        r10 = pygame.image.load('data\\r10.png')
        r10 = pygame.transform.scale(r10, (60, 60))
        l1 = pygame.image.load('data\\l1.png')
        l1 = pygame.transform.scale(l1, (60, 60))
        l2 = pygame.image.load('data\\l2.png')
        l2 = pygame.transform.scale(l2, (60, 60))
        l3 = pygame.image.load('data\\l3.png')
        l3 = pygame.transform.scale(l3, (60, 60))
        l4 = pygame.image.load('data\\l4.png')
        l4 = pygame.transform.scale(l4, (60, 60))
        l5 = pygame.image.load('data\\l5.png')
        l5 = pygame.transform.scale(l5, (60, 60))
        l6 = pygame.image.load('data\\l6.png')
        l6 = pygame.transform.scale(l6, (60, 60))
        l7 = pygame.image.load('data\\l7.png')
        l7 = pygame.transform.scale(l7, (60, 60))
        l8 = pygame.image.load('data\\l8.png')
        l8 = pygame.transform.scale(l8, (60, 60))
        l9 = pygame.image.load('data\\l9.png')
        l9 = pygame.transform.scale(l9, (60, 60))
        l10 = pygame.image.load('data\\l10.png')
        l10 = pygame.transform.scale(l10, (60, 60))



        a_l = pygame.image.load('data\\attackleft-Photoroom.png')
        a_l = pygame.transform.scale(a_l, (80, 60))
        a_d = pygame.image.load('data\\attackdown-Photoroom.png')
        a_d = pygame.transform.scale(a_d, (80, 80))
        a_r = pygame.image.load('data\\attackright-Photoroom.png')
        a_r = pygame.transform.scale(a_r, (80, 60))
        a_u = pygame.image.load('data\\attackup-Photoroom.png')
        a_u = pygame.transform.scale(a_u, (60, 60))
        self.animations = {'up': [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10], 'down': [p, p1, p2, p3, p4, p5, p6, p7, p8, p9], 'left': [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10], 'right': [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10],
                           'up_idle': [b1], 'down_idle': [p], 'left_idle': [l1], 'right_idle': [r1],
                           'right_attack': [a_r], 'left_attack': [a_l], 'up_attack': [a_u], 'down_attack': [a_d]}



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
        for monster in self.m:
            if monster.hitbox.colliderect(self.hitbox) and self.attacking:
                self.mcount += 1
                monster.kill()
                pygame.mixer.music.play(0, 18)
        for princess in self.d:
            if princess.hitbox.colliderect(self.hitbox):
                Game3(self.mcount)

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)



    def update(self):
        self.keyboard()
        self.cooldowns()
        self.animate()
        self.get_status()
        self.go(self.v)
        self.col()
import pygame


class Rock2(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        colorkey = -1
        self.image = pygame.image.load('data\\rock-Photoroom.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.image.convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)


class Princess(pygame.sprite.Sprite):
    def __init__(self, pos, groups, d):
        super().__init__(groups)
        self.d = d
        self.image = pygame.image.load('data\\princess-Photoroom.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.image.convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)


    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_1
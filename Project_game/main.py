import pygame, sys
from level import Setup
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Zelda")
        self.clock = pygame.time.Clock()
        self.level = Setup()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(50)

if __name__ == '__main__':
    game = Game()
    game.run()

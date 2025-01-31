from level2 import Setup2
import pygame, sys

class Game2:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Zelda")
        self.clock = pygame.time.Clock()
        self.level2 = Setup2()
        self.run()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            self.screen.fill('#1E5945')
            self.level2.run()
            pygame.display.update()
            self.clock.tick(65)

if __name__ == '__main__':
    game = Game2()
    game.run()
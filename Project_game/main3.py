import pygame
import sys


class Game3:
    def __init__(self, mcount):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Zelda")
        self.clock = pygame.time.Clock()
        self.mcount = mcount
        self.last_screen()


    def terminate(self):
        pygame.quit()
        sys.exit()

    def last_screen(self):
        intro_text = ["ВЫ ПРОШЛИ ИГРУ", "",
                      "РЕЗУЛЬТАТ:",
                      f"{self.mcount}/7 поверженных врагов"]

        self.image = pygame.image.load('data\\end.jpg')
        self.image = pygame.transform.scale(self.image, (1000, 600))
        self.screen.blit(self.image, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    return  # начинаем игру
            pygame.display.flip()
            self.clock.tick(65)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


if __name__ == '__main__':
    game = Game3()
    game.run()
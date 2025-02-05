import pygame, sys
from level import Setup
from settings import *
import os
import sys

import os, sys
import pygame


import pygame, sys
from level import Setup
from settings import *
from sword import Stars


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Zelda")
        self.clock = pygame.time.Clock()
        self.level = Setup()
        self.start_screen()


    def terminate(self):
        pygame.quit()
        sys.exit()

    def start_screen(self):

        intro_text = ["НАЖМИ ЧТОБЫ ИГРАТЬ", "",
                      "Игра состоит из двух уровней",
                      "1. Лабиринт (соберите все звезды!)",
                      "2.Сражение с монстрами для спасения принцессы"]

        self.image = pygame.image.load('data\\fon.gif')
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

            self.screen.fill('#1E5945')
            self.level.run()
            pygame.display.update()
            self.clock.tick(65)

if __name__ == '__main__':
    game = Game()
    game.run()
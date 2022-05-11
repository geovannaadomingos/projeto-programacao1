from pathlib import Path
import pygame
from menu import *  # importa todas as classes
import os
import sys


class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.ESC_KEY = False, False, False, False  # TECLAS
        self.DISPLAY_W, self.DISPLAY_H = 1024, 768  # TAMANHO DA DELA
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))  # CRIA A TELA COM AQUELAS DIMESSÕES
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        ttf_path = (Path(sys.path[0]) / "assets") / "fonte.ttf"
        self.font = pygame.font.Font(ttf_path, 80)
        self.background = pygame.image.load((Path(sys.path[0]) / "assets") / "TELAA.png")
        self.background_credits = pygame.image.load((Path(sys.path[0]) / "assets") / "telaredd.png")
        self.BLACK, self.WHITE = (0,0,0), ((105,105,105))  # CORES
        self.main_menu = MainMenu(self)  # referncia meu objeto do menu principal  epermite que a de baixo mude de acordo com o que for selecionado
        self.credits = CreditsMenu(self)
        self.levels = LevelsMenu(self)
        self.controls = ControlsMenu(self)
        self.curr_menu = self.main_menu  # o jogo vai passar a si proprio como parametro para o menu principal class

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)
            # self.draw_text('NOSSO JOGUINHO AQUI :)', 20, self.DISPLAY_W / 2, self.DISPLAY_H / 2)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self):  # função que vai checar as teclas que estão sendo pressionadas
        for event in pygame.event.get():  # passa por uma lista de tudo que o jogador pode fazer no computador
            if event.type == pygame.QUIT:  # se CLICOU NO X
                self.running, self.playing = False, False
                self.curr_menu.run_display = False  # impede que o menu que esta sendo executado seja executado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.ESC_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):  # verifica se o jogador ainda ta segurando a tecla chave
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.ESC_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):  # desenhar texto na tela
        text_surface = self.font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
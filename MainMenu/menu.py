import pygame
import os
from datamanager import DataManager
from gamemanager import GameManager

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20,20)  # quadrado de 20x20 como um cursor, nele pode colocar qualquer imagem
        self.offset = - 150  # para que nao fique encima e sim na esquerda

    def draw_cursor(self):  # desenhar o *
        self.game.draw_text('*', 80, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):  # levar nosso menu para tela
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 20  # saber onde isso vai ser desenhado aq por ex ta bem no meio
        self.levelsx, self.levelsy = self.mid_w, self.mid_h + 60
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 100  # aq estmaos movendo as caixas de texto pra baixo -20 no valor y
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 140
        self.logox, self.logoy = self.mid_w, self.mid_h + (-50)
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)  # alinhando o * com o texto inicial

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.game.background, (0,0))
            self.game.draw_text('Fazendinha Cin', 80, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 80)
            self.game.draw_text("Start Game", 80, self.startx, self.starty)
            self.game.draw_text("Levels", 80, self.levelsx, self.levelsy)
            self.game.draw_text("Controls", 80, self.controlsx, self.controlsy)
            self.game.draw_text("Credits", 80, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):  # aqui vai ser se a pessoa tiver em credits e ele apertar pra baixo, ele sobre para start game
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.levelsx + self.offset, self.levelsy)
                self.state = 'Levels'
            elif self.state == 'Levels':
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
                self.state = 'Controls'
            elif self.state == 'Controls':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
                self.state = 'Controls'
            elif self.state == 'Controls':
                self.cursor_rect.midtop = self.cursor_rect.midtop = (self.levelsx + self.offset, self.levelsy)
                self.state = 'Levels'
            elif self.state == 'Levels':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'

    def check_input(self):  # ver o que o usuario deseja fazer
        self.move_cursor()
        if self.game.START_KEY:
            print(f"Estado atual >: {self.state}")
            if self.state == 'Start':
                GameManager.runLevel(self.game.window, 0)
            elif self.state == 'Levels':
                self.game.curr_menu = self.game.levels
            elif self.state == 'Controls':
                self.game.curr_menu = self.game.controls
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False  # ele diz pra funcao display menu parar, para rodar o jogo


class ControlsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)  # REDEFINE A TEA PARA PRETO
            self.game.display.blit(self.game.background_credits, (0,0))
            self.game.draw_text('CONTROLES', 25, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 120)
            self.blit_screen()
      

class LevelsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.cursor_index = 1
        self.cursor_rect.midtop = (self.mid_w - 100, ((self.game.DISPLAY_H / 2) - 50) + (self.cursor_index * 50))

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.BACK_KEY:
                self.close_menu()
                continue
            self.game.display.fill(self.game.BLACK)  # REDEFINE A TEA PARA PRETO
            self.game.display.blit(self.game.background_credits, (0,0))
            self.game.draw_text('LEVELS AQUI', 25, self.game.DISPLAY_W / 2, (self.game.DISPLAY_H / 2) - 120)
            for index, level in enumerate(DataManager.LEVELS_DATA):
                if level == "0":
                    continue
                self.game.draw_text(f'LEVEL {level}', 25, self.game.DISPLAY_W / 2, ((self.game.DISPLAY_H / 2) - 50) + (index * 50))

            if self.game.DOWN_KEY or self.game.UP_KEY:
                if self.game.UP_KEY:
                    self.cursor_index = (self.cursor_index-1) % (len(DataManager.LEVELS_DATA))
                    if self.cursor_index <= 0:
                        self.cursor_index = len(DataManager.LEVELS_DATA) - 1 
                elif self.game.DOWN_KEY:
                    self.cursor_index = ((self.cursor_index) % (len(DataManager.LEVELS_DATA)-1)) + 1
                self.cursor_rect.midtop = (self.mid_w - 100, ((self.game.DISPLAY_H / 2) - 50) + (self.cursor_index * 50))
            elif self.game.START_KEY:
                GameManager.runLevel(self.game.window, self.cursor_index)
                self.close_menu()
                continue

            self.draw_cursor()
            self.blit_screen()
    
    def close_menu(self):
        self.game.curr_menu = self.game.main_menu
        self.run_display = False


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.game.background_credits, (0,0))  # REDEFINE A TEA PARA PRETO
            self.game.draw_text('Credits', 60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 200)
            self.game.draw_text('Made by:', 60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 100)
            self.game.draw_text('Demetriu Gabriel', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50)
            self.game.draw_text('Geovanna Domingos', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 0)
            self.game.draw_text('Giovanna Machado', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - (-50))
            self.game.draw_text('José Luiz', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - (-100))
            self.game.draw_text('Luana Brito', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - (-150))
            self.game.draw_text('Lucas Campos', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - (-200))
            self.blit_screen()

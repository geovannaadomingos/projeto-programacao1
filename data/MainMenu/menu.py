import pygame
import os


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20,
                                       20)  # quadrado de 20x20 como um cursor, nele pode colocar qualquer imagem
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
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 100  # aq estmaos movendo as caixas de texto pra baixo -20 no valor y
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 140
        self.logox, self.logoy = self.mid_w, self.mid_h + (-50)
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)  # alinhando o * com o texto inicial

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0,0,0))
            self.game.draw_text('Fazendinha Cin', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Levels", 20, self.levelsx, self.levelsy)
            self.game.draw_text("Volume", 20, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(
            self):  # aqui vai ser se a pessoa tiver em credits e ele apertar pra baixo, ele sobre para start game
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.levelsx + self.offset, self.levelsy)
                self.state = 'Levels'
            elif self.state == 'Levels':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Volume'
            elif self.state == 'Volume':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state == 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Volume'
            elif self.state == 'Volume':
                self.cursor_rect.midtop = self.cursor_rect.midtop = (self.levelsx + self.offset, self.levelsy)
                self.state = 'Levels'
            elif self.state == 'Levels':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state == 'Start'

    def check_input(self):  # ver o que o usuario deseja fazer
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Levels':
                self.game.curr_menu = self.game.levels
            elif self.state == 'Volume':
                self.game.curr_menu = self.game.volume
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False  # ele diz pra funcao display menu parar, para rodar o jogo


class VolumeMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Music'
        self.musicx, self.musicy = self.mid_w, self.mid_h + 50
        self.efectsx, self.efectsy = self.mid_w, self.mid_h + 100
        self.cursor_rect.midtop = (self.musicx + self.offset, self.musicy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()  # verificar ser o input do jogador ta mexendo o cursor
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text("Music", 80, self.musicx, self.musicy)
            self.game.draw_text("Efects", 80, self.efectsx, self.efectsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu  # ele volta pro menu principal
            self.run_display = False  # altera o menu na proxima interação do menu principal
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Music':
                self.state = 'Efects'
                self.cursor_rect.midtop = (self.efectsx + self.offset, self.efectsy)
            elif self.state == 'Efects':
                self.state = 'Music'
                self.cursor_rect.midtop = (self.musicx + self.offset, self.musicy)
        elif self.game.START_KEY:
            pass


class LevelsMenu(Menu):
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
            self.game.draw_text('LEVELS AQUI', 25, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 120)
            self.blit_screen()


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
            self.game.display.fill(self.game.BLACK)  # REDEFINE A TEA PARA PRETO
            self.game.draw_text('Credits', 80, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 350)
            self.game.draw_text('Made by:', 80, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 290)
            self.game.draw_text('Demetriu Gabriel', 60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 200)
            self.game.draw_text('Geovanna Domingos', 60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 100)
            self.game.draw_text('Giovanna Machado', 60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 0)
            self.game.draw_text('José Luiz', 60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - (-100))
            self.game.draw_text('Luana Brito', 60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - (-200))
            self.game.draw_text('Lucas Campos', 60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - (-300))
            self.blit_screen()

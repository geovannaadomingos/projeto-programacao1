import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)  #quadrado de 20x20 como um cursor, nele pode colocar qualquer imagem
        self.offset = - 100 #para que nao fique encima e sim na esquerda

    def draw_cursor(self): #desenhar o *
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self): #levar nosso menu para tela
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30  #saber onde isso vai ser desenhado aq por ex ta bem no meio
        self.levelsx, self.levelsy = self.mid_w, self.mid_h + 50
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 70 #aq estmaos movendo as caixas de texto pra baixo -20 no valor y
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty) #alinhando o * com o texto inicial

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Levels", 20, self.levelsx, self.levelsy)
            self.game.draw_text("Options", 20, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self): #aqui vai ser se a pessoa tiver em credits e ele apertar pra baixo, ele sobre para start game
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.levelsx + self.offset, self.levelsy)
                self.state = 'Levels'
            elif self.state == 'Levels':
                self.cursor_rect.midtop =  (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
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
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop =  self.cursor_rect.midtop = (self.levelsx + self.offset, self.levelsy) 
                self.state = 'Levels'
            elif self.state == 'Levels':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state == 'Start'

    def check_input(self): #ver o que o usuario deseja fazer
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Levels':
                self.game.curr_menu = self.game.levels
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False  # ele diz pra funcao display menu parar, para rodar o jogo


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()  #verificar ser o input do jogador ta mexendo o cursor
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu #ele volta pro menu principal
            self.run_display = False #altera o menu na proxima interação do menu principal
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # se quiser criar o volue e controle
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
            self.game.display.fill(self.game.BLACK) #REDEFINE A TEA PARA PRETO
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
            self.game.display.fill(self.game.BLACK) #REDEFINE A TEA PARA PRETO
            self.game.draw_text('Credits', 25, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 120)
            self.game.draw_text('Made by:', 25, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 90)
            self.game.draw_text('Demetriu Gabriel', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 60)
            self.game.draw_text('Geovanna Domingos', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 40)
            self.game.draw_text('Giovanna Machado', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('José Luiz', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 0)
            self.game.draw_text('Luana Brito', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - (-20))
            self.game.draw_text('Lucas Campos', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - (-40))
            self.blit_screen()

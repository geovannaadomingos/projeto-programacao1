from report import Report
import pygame
from pygame.locals import *
from sys import exit

from datamanager import DataManager

BLACK = (0,0,0) 
WHITE = (255,255,255)
GRAY = (128, 128, 128) 
BROWN = (150, 75, 0)

class HudReport():
    def __init__(self, largura, altura):
        self.x = 0
        self.y = 0
        self.largura = largura
        self.altura = altura
    
    def largura_retangulo(self, largura_tela):
        largura_rect = largura_tela * 0.09
        return abs(largura_rect)
    
    def altura_retangulo(self, altura_tela):
        altura_rect = altura_tela * 0.61
        return abs(altura_rect)
    
    def draw(self, screen):
        img = pygame.Surface((46, 234), pygame.SRCALPHA, 32) #tamanho do quadrado
        pygame.draw.rect(img, BROWN, (0, 0, self.largura_retangulo(self.largura), self.altura_retangulo(self.altura)), 0, 9) #(tela, cor, (X, Y, largura do retângulo, altura do retângulo))
        img.set_alpha(50)
        screen.blit(img, (self.x, self.y))
        
        cont = 0
        for planta in DataManager.PLANTAS:
            screen.blit(DataManager.PLANTAS[planta]['item-sprite'], (0, cont*18))
            cont += 1

        print(Report.currentHarvest)

#{'Cenoura': 0, 'Repolho': 0, 'Goiaba': 0, 'Berinjela': 0, 'Azulzinha': 1, 'Alface': 1, 
# 'Trigo': 1, 'Abobora': 1, 'Nabo': 1, 'Rosinha': 1, 'Beterraba': 0, 'Estrelinha': 0, 'Pepino': 0}
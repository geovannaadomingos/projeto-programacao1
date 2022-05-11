import os
from report import Report
import pygame
from pygame.locals import *
from datamanager import DataManager

BLACK = (0,0,0) 
WHITE = (255,255,255)
GRAY = (128, 128, 128) 
BROWN = (150, 75, 0)

class HudReport():
    def __init__(self, largura, altura, scale):
        self.x = 0
        self.y = 0
        self.scale = scale
        self.fonte = pygame.font.Font(os.path.join("assets", "Kenney Blocks.ttf"), 11*self.scale)
        self.largura = largura
        self.altura = altura
        self.tamanho_retangulo_largura = (self.largura * 0.07)
        self.tamanho_retangulo_altura = (self.altura * 0.61)
    
    def draw(self, screen):
        img = pygame.Surface((self.tamanho_retangulo_largura+10, self.tamanho_retangulo_altura+10), pygame.SRCALPHA, 32) #tamanho do quadrado
        pygame.draw.rect(img, BROWN, (2*self.scale, 2*self.scale, self.tamanho_retangulo_largura, self.tamanho_retangulo_altura), 0, 10) #(tela, cor, (X, Y, largura do retângulo, altura do retângulo))
        img.set_alpha(75)
        screen.blit(img, (self.x, self.y))

        count = 0
        for planta in DataManager.PLANTAS:
            screen.blit(DataManager.PLANTAS[planta]['item-sprite'], (5*self.scale, 6+(count*18)*self.scale))
            texto = self.fonte.render(str(Report.currentHarvest[planta]), True, WHITE, None)
            screen.blit(texto, (25*self.scale, 4+(count*18)*self.scale))
            count += 1
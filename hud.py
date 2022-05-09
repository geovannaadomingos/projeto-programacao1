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
    
    def draw(self, screen):
        img = pygame.Surface((100, 290), pygame.SRCALPHA, 32) #tamanho do quadrado
        pygame.draw.rect(img, BROWN, (0, 0, 100, 290), 0, 9) #(tela, cor, (X, Y, comprimento/largura do retângulo, altura do retângulo))
        img.set_alpha(50)
        screen.blit(img, (self.x, self.y))
        
        cont = 0
        for planta in DataManager.PLANTAS:
            screen.blit(DataManager.PLANTAS[planta]['item-sprite'], (0, cont*16))
            cont += 1

        print(Report.currentHarvest)
import pygame
import time
from mouse import Mouse
from main import SCREEN_W, SCREEN_H, screen

GREEN = (34, 139, 34)
BLUE  = (161, 255, 254)

earth_rect = pygame.rect(SCREEN_W//3, SCREEN_H//3, 16, 16)
color_earth_rect = BLUE

class Plantation:
    def __init__(self):
        self.amountWaterNeeded = 100 #porcentagem_agua abaixo de 50% a terra já pede
        self.seeds_recive = None
        self.plantCollect = None

    def draw(self):
        pygame.draw.rect((SCREEN_W, SCREEN_H), color_earth_rect, earth_rect)
    
    def receiveSeed(self, seeds):
        self.seeds_recive = seeds
        self.time_received = time.time()

    def reciveWatter(self, amountWaterNeeded):
        self.amountOfWatter = amountWaterNeeded

    def needWater(self):
        if self.amountOfWatter <= 50:
            print('preciso de agua')

    """def mudar_imagem(self):
        if seeds.evolucao >= 25:
            #imagem1...
            pass"""

    def collectPlant(self, seeds):
        self.plantCollect = seeds
    
    def loop(self):
        if self.seeds_recive != None:
            tempo_passado = time.time() - self.time_received
            if tempo_passado >= self.seeds_recive.tempo_colher:
                print('planta madura')
                self.seeds_recive.evolucao = 100
            elif tempo_passado < self.seeds_recive.tempo_colher:
                print('planta crescendo')
        
        if self.plantCollect != None:
            if self.plantCollect.evolucao == 100:
                #pygame.blit(screen, img ,earth_rect)
                print('PLANTA COLETADA')
                self.seeds_recive = None
                self.plantCollect = None

        if self.amountOfWatter != None:
            if tempo_passado >= 10:
                self.amountOfWatter -= 10
                self.amountOfWatter = None
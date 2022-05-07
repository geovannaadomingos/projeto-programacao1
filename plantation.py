import pygame
import time
from main import SCREEN_W, SCREEN_H

GREEN = (34, 139, 34)
BLUE  = (161, 255, 254)

earth_rect = pygame.rect(SCREEN_W//3, SCREEN_H//3, SCREEN_W//3, SCREEN_H)
color_earth_rect = BLUE

class Terra_fertil:
    def __init__(self):
        self.quant_agua = 100 #porcentagem_agua abaixo de 50% a terra já pede
        #self.evolucao = 0 # 0 a 100%
        self.semente_recebida = None
        self.planta_coletar = None

    def draw(self):
        pygame.draw.rect((SCREEN_W, SCREEN_H), color_earth_rect, earth_rect)
    
    def receive_seed(self, semente):
        self.semente_recebida = semente
        self.tempo_recebido = time.time()

    """def receber_agua(self, quantidade_agua):
        self.quant_agua = quantidade_agua

    def pedir_agua(self):
        if self.quant_agua <= 50:
            print('preciso de agua')

    def mudar_imagem(self):
        if Semente.evolucao >= 25:
            #imagem1...
            pass"""

    def collect_plant(self, semente):
        self.planta_coletar = semente
    
    def loop(self):
        if self.semente_recebida != None:
            tempo_passado = time.time() - self.tempo_recebido
            if tempo_passado >= self.semente_recebida.tempo_colher:
                print('planta madura')
                self.semente_recebida.evolucao = 100
            elif tempo_passado < self.semente_recebida.tempo_colher:
                print('planta crescendo')
        
        if self.planta_coletar != None:
            if self.planta_coletar.evolucao == 100:
                for event in pygame.event.get():
                    pos = pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if earth_rect.collidepoint(pos):
                            print('PLANTA COLETADA')
                            self.semente_recebida = None
                            self.planta_coletar = None
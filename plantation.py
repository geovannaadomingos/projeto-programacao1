from pygame import Surface
from gamemanager import GameManager
from gameobject import GameObject
from item import PlantItem
from mouse import Mouse
from vector2 import Vector2

class Plantation(GameObject):
    all_plantations = []
    def __init__(self, v2_pos):
        super().__init__(v2_pos, Vector2(16, 16) * GameManager.scale, clickable=True)
        self.amountOfWater = 1 #porcentagem_agua abaixo de 50% a terra já pede
        self.evolucao = 0
        self.seed = None
        self.tempo_plantado = 0
        self.tempo_terreno = 0
        Plantation.all_plantations.append(self)
        self.surface = Surface(self.v2_size)
        self.surface.fill((0,0,0))


    def draw(self, screen):
        # screen.blit(self.surface, self.v2_pos)
        if self.seed != None:

            if self.needWater():
                # desenha gotinha
                pass

            evolucao = self.getEvolution()

            if evolucao <= 0.25:
                screen.blit(self.seed.data['planta-sprites'][0], self.v2_pos)
            elif evolucao <= 0.5:
                screen.blit(self.seed.data['planta-sprites'][1], self.v2_pos)
            elif evolucao <= 0.75:
                screen.blit(self.seed.data['planta-sprites'][2], self.v2_pos)
            else:
                screen.blit(self.seed.data['planta-sprites'][3], self.v2_pos)
            #elif self.getEvolution() == 1:
                #screen.blit(self.seed.data['planta-sprites'][3], self.v2_pos)
    
    def canReceiveSeed(self):
        return self.seed == None

    def receiveSeed(self, seed): # receber semente
        self.seed = seed
        self.tempo_plantado = 0

    def receiveWater(self, amountOfWaterNeeded): # receber agua
        self.amountOfWater += amountOfWaterNeeded
        self.amountOfWater = min(self.amountOfWater, 1)

    def needWater(self): # pede agua quando a planta tiver secando
        return self.amountOfWater <= 0.5

    """def mudar_imagem(self):
        if seeds.evolucao >= 25:
            #imagem1...
            pass"""

    def getEvolution(self):
        if self.seed != None:
            return min(self.tempo_plantado / self.seed.tempo_colher, 1)
        else:
            return 0

    def brotar(self):
        PlantItem(self.v2_pos, self.seed.name)
        self.seed = None
    
    def loop(self):
        if self.seed != None:
            if self.needWater() == False:
                self.tempo_plantado += GameManager.deltaTime
                self.tempo_terreno += GameManager.deltaTime

                if self.getEvolution() >= 1:
                    # brotar
                    self.brotar()

            if self.tempo_terreno >= 10:
                self.tempo_terreno = 0
                self.amountOfWater -= 0.1
                self.amountOfWater = max(0, self.amountOfWater)

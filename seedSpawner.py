import random
from gameobject import GameObject
from item import Item, SeedItem
from report import Report
from vector2 import Vector2
import gamemanager

class SeedSpawner(GameObject):
    def __init__(self, v2_pos):
        super().__init__(v2_pos, Vector2(16, 16) * gamemanager.GameManager.scale, False)
        self.temporizador = 0
        self.lastItem = None
        self.spawnRandomSeed()
    
    def loop(self):
        if self.lastItem == None or (self.lastItem != None and self.lastItem in Item.all_itens):
            self.temporizador += gamemanager.GameManager.deltaTime
            if self.temporizador >= 5:
                self.spawnRandomSeed()
                self.temporizador = 0

    def spawnRandomSeed(self):
        item_nome = "Cenoura"
        keys = list(Report.getCurrentHarvestGoal().keys())
        for x in range(5):
            rnd = random.randint(0, len(keys))
            if Report.getCurrentHarvestGoal()[keys[rnd]] > 0:
                item_nome = keys[rnd]
                break

        self.lastItem = SeedItem(self.v2_pos, item_nome)
        


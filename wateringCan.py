from vector2 import Vector2
from datamanager import DataManager
from item import Item

class WateringCan(Item):

    def __init__(self):
        self.surface = DataManager.OBJECTS['wateringCan'].copy()
        super().__init__(Vector2(0,0), Vector2.FromList(self.surface.get_size()), "WateringCan", surface=self.surface)
        self.enabled = False
        self.amountOfWater = 0.2

    def canRestock(self):
        return self.amountOfWater <= 0.9

    def hasWater(self):
        return self.amountOfWater > 0.1

    def water(self, plantation):
        amountWaterNeeded = 1 - plantation.amountOfWater
        amountToGive = min(self.amountOfWater, amountWaterNeeded)

        plantation.receiveWater(amountToGive)
        self.amountOfWater -= amountToGive
        
        if self.hasWater() == False:
            self.surface.blit(DataManager.OBJECTS["waterDrop"], (0,0))
        
        print(f"Agua: {self.amountOfWater}")

    def restock(self, receivedWater):
        self.amountOfWater += receivedWater
        self.amountOfWater = min(self.amountOfWater, 1)
        if self.hasWater():
            self.surface = DataManager.OBJECTS["wateringCan"].copy()
        print(f"Agua: {self.amountOfWater}")

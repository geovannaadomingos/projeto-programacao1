from vector2 import Vector2
from datamanager import DataManager
from item import Item

class WateringCan(Item):

    def __init__(self):
        self.surface = DataManager.OBJECTS['wateringCan']
        super().__init__(Vector2(0,0), Vector2.FromList(self.surface.get_size()), "WateringCan", surface=self.surface)
        self.enabled = False
        self.amountOfWater = 1

    def water(self, plantation):
        amountWaterNeeded = 1 - plantation.amountOfWater
        print(f"Aquando >: {amountWaterNeeded}")
        print(f"Agua do regador >: {self.amountOfWater}")
        if self.amountOfWater >= amountWaterNeeded:
            plantation.receiveWater(amountWaterNeeded)
            self.amountOfWater -= amountWaterNeeded

    def restock(self, receivedWater):
        self.amountOfWater += receivedWater
        self.amountOfWater = min(self.amountOfWater, 1)

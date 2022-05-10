from place import Place
from vector2 import Vector2
import datamanager

class WaterWell(Place):
    def __init__(self, v2_spawnPos):
        image = datamanager.DataManager.OBJECTS['waterWell']
        super().__init__(v2_spawnPos, Vector2.FromList(image.get_size()))
        self.surface = image

    def restockWateringCan(self, wateringCan):
        wateringCan.restock(self, 1)

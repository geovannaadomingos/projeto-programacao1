from typing_extensions import Self
from gameobject import GameObject
from plantation import Plantation


class WateringCan(GameObject):

    def __init__(self, v2_spawnPos, v2_size):
        super().__init__(v2_spawnPos, v2_size, clickable=True)
        self.amountOfWater = 1

    def water(self, plantation, amountOfWater):

        if amountOfWater < plantation.amountWaterNeeded:
            self.restock()
        else:
            plantation.receiveWater(plantation.amountWaterNeeded)
            amountOfWater -= plantation.amountWaterNeeded

    def restock(self):
        print("Ir pegar água no poço")

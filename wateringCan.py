from gameobject import GameObject


class WateringCan(GameObject):

    def __init__(self, v2_spawnPos, v2_size):
        super().__init__(v2_spawnPos, v2_size, clickable=True)
        self.amountOfWater = 1

    def water(self, plantation):
        amountWaterNeeded = 1 - plantation.water
        if self.amountOfWater >= amountWaterNeeded:
            plantation.receiveWater(amountWaterNeeded)
            self.amountOfWater -= amountWaterNeeded

    def restock(self, receivedWater):
        self.amountOfWater += receivedWater
        self.amountOfWater = min(self.amountOfWater, 1)

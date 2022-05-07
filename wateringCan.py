from gameobject import GameObject


class WateringCan(GameObject):

    def __init__(self, v2_spawnPos, v2_size):
        super().__init__(v2_spawnPos, v2_size, clickable=True)
        self.amountOfWater = 1

    def water(self, plantation):

        if self.amountOfWater >= plantation.amountWaterNeeded:
            plantation.receiveWater(plantation.amountWaterNeeded)
            self.amountOfWater -= plantation.amountWaterNeeded

    def restock(self, receivedWater):
        self.amountOfWater += receivedWater
        self.amountOfWater = min(self.amountOfWater, 1)

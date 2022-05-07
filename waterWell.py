from place import Place


class WaterWell(Place):
    def __init__(self, v2_spawnPos, v2_size):
        super().__init__(v2_spawnPos, v2_size, (0, 0, 255))

    def restockWateringCan(self, wateringCan):
        wateringCan.restock(self, 1)

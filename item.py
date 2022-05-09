import pygame
import datamanager
from gameobject import GameObject
from vector2 import Vector2


class Item(GameObject):
    all_itens = []

    def __init__(self, v2_spawnPos, v2_size, name):
        super().__init__(v2_spawnPos, v2_size, False)
        self.name = name
        Item.all_itens.append(self)

class PlantItem(Item):
    def __init__(self, v2_pos, name):
        self.surface = datamanager.DataManager.PLANTAS[name]["item-sprite"]
        super().__init__(v2_pos, Vector2.FromList(self.surface.get_size()), name)

    def draw(self, screen):
        screen.blit(self.surface, self.v2_pos)

class SeedItem(Item):
    def __init__(self, v2_pos, name):
        self.surface = datamanager.DataManager.PLANTAS[name]["semente-sprite"]
        super().__init__(v2_pos, Vector2.FromList(self.surface.get_size()), name)

    def draw(self, screen):
        screen.blit(self.surface, self.v2_pos)

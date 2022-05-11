import pygame
import datamanager
import gameobject
from vector2 import Vector2


class Item(gameobject.GameObject):
    all_itens = []

    def __init__(self, v2_spawnPos, v2_size, name, surface=None):
        super().__init__(v2_spawnPos, v2_size, False)
        self.name = name
        self.enabled = True
        self.surface = surface
        self.v2_collideBox = Vector2(16,16) * (self.v2_size.x//16) * 0.5
        self.v2_collideOffset = (self.getCenterPos() - (self.v2_collideBox/2)) - self.v2_pos
        Item.all_itens.append(self)

class PlantItem(Item):
    def __init__(self, v2_pos, name):
        self.surface = datamanager.DataManager.PLANTAS[name]["item-sprite"]
        super().__init__(v2_pos, Vector2.FromList(self.surface.get_size()), name, self.surface)

    def draw(self, screen):
        screen.blit(self.surface, self.v2_pos)

class SeedItem(Item):
    def __init__(self, v2_pos, name):
        self.surface = datamanager.DataManager.PLANTAS[name]["semente-sprite"]
        super().__init__(v2_pos, Vector2.FromList(self.surface.get_size()), name, self.surface)
        self.data = datamanager.DataManager.PLANTAS.get(name, None)
        self.tempo_colher = self.data["time_to_grow_sec"]

    def draw(self, screen):
        if not self.enabled:
            return
        screen.blit(self.surface, self.v2_pos)
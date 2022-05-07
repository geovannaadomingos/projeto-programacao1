import pygame
from vector2 import Vector2
from gameobject import GameObject


class Estabelecimento(GameObject):
    def __init__(self, v2_spawnPos, v2_size, color=(255, 255, 255)):
        super().__init__(v2_spawnPos, v2_size, clickable=True)
    
        self.surface = pygame.Surface((self.v2_size.toTuple()))
        self.surface.fill(color)

    def draw(self, screen):
        screen.blit(self.surface, self.v2_pos.toTuple())

    def handleClick(self, bot_selected):
        bot_selected.moveTo(self.v2_pos, self.example_func_arrive)

    def example_func_arrive(self, bot):
        print("Bot chegou ao destino")

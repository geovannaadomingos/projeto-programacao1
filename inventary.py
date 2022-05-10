import pygame
from gamemanager import GameManager

class Inventory:
    #rect = (612, 768, 300, 300)
    def __init__(self):
        self.slots = []
        
        for i in range(9):
            surface = pygame.Surface((55, 55), pygame.SRCALPHA, 32)
            pygame.draw.rect(surface, (75, 54, 33),(0,0, 55, 55))
            self.slots.append(surface)

    def draw(self, screen):
        x = 0
        y = 0
        inventory = GameManager.farmer.inventory

        for slot in self.slots:
            screen.blit(slot, (x, y))

            if len(inventory) > 0:
                #for num in range(inventory):
                screen.blit(inventory[0].surface, (x, y))
            
            x += 60
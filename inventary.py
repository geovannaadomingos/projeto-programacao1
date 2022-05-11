import pygame
from datamanager import DataManager
import gamemanager

BROWN = (150, 75, 0)
RED = (255, 0, 0)

class Inventory:
    #rect = (612, 768, 300, 300)
    def __init__(self):
        self.slots = []
        
        for i in range(9):
            surface = pygame.Surface((55, 55), pygame.SRCALPHA, 32)
            pygame.draw.rect(surface, BROWN,(0, 0, 55, 55), 0, 10)
            surface.set_alpha(100)
            self.slots.append(surface)

    def draw(self, screen):
        x = 250
        y = 670
        inventory = gamemanager.GameManager.farmer.inventory
        

        for slot in self.slots:
            screen.blit(slot, (x, y))
            x += 60

        for index in range(len(inventory)):
            if inventory[index] != None:
                screen.blit(DataManager.scaleImage(inventory[index].surface, 1.5), (254+(index*60), y+4))
        
        gamemanager.GameManager.farmer.selectedInventoryIndex
        pygame.draw.rect(screen, RED,(250+(gamemanager.GameManager.farmer.selectedInventoryIndex*60), y, 55, 55), 2, 10)
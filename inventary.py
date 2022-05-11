import pygame
import gamemanager

class Inventory:
    #rect = (612, 768, 300, 300)
    def __init__(self):
        self.slots = []
        
        for i in range(9):
            surface = pygame.Surface((55, 55), pygame.SRCALPHA, 32)
            pygame.draw.rect(surface, (75, 54, 33),(0,0, 55, 55))
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
                screen.blit(inventory[index].surface, (250+(index*60),y))
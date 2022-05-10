import pygame
from gamemanager import GameManager
from item import Item

class InventarySlot:
    def __init__(self, name, v2_pos):
        self.image = pygame.image.load(name)
        self.rect = self.image.get_rect()
        self.rect.topleft = v2_pos
        self.count = 0

        self.font = pygame.font.SysFont("arial", 20)

    def draw(self, screen):
        text = self.font.render(str(self.count), True, (0, 0, 0))
        screen.blit(self.image, self.rect)
        screen.blit(text, self.rect.midright)

class Inventory:
    def __init__(self):
        self.slots = GameManager.farmer.inventory
        self.rect = self.image.get_rect()
        self.rect.topleft = (10, 360)

        self.slots.append(InventarySlot(Item.surface, 25))

    def draw(self, screen):
        self.backgroundInventory = pygame.rect(screen, (255, 255, 255), (1024//2, 768, 45, 234), 0, 9)
        screen.blit(self.backgroundInventory, self.rect)
        for slot in self.slots:
            slot.render(screen)
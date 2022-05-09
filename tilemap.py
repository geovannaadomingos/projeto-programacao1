import pygame


class Tilemap():
    def __init__(self):
        self.layers = []

    def load(self, data):
        sheets = {}
        tiles = {}
        
        for tilePath in data["tiles"]:
            sheetPath, position = tilePath.split("/")
            x, y = map(int, position.split("_"))

            sheet = sheet.get(sheetPath, None)
            
            if sheet == None:
                sheet = pygame.image.load(sheetPath)
                sheets[sheetPath] = sheet
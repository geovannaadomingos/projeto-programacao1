import pygame

import datamanager
from tilemapEditor import Grid
from vector2 import Vector2
import json


class Tilemap():
    def __init__(self):
        self.layers = []
        self.sheets = {}
        self.tiles = {}
        self.tiles[None] = None

    def load(self, data, scale):

        for tilePath in data["tiles"]:
            sheetPath, position = tilePath.split("/")
            imageX, imageY = map(int, position.split("_"))

            sheet = self.sheets.get(sheetPath, None)

            if sheet == None:
                sheet = pygame.image.load(sheetPath)
                self.sheets[sheetPath] = sheet

            self.tiles[tilePath] = datamanager.DataManager.getImageFromSpriteSheet(
                sheet, imageX, imageY, scale=scale)

        gridWidth = len(data["layers"][0]["grid"][0])
        gridHeight = len(data["layers"][0]["grid"])

        for layer in data["layers"]:
            grid = Grid(Vector2(0, 0), Vector2(gridWidth, gridHeight) * 16 * scale, 16*scale)
            for y, row in enumerate(layer["grid"]):
                for x, tile in enumerate(row):
                    spritePath = tile.get("tile", None)
                    if spritePath != None:
                        spritePath = spritePath["path"]

                    grid.matrix[y][x].state = tuple(tile.get("state"))
                    grid.matrix[y][x].surface = self.tiles[spritePath]
            self.layers.append(grid)
        print("loaded")

    def draw(self, screen):
        for layer in self.layers:
            layer.draw(screen)


if __name__ == "__main__":
    run = True
    scale = 2

    TILE_LENGHT = 16 * scale

    GRID_W = TILE_LENGHT * 32
    GRID_H = TILE_LENGHT * 24

    SCREEN_W = GRID_W
    SCREEN_H = GRID_H
    pygame.init()
    pygame.display.set_caption("Teste Projetinho P1")
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

    FPS = 60
    clock = pygame.time.Clock()

    tilemap = Tilemap()

    dataJson = json.load(open("data\\levels\\level_test.json"))

    tilemap.load(dataJson, scale=scale)

    while run:
        clock.tick(FPS)

        screen.fill((255, 255, 255))

        tilemap.draw(screen)

        pygame.display.update()

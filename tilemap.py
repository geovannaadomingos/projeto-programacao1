from pathlib import Path, WindowsPath
import pygame
from Events import Events
from NodeState import NodeState

import datamanager
from gameobject import GameObject
from plantation import Plantation
from tilemapEditor import Grid
from vector2 import Vector2
import json

from waterWell import WaterWell


class Tilemap():
    def __init__(self, drawLines=False):
        self.layers = []
        self.sheets = {}
        self.tiles = {}
        self.tiles[None] = None
        self.plantations = []
        self.drawLines = drawLines

    def load(self, data, scale):

        for tilePath in data["tiles"]:
            tilePath = Path(tilePath)
            position = tilePath.name
            sheetPath = Path(str(tilePath).replace(position, ""))
            imageX, imageY = map(int, position.split("_"))

            sheet = self.sheets.get(str(Path(sheetPath)), None)

            if sheet == None:
                sheet = pygame.image.load(sheetPath)
                self.sheets[str(Path(sheetPath))] = sheet

            self.tiles[str(Path(tilePath))] = datamanager.DataManager.getImageFromSpriteSheet(
                sheet, imageX, imageY, scale=scale)

        gridWidth = len(data["layers"][0]["grid"][0])
        gridHeight = len(data["layers"][0]["grid"])

        for layer in data["layers"]:
            grid = Grid(Vector2(0, 0), Vector2(gridWidth, gridHeight)
                        * 16 * scale, 16*scale, enableLines=self.drawLines)
            for y, row in enumerate(layer["grid"]):
                for x, tile in enumerate(row):
                    spritePath = tile.get("tile", None)
                    if spritePath != None:
                        spritePath = str(Path(spritePath["path"]))

                    state = tuple(tile.get("state"))
                    grid.matrix[y][x].state = state
                    grid.matrix[y][x].surface = self.tiles[spritePath]

                    if state == NodeState.Plantable:
                        self.plantations.append(
                            Plantation(grid.getScreenPos(x, y)))
                    elif state == NodeState.WaterWell:
                        WaterWell(grid.getScreenPos(x, y))
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

    tilemap = Tilemap(drawLines=True)

    dataJson = json.load(open("data\\levels\\editor\\level_1652215111.json"))

    datamanager.DataManager.load(2)

    tilemap.load(dataJson, scale=scale)

    while run:
        clock.tick(FPS)

        screen.fill((255, 255, 255))

        tilemap.draw(screen)

        for go in GameObject.all_objects:
            go.draw(screen)

        pygame.display.update()

        Events.loop()
        for event in Events.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # ESC
                    run = False
            elif event.type == pygame.QUIT:
                run = False
                continue

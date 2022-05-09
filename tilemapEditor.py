import json
import os
import pygame
from Events import Events
from NodeState import NodeState
import datamanager
from gameobject import GameObject
from mouse import Mouse
from vector2 import Vector2
import pathlib
import time

class Node():
    def __init__(self, x, y, surface, state=NodeState.Normal, item=None):
        self.x = x
        self.y = y
        self.state = state
        self.surface = surface
        self.item = item
        self.parent = None
        self.g = 0
        self.h = 0

    def valor_f(self):
        return self.g + self.h


class Grid(GameObject):
    def __init__(self, v2_pos, v2_size, nodeDiameter, nodeSurface=None, item=None, enableLines=False, drawState=False):
        super().__init__(v2_pos, v2_size, False)
        self.nodeDiameter = nodeDiameter
        self.sizeX = v2_size.x // self.nodeDiameter
        self.sizeY = v2_size.y // self.nodeDiameter
        self.matrix = []
        self.enableLines = enableLines
        self.lineWidth = 1
        self.lineColor = (0,0,0)
        self.drawState = drawState

        if nodeSurface == None:
            nodeSurface = pygame.Surface((self.nodeDiameter, self.nodeDiameter), pygame.SRCALPHA, 32).convert_alpha()

        for y in range(self.sizeY):
            self.matrix.append([])
            for x in range(self.sizeX):
                self.matrix[y].insert(x, Node(x, y, surface=nodeSurface, item=item))

        self.nodeSurfaceMouse = pygame.Surface(
            (self.nodeDiameter, self.nodeDiameter))
        self.nodeSurfaceMouse.fill((255, 0, 0))

    def neighbors(self, node):
        neighbors_list = []

        if node.x + 1 < self.sizeX:
            neighbors_list.append(self.matrix[node.y][node.x+1]) #vizinho da direita
        if node.x - 1 >= 0:
            neighbors_list.append(self.matrix[node.y][node.x-1]) #vizinho da esquerda
        if node.y + 1 < self.sizeY:
            neighbors_list.append(self.matrix[node.y+1][node.x]) #vizinho de cima
        if node.y - 1 >= 0:
            neighbors_list.append(self.matrix[node.y-1][node.x]) #vizinho de baixo
        
        return neighbors_list

    def getPositionFromPoint(self, v2_point):
        pointX = (v2_point.x - self.v2_pos.x) // self.nodeDiameter
        pointY = (v2_point.y - self.v2_pos.y) // self.nodeDiameter
        pointX = min(self.sizeX-1, max(0, pointX))
        pointY = min(self.sizeY-1, max(0, pointY))

        return int(pointX), int(pointY)

    def getNodeWithState(self, state):
        for row in self.matrix:
            for node in row:
                if node.state == state:
                    return node
        return None

    def getNodeFromPoint(self, v2_point):
        pointX, pointY = self.getPositionFromPoint(v2_point)
        return self.matrix[pointY][pointX]

    def getScreenPos(self, x, y):
        return self.v2_pos + Vector2(x * self.nodeDiameter, y * self.nodeDiameter)

    def getScreenPosCenter(self, x, y):
        return self.v2_pos + Vector2(x * self.nodeDiameter, y * self.nodeDiameter) + Vector2(self.nodeDiameter, self.nodeDiameter)/2

    def getNodeScreenPos(self, node):
        return self.getScreenPos(node.x, node.y)

    def getNodeScreenPosCenter(self, node):
        return self.getScreenPosCenter(node.x, node.y)

    def getScreenPosFromPoint(self, v2_point):
        x, y = self.getPositionFromPoint(v2_point)
        return self.getScreenPosCenter(x, y)

    def drawLines(self, screen):
        if self.enableLines == False:
            return
        
        for x in range(self.sizeX):
            #(self.x + (x * diameter), pos.y)
            #(self.x + (x * diameter), pos.y + size.y)
            pygame.draw.line(screen, self.lineColor, (self.v2_pos.x + (x*self.nodeDiameter), self.v2_pos.y), (self.v2_pos.x + (x*self.nodeDiameter), self.v2_pos.y+self.v2_size.y), width=self.lineWidth)
        for y in range(self.sizeY):
            #(pos.x, self.y + (y * diameter), width=self.lineWidth)
            #(pos.x + size.x, self.y + (y * diameter))
            pygame.draw.line(screen, self.lineColor, (self.v2_pos.x, self.v2_pos.y + y*self.nodeDiameter), (self.v2_pos.x+self.v2_size.x, self.v2_pos.y+y*self.nodeDiameter))

    def draw(self, screen):
        for nodeList in self.matrix:
            for node in nodeList:
                if node.surface != None:
                    screen.blit(node.surface, self.getNodeScreenPos(node))
                if self.drawState:
                    if node.state != NodeState.Normal:
                        self.nodeSurfaceMouse.fill(node.state)
                        self.nodeSurfaceMouse.set_alpha(50)
                        screen.blit(self.nodeSurfaceMouse, self.getNodeScreenPos(node))
        self.drawLines(screen)


class Tile():
    def __init__(self, path, surface, tileX, tileY):
        self.tileX = tileX
        self.tileY = tileY
        self.filePath = str(path) +f"/{self.tileX}_{self.tileY}"
        self.fileName = self.filePath.split("\\")[-1]+f"/{self.tileX}_{self.tileY}"
        self.surface = surface

class TilemapEditor():
    def __init__(self):
        pass

    def main(self):
        run = True
        scale = 2

        TILE_LENGHT = 16 * scale

        GRID_W = TILE_LENGHT * 32
        GRID_H = TILE_LENGHT * 24

        TILES_GRID_W = (TILE_LENGHT * 10)
        TILES_GRID_H = GRID_H

        SCREEN_W = GRID_W + TILES_GRID_W
        SCREEN_H = GRID_H
        pygame.init()
        pygame.display.set_caption("Teste Projetinho P1")
        screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

        FPS = 60
        clock = pygame.time.Clock()

        current_layer_index = 0
        layers = []

        grid_tiles = Grid(Vector2(GRID_W, 0), Vector2(TILES_GRID_W, TILES_GRID_H), TILE_LENGHT)
        grid_tiles.enableLines = True
        grid_tiles.lineColor = (156, 98, 54)

        tileset_folder = datamanager.PREMIUM_ASSETS_FOLDER + "\\tilesets"
        tilesets_sheets_paths = list(
            pathlib.Path(tileset_folder).glob('*.png'))

        tiles = []

        for sheet_path in tilesets_sheets_paths:
            image_sheet = pygame.image.load(sheet_path)
            for y in range(image_sheet.get_height() // (TILE_LENGHT//scale)):
                for x in range(image_sheet.get_width() // (TILE_LENGHT//scale)):
                    sprite = datamanager.DataManager.getImageFromSpriteSheet(
                        image_sheet, x, y, scale=scale)
                    tiles.append(Tile(sheet_path, sprite, x, y))
        
        tileX = 0
        tileY = 0
        for tile in tiles:
            grid_tiles.matrix[tileY][tileX].surface = tile.surface
            grid_tiles.matrix[tileY][tileX].item = tile

            if tileX % (TILES_GRID_W // TILE_LENGHT) == (TILES_GRID_W // TILE_LENGHT)-1:
                tileY += 1
                tileY = (tileY) % (TILES_GRID_H // TILE_LENGHT)
                
            tileX += 1
            tileX = (tileX) % (TILES_GRID_W // TILE_LENGHT)

        layers.append(Grid(Vector2(0, 0), Vector2(
            GRID_W, GRID_H), TILE_LENGHT, tiles[-1].surface, tiles[-1], enableLines = True, drawState=True))

        tileSelected = None

        print(f"Layer atual >: {current_layer_index}")
        apagar = False

        while run:
            clock.tick(FPS)

            screen.fill((255, 255, 255))

            Events.loop()
            Mouse.loop()

            criar_layer = False
            descer_layer = False
            subir_layer = False
            salvar = False
            block = False

            for event in Events.events:
                if event.type == pygame.KEYDOWN:
                    if event.key == 8:
                        apagar = True
                    elif event.key == pygame.K_RIGHT:
                        criar_layer = True
                    elif event.key == pygame.K_UP:
                        subir_layer = True
                    elif event.key == pygame.K_DOWN:
                        descer_layer = True
                    elif event.key == pygame.K_s:
                        salvar = True
                    elif event.key == pygame.K_b:
                        block = True
                elif event.type == pygame.KEYUP:
                    if event.key == 8:
                        apagar = False
            
            if subir_layer or descer_layer:
                next_layer_index = current_layer_index + (1 if subir_layer else -1)
                next_layer_index = max(0, min(len(layers)-1, next_layer_index))

                layers[next_layer_index].nodeSurfaceMouse = layers[current_layer_index].nodeSurfaceMouse
                current_layer_index = next_layer_index
                print(f"Layer atual >: {current_layer_index}")
            
            elif criar_layer:
                newLayer = Grid(Vector2(0, 0), Vector2(GRID_W, GRID_H), TILE_LENGHT, enableLines = True, drawState=True)
                layers.append(newLayer)
                print(f"Nova Layer criada >: {len(layers)-1}")
            elif salvar:
                fileName = f"level_{int(time.time())}.json"
                if os.path.exists("data\\levels") == False:
                    os.mkdir("data/levels")
                if os.path.exists("data\\levels\\editor") == False:
                    os.mkdir("data/levels/editor")
                    
                file = open(f"data\\levels\\editor\\{fileName}", 'w')
                file_dict = {}
                file_dict["tiles"] = []
                file_dict["layers"] = []
                for layer in layers:
                    grid = {}
                    grid['grid'] = []

                    for row in layer.grid:
                        tiles = []
                        for node in row:
                            node_dict = {}
                            node_dict["x"] = node.x
                            node_dict["y"] = node.y
                            node_dict["state"] = node.state
                            if node.item != None:
                                node_dict["tile"] = {}
                                if node.item.filePath not in file_dict["tiles"]:
                                    file_dict["tiles"].append(node.item.filePath)
                                node_dict["tile"]["path"] = node.item.filePath
                            tiles.append(node_dict)
                        grid['grid'].append(tiles)
                    file_dict["layers"].append(grid)
                file.write(json.dumps(file_dict, indent=4))
                file.close()
                print(f"Tilemap({fileName}) salvo com sucesso")
            
            if layers[current_layer_index].isPointInside(Mouse.getMousePos()):
                if Mouse.clicked_default(0) and tileSelected != None:
                    node = layers[current_layer_index].getNodeFromPoint(Mouse.getMousePos())
                    node.item = tileSelected
                    node.surface = tileSelected.surface
                elif apagar:
                    node = layers[current_layer_index].getNodeFromPoint(Mouse.getMousePos())
                    node.item = None
                    node.surface = None
                elif block:
                    node = layers[current_layer_index].getNodeFromPoint(Mouse.getMousePos())
                    if node.state == NodeState.Normal:
                        node.state = NodeState.Obstacle
                    elif node.state == NodeState.Obstacle:
                        node.state = NodeState.FarmerSpawn
                    elif node.state == NodeState.FarmerSpawn:
                        node.state = NodeState.Normal
                    else:
                        node.state = NodeState.Normal
                        
            elif grid_tiles.isPointInside(Mouse.getMousePos()):
                if Mouse.clicked(0):
                    tileSelected = grid_tiles.getNodeFromPoint(Mouse.getMousePos()).item
                    layers[current_layer_index].nodeSurfaceMouse = tileSelected.surface


            for layer in layers:
                layer.draw(screen)
            
            grid_tiles.draw(screen)

            pygame.display.update()


if __name__ == "__main__":
    TilemapEditor().main()

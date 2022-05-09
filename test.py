import json
import pygame
from Events import Events
from NodeState import NodeState
import datamanager
from farmer import Farmer
from gamemanager import GameManager
from gameobject import GameObject
from item import Item, PlantItem, SeedItem
from mouse import Mouse
from plantation import Plantation
from report import Report
from seeds import Seed
from tilemap import Tilemap
from tilemapEditor import Grid
from vector2 import Vector2
from waterWell import WaterWell


def main():
    pygame.init()
    pygame.display.set_caption("Teste Projetinho P1")

    FPS = 60
    clock = pygame.time.Clock()

    # Screen
    SCREEN_W = 16 * 32 * GameManager.scale
    SCREEN_H = 16 * 24 * GameManager.scale
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    datamanager.DataManager.load(GameManager.scale)

    tilemap = Tilemap()
    dataJson = json.load(open("data\\levels\\level_test.json"))
    tilemap.load(dataJson, scale=GameManager.scale)

    running = True

    # Cria poço
    waterWell = WaterWell(Vector2(500, 225), Vector2(50, 50))

    # Criar plantas coletaveis
    for y, planta_nome in enumerate(datamanager.DataManager.PLANTAS):
        PlantItem(Vector2(200, y*16*1.5*GameManager.scale), planta_nome)
    
    # Criar sementes coletaveis
    for y, planta_nome in enumerate(datamanager.DataManager.PLANTAS):
        SeedItem(Vector2(100, y*16*1.5*GameManager.scale), planta_nome)

    spawnPoint = tilemap.layers[-1].getNodeWithState(NodeState.FarmerSpawn)
    GameManager.grid = Grid(Vector2(0,0), Vector2(SCREEN_W, SCREEN_H), 16 * GameManager.scale, enableLines=False)
    GameManager.farmer = Farmer(tilemap.layers[-1].getNodeScreenPos(spawnPoint), speed=1.5)

    GameManager.updateTime()
    
    while running:
        clock.tick(FPS)
        # Preenche o display com a cor preta (0, 0, 0)
        screen.fill((255, 255, 255))

        Events.loop()
        Mouse.loop()
        GameManager.loop()

        # desenha todos os objetos na tela
        # if GameManager.grid != None:
        #     GameManager.grid.draw(screen)

        tilemap.draw(screen)

        for go in GameObject.all_objects:
            go.draw(screen)

        for event in Events.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # ESC
                    running = False
                elif event.key == pygame.K_r:
                    print(Report.currentHarvest)

        # Atualiza a tela do pygame
        pygame.display.update()


if __name__ == "__main__":
    main()

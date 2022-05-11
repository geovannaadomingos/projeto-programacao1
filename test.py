import json
import pygame
from Events import Events
from NodeState import NodeState
import datamanager
from pathlib import Path
from farmer import Farmer
from gamemanager import GameManager
from gameobject import GameObject
from inventary import Inventory
from hud import HudReport
from item import Item, PlantItem, SeedItem
from mouse import Mouse
from plantation import Plantation
from report import Report
from tilemap import Tilemap
from tilemapEditor import Grid
from vector2 import Vector2
from waterWell import WaterWell
from soundEffects import Sounds

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
    dataJson = json.load(open(Path("data/levels/level_test.json")))
    tilemap.load(dataJson, scale=GameManager.scale)

    running = True

    # Cria poço
    # waterWell = WaterWell(Vector2(500, 225), Vector2(50, 50))

    # Criar plantas coletaveis
    for y, planta_nome in enumerate(datamanager.DataManager.PLANTAS):
        PlantItem(Vector2(320+((y//5) * 16*GameManager.scale), 258+((y%5)*16*GameManager.scale)), planta_nome)


    spawnPoint = tilemap.layers[-1].getNodePosWithState(NodeState.FarmerSpawn)
    GameManager.grid = tilemap.layers[-1]
    GameManager.farmer = Farmer(spawnPoint, speed=1.5)


    GameManager.updateTime()
    inventario = Inventory()
    
    relatorio_hud = HudReport(SCREEN_W, SCREEN_H, GameManager.scale)
    Sounds.backgroundMusic()

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

        inventario.draw(screen)
        relatorio_hud.draw(screen)

        for event in Events.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # ESC
                    running = False
                elif event.key == pygame.K_r:
                    print(Report.currentHarvest)
            elif event.type == pygame.QUIT:
                running = False
                continue

        # Atualiza a tela do pygame
        pygame.display.update()


if __name__ == "__main__":
    main()

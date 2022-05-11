import json
from pathlib import Path
import pygame
from Events import Events
from NodeState import NodeState
from datamanager import DataManager
import farmer
import gameobject
from hud import HudReport
from inventary import Inventory
from item import Item, PlantItem, SeedItem
from mouse import Mouse
import time
from pathfinding import Pathfinding
from plantation import Plantation
from soundEffects import Sounds
from report import Report
from tilemap import Tilemap
from tilemapEditor import Grid
from vector2 import Vector2


class GameManager():
    time = 0
    lastTime = 0
    deltaTime = 0
    scale = 2
    farmer = None
    grid = None
    grid_collider = None
    level = 0
    running = False

    def updateTime():
        GameManager.lastTime = GameManager.time
        GameManager.time = time.time()
        GameManager.deltaTime = GameManager.time - GameManager.lastTime

    def handleClick(gameObject):
        # pega a posição do mouse
        v2_mousePos = Mouse.getMousePos()

        # if GameObject in type(gameObject).mro():
        #     if gameObject.clickable == False:
        #         return

        if GameManager.farmer != None:
            if Mouse.clicked(0):
                GameManager.farmer.handleClick(gameObject, v2_mousePos)

    def loop():
        GameManager.updateTime()
        # objeto que está sob o mouse
        go_sob_mouse = None

        # for em todos os objetos pra achar o ULTIMO objeto que está sob o mouse
        for go in gameobject.GameObject.all_objects:
            # Verifica se o mouse está posicionado sobre o objeto
            if go.clickable and go.isPointInside(Mouse.getMousePos()):
                go_sob_mouse = go
        
        GameManager.handleClick(go_sob_mouse)

        for go in gameobject.GameObject.all_objects:
            go.loop()

        for item in Item.all_itens:
            if item.isCollide(GameManager.farmer):
                if GameManager.farmer.canAddToInventory():
                    if type(item) == PlantItem:
                        # Coletar planta
                        Item.all_itens.remove(item)
                        gameobject.GameObject.all_objects.remove(item)
                        Report.harvestReport(item.name)
                        Sounds.playSFX("collect.wav")

                    elif type(item) == SeedItem:
                        # Reportar no relatorio ( talvez )
                        GameManager.farmer.addToInventory(item)
                        Item.all_itens.remove(item)
                        gameobject.GameObject.all_objects.remove(item)
                        Sounds.playSFX("bag.wav")

    def runLevel(screen, level):
        GameManager.level = level

        FPS = 60
        clock = pygame.time.Clock()

        DataManager.load(GameManager.scale)

        SCREEN_W, SCREEN_H = screen.get_size()

        tilemap = Tilemap()
        dataJson = json.load(open(Path(f"data/levels/level_{level}.json")))
        tilemap.load(dataJson, scale=GameManager.scale)

        # Criar plantas coletaveis
        for y, planta_nome in enumerate(DataManager.PLANTAS):
            SeedItem(Vector2(320+((y//5) * 16*GameManager.scale), 258+((y%5)*16*GameManager.scale)), planta_nome)


        spawnPoint = tilemap.layers[-1].getNodePosWithState(NodeState.FarmerSpawn)
        GameManager.grid = tilemap.layers[-1]
        GameManager.farmer = farmer.Farmer(spawnPoint, speed=1.5)


        GameManager.updateTime()
        
        inventario = Inventory()
        relatorio_hud = HudReport(SCREEN_W, SCREEN_H, GameManager.scale)
        Sounds.backgroundMusic()

        GameManager.running = True
        while GameManager.running:
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

            for go in gameobject.GameObject.all_objects:
                go.draw(screen)

            inventario.draw(screen)
            relatorio_hud.draw(screen)

            for event in Events.events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # ESC
                        GameManager.running = False
                    elif event.key == pygame.K_r:
                        print(Report.currentHarvest)
                elif event.type == pygame.QUIT:
                    GameManager.running = False

            # Atualiza a tela do pygame
            pygame.display.update()
        GameManager.clearObjects()

    def levelCompleted():
        print("ganhei")
        GameManager.running = False

    def clearObjects():
        GameManager.deltaTime = 0
        GameManager.farmer = None
        GameManager.grid = None
        GameManager.grid_collider = None

        Events.events = []
        gameobject.GameObject.all_objects = []
        Item.all_itens = []
        Plantation.all_objects = []
        Report.clearCurrentHarvest()

def main():
    pygame.init()
    pygame.display.set_caption("Teste Projetinho P1")

    # Screen
    SCREEN_W = 16 * 32 * GameManager.scale
    SCREEN_H = 16 * 24 * GameManager.scale
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

    GameManager.runLevel(screen, 0)

if __name__ == "__main__":
    main()
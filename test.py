import pygame
from Events import Events
import datamanager
from farmer import Farmer
from gamemanager import GameManager
from gameobject import GameObject
from item import Item, PlantItem
from mouse import Mouse
from plantation import Plantation
from report import Report
from seeds import Seed
from vector2 import Vector2
from waterWell import WaterWell


def main():
    pygame.init()
    pygame.display.set_caption("Teste Projetinho P1")

    FPS = 60
    clock = pygame.time.Clock()

    # Screen
    SCREEN_W = 400
    SCREEN_H = 400
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    datamanager.DataManager.load()

    running = True

    # Cria lago
    waterWell = WaterWell(Vector2(100, 225), Vector2(50, 50))
    PlantItem(Vector2(100, 100), "Cenoura")
    GameManager.farmer = Farmer(Vector2(25, 200), speed=1.5)

    GameManager.updateTime()
    
    while running:
        clock.tick(FPS)
        # Preenche o display com a cor preta (0, 0, 0)
        screen.fill((255, 255, 255))

        Events.loop()
        Mouse.loop()
        GameManager.loop()

        # desenha todos os objetos na tela
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

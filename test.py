import pygame
from Events import Events
from gamemanager import GameManager
from gameobject import GameObject
from mouse import Mouse
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

    running = True

    # Cria lago
    WaterWell(Vector2(25, 325), Vector2(50, 50))

    while running:
        clock.tick(FPS)
        # Preenche o display com a cor preta (0, 0, 0)
        screen.fill((0, 0, 0))

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

        # Atualiza a tela do pygame
        pygame.display.update()


if __name__ == "__main__":
    main()

import pygame
from Events import Events
from gameobject import GameObject
from mouse import Mouse


class GameManager():
    def handleClick(gameObject):
        if GameObject in type(gameObject).mro():
            if gameObject.clickable == False:
                return
        # pega a posição do mouse
        v2_mousePos = Mouse.getMousePos()

        mouse3 = Mouse.clicked(1) # False

        for event in Events.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:  # J
                    mouse3 = True

        pass

    def loop():
        # objeto que está sob o mouse
        go_sob_mouse = None

        # for em todos os objetos pra achar o ULTIMO objeto que está sob o mouse
        for go in GameObject.all_objects:
            # Verifica se o mouse está posicionado sobre o objeto
            if go.isPointInside(Mouse.getMousePos()):
                go_sob_mouse = go

        GameManager.handleClick(go_sob_mouse)

        for go in GameObject.all_objects:
            go.loop()

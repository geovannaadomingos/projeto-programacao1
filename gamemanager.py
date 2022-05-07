import pygame
from Events import Events
from farmer import Farmer
from gameobject import GameObject
from mouse import Mouse
import time

class GameManager():
    time = 0
    lastTime = 0
    deltaTime = 0
    scale = 2
    farmer = None

    def updateTime():
        GameManager.lastTime = GameManager.time
        GameManager.time = time.time()
        GameManager.deltaTime = GameManager.time - GameManager.lastTime

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

        if GameManager.farmer != None:
            if Mouse.clicked(0):
                GameManager.farmer.moveTo(v2_mousePos)

    def loop():
        GameManager.updateTime()
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

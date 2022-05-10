from math import gamma
import pygame
import datamanager
from Events import Events
import gamemanager
from gameobject import GameObject
from item import SeedItem
from pathfinding import Pathfinding
from plantation import Plantation
from vector2 import Vector2
from wateringCan import WateringCan


class Farmer(GameObject):

    def __init__(self, v2_pos, speed, frameDuration=6):
        self.animations = datamanager.DataManager.PLAYER_ANIMATIONS
        super().__init__(v2_pos, Vector2.FromList(self.animations["idle_left"][0].get_size()), clickable=False)

        self.speed = speed
        self.v2_targetPos = None
        self.v2_direction = Vector2(0,0)
        self.arriveEvent = None

        self.frameCount = 0
        self.frameDuration = frameDuration
        self.state = "idle"

        self.inventory = [None for x in range(9)]
        self.len_itens_inventory = 0
        self.selectedInventoryIndex = 0

        self.v2_collideBox = Vector2(16,16) * (self.v2_size.x//48)
        self.v2_collideOffset = self.v2_collideBox

        self.surface = pygame.Surface(self.v2_collideBox)
        self.surface.fill((0,0,0))

        self.targetObject = None
        self.targetPath = []
        self.targetPathIndex = 0
        
    def loop(self):
        self.move()

        self.frameCount += 1
        if self.frameCount == self.frameDuration * 8:
            self.frameCount = 0

            if self.state == "enxada":
                self.arar()
            elif self.state == "regador":
                self.regar()

        for event in Events.events:
            if event.type == pygame.KEYDOWN:
                if event.key in range(49, 58):
                    self.selectedInventoryIndex = (event.key - 49)
                    print(f"({self.selectedInventoryIndex}) Item atual >: {type(self.getCurrentItem())}")


    def getCurrentItem(self):
        try:
            return self.inventory[self.selectedInventoryIndex]
        except:
            return None


    def handleClick(self, gameObject, v2_mousePos):
        if gamemanager.GameManager.grid != None:
            if type(gameObject) == Plantation:
                currentItem = self.getCurrentItem()
                if type(currentItem) == SeedItem:
                    print(type(currentItem))
                    if gameObject.canReceiveSeed():
                        self.moveTo(v2_mousePos, gameObject, self.ararAnimation)
                elif type(currentItem) == WateringCan:
                    self.moveTo(v2_mousePos, gameObject, self.regarAnimation)
            else:
                self.moveTo(v2_mousePos)

    def move(self):
        try:
            if self.state == "walking" and self.v2_targetPos != None:
                self.v2_direction = (self.targetPath[self.targetPathIndex] - self.getCenterPos())
                if self.v2_direction.magnitude() > self.speed:
                    self.v2_pos += self.v2_direction.normalize() * self.speed
                else:
                    if self.targetPath[self.targetPathIndex] == self.targetPath[-1]:
                        self.arrived()
                    else:
                        self.targetPathIndex += 1
                        self.move()
        except Exception as e:
            print(f"Error {e}")


    def arrived(self):
        self.changeState("idle")
        if self.arriveEvent != None:
            temp_event = self.arriveEvent
            self.arriveEvent = None
            temp_event()

    def draw(self, screen):
        # screen.blit(self.surface, self.v2_pos + self.v2_collideOffset)

        direction = ""
        if abs(self.v2_direction.x) > abs(self.v2_direction.y):
            if self.v2_direction.x < 0:
                direction = "left"
            else:
                direction = "right"
        else:
            if self.v2_direction.y < 0:
                direction = "up"
            else:
                direction = "down"

        screen.blit(self.animations[self.state+"_"+direction][self.frameCount // self.frameDuration], self.v2_pos)

    def changeState(self, newState):
        self.state = newState
        self.frameCount = 0

    def moveTo(self, v2_targetPos, gameObject=None, eventHandler=None):
        if v2_targetPos != None:
            nodeFarmer = gamemanager.GameManager.grid.getNodeFromPoint(self.getCenterPos())
            nodeDestino = gamemanager.GameManager.grid.getNodeFromPoint(v2_targetPos)

            if nodeFarmer == nodeDestino:
                return

            path = Pathfinding.get_path(nodeFarmer, nodeDestino, gamemanager.GameManager.grid)
            caminho = []
            if len(path) > 0:
                for node in path:
                    caminho.append(gamemanager.GameManager.grid.getNodeScreenPosCenter(node))

                self.v2_targetPos = caminho[-1]

                if gameObject != None:
                    if len(caminho) <= 2:
                        caminho = [caminho[0]]
                    else:
                        caminho = caminho[1:-1]
                else:
                    caminho = caminho[1:]

                self.targetObject = gameObject
                self.arriveEvent = eventHandler
                self.targetPath = caminho
                self.targetPathIndex = 0
                self.changeState("walking")
        else:
            self.v2_targetPos = None
            self.arriveEvent = None

    def ararAnimation(self):
        self.changeState("enxada")
        if self.v2_targetPos != None:
            self.v2_direction = (self.v2_targetPos - self.getCenterPos())
    
    def regarAnimation(self):
        self.changeState("regador")
        if self.v2_targetPos != None:
            self.v2_direction = (self.v2_targetPos - self.getCenterPos())
    
    def regar(self):
        self.changeState("idle")

    def arar(self):
        self.targetObject.receiveSeed(self.getCurrentItem())
        self.inventory[self.selectedInventoryIndex] = None
        self.len_itens_inventory -= 1
        self.changeState("idle")

    def canAddToInventory(self):
        return self.len_itens_inventory < 9

    def addToInventory(self, item):
        item.enabled = False
        for index in range(9):
            if self.inventory[index] == None:
                break
        self.len_itens_inventory += 1
        self.inventory[index] = item
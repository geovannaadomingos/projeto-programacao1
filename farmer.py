import pygame
import datamanager
from gameobject import GameObject
from vector2 import Vector2


class Farmer(GameObject):

    def __init__(self, v2_pos, speed, frameDuration=6):
        self.animations = datamanager.DataManager.PLAYER_ANIMATIONS
        super().__init__(v2_pos, Vector2.FromList(self.animations["idle_left"][0].get_size()), clickable=True)

        self.speed = speed
        self.v2_targetPos = None
        self.v2_direction = Vector2(0,0)
        self.arriveEvent = None

        self.frameCount = 0
        self.frameDuration = frameDuration
        self.state = "idle"

        self.v2_collideBox = Vector2(16,16) * (self.v2_size.x//48)
        self.v2_collideOffset = self.v2_collideBox

        self.surface = pygame.Surface(self.v2_collideBox)
        self.surface.fill((0,0,0))
        
    def loop(self):
        self.move()

        self.frameCount += 1
        if self.frameCount == self.frameDuration * 8:
            self.frameCount = 0

    def move(self):
        if self.v2_targetPos != None:
            self.v2_direction = (self.v2_targetPos - self.getCenterPos())
            if self.v2_direction.magnitude() > self.speed:
                self.v2_pos += self.v2_direction.normalize() * self.speed
            else:
                self.arrived()

    def arrived(self):
        self.changeState("idle")
        if self.arriveEvent != None:
            temp_event = self.arriveEvent
            self.arriveEvent = None
            temp_event(self)

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

    def moveTo(self, v2_targetPos, eventHandler=None):
        if v2_targetPos != None:
            self.changeState("walking")
            self.v2_targetPos = v2_targetPos
            self.arriveEvent = eventHandler
        else:
            self.v2_targetPos = None
            self.arriveEvent = None
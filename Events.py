import pygame

class Events():
    events = []

    def loop():
        Events.events = pygame.event.get()
from vector2 import Vector2
import pygame

class Mouse():
    v2_mousePos = None
    mouse_buttons_pressed = [False, False, False]
    last_mouse_events = [False, False, False]

    def setMousePos(newPos):
        Mouse.v2_mousePos = Vector2.FromList(newPos)

    def loop():
        Mouse.setMousePos(pygame.mouse.get_pos())
        mouse_events = pygame.mouse.get_pressed()

        mouse_buttons_pressed = Mouse.mouse_buttons_pressed

        for i in range(3):
            if mouse_events[i] == True:
                if mouse_buttons_pressed[i] == False and Mouse.last_mouse_events[i] == False:
                    mouse_buttons_pressed[i] = True
                else:
                    mouse_buttons_pressed[i] = False
            else:
                mouse_buttons_pressed[i] = False

        Mouse.last_mouse_events = mouse_events
        Mouse.mouse_buttons_pressed = mouse_buttons_pressed


    def clicked(index):
        return Mouse.mouse_buttons_pressed[index]

    def getMousePos():
        return Mouse.v2_mousePos
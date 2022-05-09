import pygame
import json

from gamemanager import GameManager

PREMIUM_ASSETS_FOLDER = "assets\sprites\premium_sprites"
PREMIUM_ASSETS_FOLDER_OBJECTS =  f"{PREMIUM_ASSETS_FOLDER}\objects"
PREMIUM_ASSETS_FOLDER_CHARACTERS =  f"{PREMIUM_ASSETS_FOLDER}\characters"
PREMIUM_ASSETS_FOLDER_ITEMS =  f"{PREMIUM_ASSETS_FOLDER_OBJECTS}\Items"


class DataManager():

    PLANTAS = {}
    PLAYER_ANIMATIONS = {}
    plant_sheet = None
    itens_sheet = None
    player_sheet = None

    def load():
        DataManager.loadSheets()
        DataManager.loadPlantasData()
        DataManager.loadPlayerData()

    def loadSheets():
        DataManager.plant_sheet = pygame.image.load(
            PREMIUM_ASSETS_FOLDER_OBJECTS+"\Farming Plants.png")
        DataManager.itens_sheet = pygame.image.load(
            PREMIUM_ASSETS_FOLDER_ITEMS+"\All items.png")
        DataManager.player_sheet = pygame.image.load(
            PREMIUM_ASSETS_FOLDER_CHARACTERS+"\Premium Charakter Spritesheet.png")

    def loadPlayerData():
        ordem = ["idle_down", "idle_up", "idle_left", "idle_right", "walking_down", "walking_up", "walking_right", "walking_left", "running_down", "running_up", "running_right", "running_left", "enxada_down", "enxada_up", "enxada_left", "enxada_right", "machado_down", "machado_up", "machado_left", "machado_right", "regador_down", "regador_up", "regador_left", "regador_right"]
        for index, animation in enumerate(ordem):
            list_animations = []
            for x in range(8):
                list_animations.append(DataManager.getImageFromSpriteSheet(
                    DataManager.player_sheet, frameX=x, frameY=index, width=48, height=48))
            DataManager.PLAYER_ANIMATIONS[animation] = list_animations

    def loadPlantasData():
        DataManager.PLANTAS = json.load(open("data\plants.json"))
        for index, planta in enumerate(DataManager.PLANTAS.keys()):
            DataManager.PLANTAS[planta]["item-sprite"] = DataManager.getImageFromSpriteSheet(DataManager.itens_sheet, frameX=1, frameY=index+2)
            DataManager.PLANTAS[planta]["semente-sprite"] = DataManager.getImageFromSpriteSheet(DataManager.itens_sheet, frameX=0, frameY=index+2)
            DataManager.PLANTAS[planta]["planta-sprites"] = []
            for x in range(4):
                DataManager.PLANTAS[planta]["planta-sprites"].append(DataManager.getImageFromSpriteSheet(
                    DataManager.plant_sheet, frameX=x, frameY=index+2))

    def getImageFromSpriteSheet(sheet, frameX, frameY, width=16, height=16):
        image = pygame.Surface((width, height), pygame.SRCALPHA, 32).convert_alpha()
        image.blit(sheet, (0, 0), ((frameX * width),
                   frameY * height, width, height))
        # Scale
        image = pygame.transform.scale(image, (width*GameManager.scale, height*GameManager.scale))
        return image

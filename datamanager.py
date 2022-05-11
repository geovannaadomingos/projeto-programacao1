import os
import pygame
import json
from pathlib import Path

from gamemanager import GameManager

PREMIUM_ASSETS_FOLDER = Path("assets/sprites/premium_sprites")
PREMIUM_ASSETS_FOLDER_OBJECTS = PREMIUM_ASSETS_FOLDER / "objects"
PREMIUM_ASSETS_FOLDER_CHARACTERS =  PREMIUM_ASSETS_FOLDER / "characters"
PREMIUM_ASSETS_FOLDER_ITEMS =  PREMIUM_ASSETS_FOLDER_OBJECTS / "Items"


class DataManager():

    PLANTAS = {}
    PLAYER_ANIMATIONS = {}
    OBJECTS = {}
    plant_sheet = None
    itens_sheet = None
    player_sheet = None

    def load(scale):
        DataManager.loadSheets()
        DataManager.loadPlantasData(scale)
        DataManager.loadPlayerData(scale)
        DataManager.loadObjects(scale)
        DataManager.loadItems(scale)

    def loadSheets():
        DataManager.plant_sheet = pygame.image.load(PREMIUM_ASSETS_FOLDER_OBJECTS / "Farming Plants.png")
        DataManager.itens_sheet = pygame.image.load(PREMIUM_ASSETS_FOLDER_ITEMS / "All items.png")
        DataManager.player_sheet = pygame.image.load(PREMIUM_ASSETS_FOLDER_CHARACTERS / "Premium Charakter Spritesheet.png")

    def loadPlayerData(scale):
        ordem = ["idle_down", "idle_up", "idle_left", "idle_right", "walking_down", "walking_up", "walking_right", "walking_left", "running_down", "running_up", "running_right", "running_left", "enxada_down", "enxada_up", "enxada_left", "enxada_right", "machado_down", "machado_up", "machado_left", "machado_right", "regador_down", "regador_up", "regador_left", "regador_right"]
        for index, animation in enumerate(ordem):
            list_animations = []
            for x in range(8):
                list_animations.append(DataManager.getImageFromSpriteSheet(
                    DataManager.player_sheet, frameX=x, frameY=index, width=48, height=48, scale=scale))
            DataManager.PLAYER_ANIMATIONS[animation] = list_animations

    def loadItems(scale):
        DataManager.OBJECTS["wateringCan"] = DataManager.getImageFromSpriteSheet(DataManager.itens_sheet, frameX=2, frameY=1, scale=scale)

    def loadPlantasData(scale):
        DataManager.PLANTAS = json.load(open(os.path.join("data", "plants.json")))
        for index, planta in enumerate(DataManager.PLANTAS.keys()):
            DataManager.PLANTAS[planta]["item-sprite"] = DataManager.getImageFromSpriteSheet(DataManager.itens_sheet, frameX=1, frameY=index+2, scale=scale)
            DataManager.PLANTAS[planta]["semente-sprite"] = DataManager.getImageFromSpriteSheet(DataManager.itens_sheet, frameX=0, frameY=index+2, scale=scale)
            DataManager.PLANTAS[planta]["planta-sprites"] = []
            for x in range(4):
                DataManager.PLANTAS[planta]["planta-sprites"].append(DataManager.getImageFromSpriteSheet(
                    DataManager.plant_sheet, frameX=x, frameY=index+2, scale=scale))

    def loadObjects(scale):
        DataManager.OBJECTS["waterWell"] = DataManager.scaleImage(pygame.image.load(PREMIUM_ASSETS_FOLDER_OBJECTS / 'Water well.png') ,scale)

    def getImageFromSpriteSheet(sheet, frameX, frameY, width=16, height=16, scale=1):
        image = pygame.Surface((width, height), pygame.SRCALPHA, 32).convert_alpha()
        image.blit(sheet, (0, 0), ((frameX * width),
                   frameY * height, width, height))
        
        return DataManager.scaleImage(image, scale)

    def scaleImage(image, scale):
        if scale == 1:
            return image
        else:
            width,height = image.get_size()
            return pygame.transform.scale(image, (width*scale, height*scale))

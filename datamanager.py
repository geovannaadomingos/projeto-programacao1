import pygame
import json

PREMIUM_ASSETS_OBJECTS_FOLDER = "assets\sprites\premium_sprites\objects"


class DataManager():

    PLANTAS = {}
    sheet = None

    def load():
        DataManager.loadSheets()
        DataManager.loadPlantasData()

    def loadSheets():
        DataManager.plant_sheet = pygame.image.load(
            PREMIUM_ASSETS_OBJECTS_FOLDER+"\Farming Plants.png")
        DataManager.itens_sheet = pygame.image.load(
            PREMIUM_ASSETS_OBJECTS_FOLDER+"\Items\All items.png")

    def loadPlantasData():
        DataManager.PLANTAS = json.load(open("data\plants.json"))
        for index, planta in enumerate(DataManager.PLANTAS.keys()):
            DataManager.PLANTAS[planta]["semente-sprite"] = DataManager.getImageFromSpriteSheet(DataManager.itens_sheet, frameX=0, frameY=index+2)
            DataManager.PLANTAS[planta]["planta-sprites"] = []
            for x in range(4):
                DataManager.PLANTAS[planta]["planta-sprites"].append(DataManager.getImageFromSpriteSheet(
                    DataManager.plant_sheet, frameX=x, frameY=index+2))

    def getImageFromSpriteSheet(sheet, frameX, frameY, width=16, height=16):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0, 0), ((frameX * width),
                   frameY * height, width, height))
        return image

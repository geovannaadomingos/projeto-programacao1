import json
import os

class Report():
    level = 0
    levels = json.load(open(os.path.join("data", "levels.json")))
    usedSeeds = 0
    usedWateringCan = 0
    currentHarvest = {
        "Cenoura": 0,
        "Repolho": 0,
        "Goiaba": 0,
        "Berinjela": 0,
        "Azulzinha": 0,
        "Alface": 0,
        "Trigo": 0,
        "Abobora": 0,
        "Nabo": 0,
        "Rosinha": 0,
        "Beterraba": 0,
        "Estrelinha": 0,
        "Pepino": 0
    }

    def harvestReport(plantName):
        # relata plantas colhidas(coletadas)
        Report.currentHarvest[plantName] += 1

        if Report.checkGoal():
            print("Ganhei o level")

    def usedSeedsReport():
        # relata sementes utilizadas(coletadas)
        Report.usedSeeds += 1

    def getCurrentHarvestGoal():
        return Report.levels[str(Report.level)]["harvestGoal"]

    def usedWateringCanReport():
        # relata quantas vezes o regador foi coletado
        Report.usedWateringCan += 1

    def checkGoal():
        # verfica se a colheita atual atingiu a meta do level
        goal = Report.getCurrentHarvestGoal()

        for i in Report.currentHarvest:
            # retorna o valor de colheita de cada planta
            if Report.currentHarvest[i] < goal[i]:
                return False
        return True

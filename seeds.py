from datamanager import DataManager


class Seed():
    def __init__(self, name):
        self.name = name
        self.data = DataManager.PLANTAS.get(name, None)
        self.tempo_colher = self.data["time_to_grow_sec"]
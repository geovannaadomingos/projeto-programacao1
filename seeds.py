from datamanager import DataManager


class Seed():
    def __init__(self, name):
        self.name = name
        self.data = DataManager.PLANTAS.get(name, default=None)
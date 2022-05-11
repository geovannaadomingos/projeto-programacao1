import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from game import Game
import datamanager

if __name__ == "__main__":

    g = Game() #OBG DONJOGOA
    datamanager.DataManager.load(2)

    while g.running:
        g.curr_menu.display_menu()
        g.game_loop()


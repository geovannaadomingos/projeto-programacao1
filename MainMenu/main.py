from game import Game

g = Game() #OBG DONJOGOA

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
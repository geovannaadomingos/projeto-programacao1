import pygame

class Sounds():
    SoundsFolder = "assets\\Sounds\\"

    def playSFX(musicName):
        playSE = pygame.mixer.Sound(Sounds.SoundsFolder+musicName)
        pygame.mixer.music.set_volume(0.5)
        playSE.play()

    def backgroundMusic():
        background_music = pygame.mixer.music.load(Sounds.SoundsFolder+'bg music.mp3')
        pygame.mixer.music.play(-1)

#Som que faz qdo plantar algo
#Som que faz qdo regar
#Som que faz ao coletar o objeto
#Som que faz ao se mover no cenário
#Som planta nascendo
#Som planta pronta para ser colhida
#coisas que faltam fazer no codigo: - "mergir" com o menu de gio para que consiga ajeitar o volume!
#Background Music 
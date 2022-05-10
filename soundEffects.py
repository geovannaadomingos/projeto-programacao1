import pygame

class Sounds():
#coisas que faltam fazer no codigo: - "mergir" com o menu de gio para que consiga ajeitar o volume!
#  
#Background Music
    def backgroundMusic():
        background_music = pygame.mixer.music.load('mixkit-zanarkand-forest-169.mp3')
        pygame.mixer.music.play(-1)

#Som que faz qdo plantar algo
    def plantSmthSound():
        plant_SE = pygame.mixer.Sound('som terra.wav')
        plant_SE.play()

#Som que faz qdo regar
    def waterSound():
        water_SE = pygame.mixer.Sound('mixkit-sea-water-splash-1198.wav')
        water_SE.play()

#Som que faz ao coletar o objeto
    def colectSmthSound():
        colect_SE = pygame.mixer.Sound('pass.wav')
        colect_SE.play()

#Som que faz ao se mover no cenário
    def footstepsSound():
        walk_SE = pygame.mixer.Sound('mixkit-footsteps-in-woods-loop-533.wav')
        walk_SE.play()

#Som planta nascendo
    def plantGrow():
        grow_SE = pygame.mixer.Sound('pass.wav')
        grow_SE.play()

#Som planta pronta para ser colhida
    def plantReady():
        ready_SE = pygame.mixer.Sound('pass.wav')
        ready_SE.play()
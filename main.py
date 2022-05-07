import pygame

def main():
    pygame.init()
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("Projetinho P1")

    FPS = 30
    clock = pygame.time.Clock()

    # Screen
    SCREEN_W = 400
    SCREEN_H = 400
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        pygame.display.update()


if __name__ == "__main__":
    main()

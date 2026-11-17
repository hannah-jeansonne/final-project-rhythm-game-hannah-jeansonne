import pygame

class Key():
    def __init__(self, x, y, color1, color2, key):
        self.pos = (x, y)
        self.color1 = color1
        self.color2 = color2
        self.key = key

    def draw(self, surface):
        pygame.draw.circle(surface, self.color1, self.pos, 75)
        



def main ():
    pygame.init()
    pygame.display.set_caption("Rhythm Game")
    #clock
    #dt
    resolution = (1920, 1080)
    screen = pygame.display.set_mode(resolution)
    pygame.FULLSCREEN
    keys = [Key(660, 950, (178, 30, 232), (0 ,0 ,0), pygame.K_a),
            Key(860, 950, (43, 34, 214), (0, 0, 0), pygame.K_s),
            Key(1060, 950, (27, 191, 224), (0, 0, 0), pygame.K_k),
            Key(1260, 950, (14, 201, 105), (0, 0, 0), pygame.K_l)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        for key in keys:
            key.draw(screen)
            pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
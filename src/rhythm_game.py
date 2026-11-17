import pygame
from pygame import mixer

class Key():
    def __init__(self, x, y, color1, color2, key):
        self.pos = (x, y)
        self.color1 = color1
        self.color2 = color2
        self.key = key

    def draw(self, surface, color):
        if color == 1:
            pygame.draw.circle(surface, self.color1, self.pos, 75)
        if color == 2:
            pygame.draw.circle(surface, self.color2, self.pos, 75)
        



def main ():
    pygame.init()
    mixer.init()
    mixer.music.load('speed_lvl.mp3')
    mixer.music.play()
    pygame.display.set_caption("Rhythm Game")
    #clock
    #dt
    resolution = (1920, 1080)
    screen = pygame.display.set_mode(resolution)
    pygame.FULLSCREEN
    keys = [Key(660, 950, (178, 30, 232), (139, 73, 163), pygame.K_a),
            Key(860, 950, (43, 34, 214), (73, 69, 163), pygame.K_s),
            Key(1060, 950, (27, 191, 224), (67, 145, 161), pygame.K_k),
            Key(1260, 950, (14, 201, 105), (60, 150, 104), pygame.K_l)]
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        k = pygame.key.get_pressed()
        for key in keys:
            if k[key.key]:
                key.draw(screen, 1)
            if not k[key.key]:
                key.draw(screen, 2)
            pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
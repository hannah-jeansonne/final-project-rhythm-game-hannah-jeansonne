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

class Track():
    def __init__(self, x, y, color, key):
        self.pos = (x, y)
        self.color = color
        self.key = key
        

def load(map, keys, surface):
    beats = []
    mixer.music.load(map + ".mp3")
    mixer.music.play()
    f = open(map + ".txt", 'r')
    data = f.readlines()
    lane_centers = [660, 860, 1060, 1260]
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '0':
                beats.append((lane_centers[x], 0))
    return beats

        

def main ():
    pygame.init()
    mixer.init()
    pygame.display.set_caption("Rhythm Game")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (1920, 1080)
    screen = pygame.display.set_mode(resolution)
    pygame.FULLSCREEN
    keys = [Key(660, 950, (178, 30, 232), (139, 73, 163), pygame.K_a),
            Key(860, 950, (43, 34, 214), (73, 69, 163), pygame.K_s),
            Key(1060, 950, (27, 191, 224), (67, 145, 161), pygame.K_k),
            Key(1260, 950, (14, 201, 105), (60, 150, 104), pygame.K_l)]
    running = True
    map_beats = load("speed_lvl", keys, screen)
    while running:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        k = pygame.key.get_pressed()
        screen.fill((0, 0, 0))
        for key in keys:
            if k[key.key]:
                key.draw(screen, 1)
            if not k[key.key]:
                key.draw(screen, 2)
            
        for beat in map_beats:
            x, y = beat
            pygame.draw.circle(screen, (200,0,0), (x,y), 50)
            y += 10
        pygame.display.flip()
        dt = clock.tick(12)
        
    pygame.quit()


if __name__ == "__main__":
    main()
import pygame
from pygame.transform import scale
from settings import *
from player import Player
import math
from map import world_map
from ray_casting import ray_casting

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

# assigning values to X and Y variable
X = 400
Y = 400

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)
texture_img = pygame.image.load('images/brickwall2.jpg').convert()
fps = FPS // 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement(fps)

    pygame.draw.rect(sc, BLUE, (0, 0, WIDTH, HALF_HEIGHT))
    pygame.draw.rect(sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    x_, y_, rects_to_draw = ray_casting(player.pos, player.angle, world_map)
    for rect in rects_to_draw:
        x0, y0, height, offset = rect
        wall_column = texture_img.subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
        wall_column = scale(wall_column, (SCALE, height))
        sc.blit(wall_column, (x0, y0))

    pygame.draw.circle(sc, GREEN, (int(player.x), int(player.y)), 12)
    if x_ and y_:
        pygame.draw.circle(sc, RED, (int(x_), int(y_)), 6)
    pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
                                             player.y + WIDTH * math. sin(player.angle)), 2)
    for x,y in world_map:
        pygame.draw.rect(sc, BLACK, (x, y, TILE, TILE), 2)

    fps = clock.get_fps()
    text = font.render(str(round(fps)), True, WHITE, BLUE)
    sc.blit(text, (50, 20))
    pygame.display.update()
    clock.tick(FPS)

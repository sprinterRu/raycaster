from settings import *
from numba.typed import List
from numba import njit
from geometry import rect_circle_intersect

text_map = [
    'WWWWWWWWWWWW',
    'W......W...W',
    'W..WWW...W.W',
    'W....W..WW.W',
    'W..W....W..W',
    'W..W...WWW.W',
    'W....W.....W',
    'WWWWWWWWWWWW'
]

world_map = List()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.append((i * TILE, j * TILE))


@njit(cache=True)
def collision_detected(new_x, new_y, objects):
    for x, y in objects:
        if rect_circle_intersect(x, y, new_x, new_y, COLLISION_SPHERE_RADIUS):
            return True
    return False

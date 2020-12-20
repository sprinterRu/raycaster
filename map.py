from settings import *
from numba.typed import List
from numba import njit

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
def collision_detected(old_x, old_y, new_x, new_y, objects):
    sx = new_x + COLLISION_SPHERE_RADIUS * (new_x - old_x)
    sy = new_y + COLLISION_SPHERE_RADIUS * (new_y - old_y)
    for x, y in objects:
        if x <= sx <= x + TILE and y <= sy <= y + TILE:
            return True
    return False

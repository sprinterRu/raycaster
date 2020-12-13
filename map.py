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
def collision_detected(tmp_x, tmp_y, objects):
    for x, y in objects:
        if x <= tmp_x <= x + TILE and y <= tmp_y <= y + TILE:
            return True
    return False

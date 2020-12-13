from settings import *
from geometry import ray_intersects_rectangle
from numba import njit, prange
from numba.typed import List
from math import cos, sin


@njit(fastmath=True)
def ray_casting(player_pos, player_angle: float, objects: List):
    start_angle = player_angle - HALF_FOV
    x0, y0 = player_pos
    min_x = None
    min_y = None
    objects_in_fov = get_objects_in_fov(x0, y0, player_angle, objects)

    rects = []
    for ray in prange(NUM_RAYS):
        cur_angle = start_angle + ray * DELTA_ANGLE
        cos_a, sin_a = cos(cur_angle), sin(cur_angle)
        min_depth = 999999999

        for x, y, dst in objects_in_fov:
            if dst < min_depth + 90000:
                x_i, y_i, d = ray_intersects_rectangle(x0, y0, x, y, cos_a, sin_a, min_depth)
                if d < min_depth:
                    min_depth = d
                    if ray == NUM_RAYS_HALF:
                        min_x = x_i
                        min_y = y_i

        proj_height = min(PROJ_COEFF / (math.sqrt(min_depth) + 0.0001), HEIGHT)
        c = 255 / (1 + min_depth * 0.0001)
        color = (c // 2, c, c // 3)
        rects.append((color,  (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height)))

    return min_x, min_y, rects


@njit(fastmath=True)
def get_objects_in_fov(x0, y0, angle, objects):
    n_x = math.cos(angle)
    n_y = math.sin(angle)

    b = -(x0 * n_x + y0 * n_y)
    l = List()

    for x, y in objects:
        # determine coordinates of the closest corner to the player
        xt = x if n_x < 0 else x + TILE
        yt = y if n_y < 0 else y + TILE
        d = xt * n_x + yt * n_y + b
        if d >= 0:
            dst = (x - x0) ** 2 + (y - y0) ** 2
            l.append((x, y, dst))

    return sorted(l, key=lambda x: x[2])

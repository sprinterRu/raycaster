from numba import njit
from settings import *


@njit(fastmath=True, cache=True)
def ray_intersects_rectangle_old(x0, y0, k, b, x_rect, y_rect, cos, sin, min_depth):
    dist_min = min_depth
    x_min = None
    y_min = None

    # check intersection with vertical edge
    # if we're on the left then check only leftmost edge
    x_rect_end = x_rect + TILE
    x = x_rect if x0 < x_rect or (x0 < x_rect_end and cos < 0) else x_rect_end
    y = k * x + b
    h = x - x0
    v = y - y0
    if y_rect < y <= y_rect + TILE and (h * cos + v * sin) > 0:  # found an intersection with a box
        d = h * h + v * v
        if d < dist_min:
            x_min = x
            y_min = y
            dist_min = d

    # check intersection with horizontal edge
    # if we're on the bottom then check only bottommost edge
    y_rect_end = y_rect + TILE
    y = y_rect if y0 < y_rect or (y0 < y_rect_end and sin < 0) else y_rect + TILE
    x = (y - b) / k
    h = x - x0
    v = y - y0
    if x_rect < x <= x_rect + TILE and (h * cos + v * sin) > 0:  # found an intersection with a box
        d = h * h + v * v
        if d < dist_min:
            x_min = x
            y_min = y
            dist_min = d

    return x_min, y_min, dist_min


@njit(fastmath=True, cache=True)
def ray_intersects_rectangle(x0, y0, x_rect, y_rect, cos, sin, min_depth):
    dist_min = min_depth
    x_min = None
    y_min = None
    x_rect_end = x_rect + TILE
    y_rect_end = y_rect + TILE

    # check intersection with vertical edge
    # if we're on the left then check only leftmost edge
    if cos != 0.0:
        x = x_rect if x0 < x_rect or (x0 < x_rect_end and cos < 0) else x_rect_end
        t = (x - x0) / cos
        y = y0 + t * sin
        if y_rect < y <= y_rect_end and t > 0:  # found an intersection with a box
            d = (y - y0)**2 + (x - x0)**2
            if d < dist_min:
                x_min = x
                y_min = y
                dist_min = d

    # check intersection with horizontal edge
    # if we're on the bottom then check only bottommost edge
    if sin != 0.0:
        y = y_rect if y0 < y_rect or (y0 < y_rect_end and sin < 0) else y_rect + TILE
        t = (y - y0) / sin
        x = x0 + t * cos
        if x_rect < x <= x_rect_end and t > 0:  # found an intersection with a box
            d = (y - y0)**2 + (x - x0)**2
            if d < dist_min:
                x_min = x
                y_min = y
                dist_min = d

    return x_min, y_min, dist_min


@njit(fastmath=True, cache=True)
def rect_circle_intersect(x_rect, y_rect, x_circle, y_circle, r) -> bool:
    # check intersection with horizontal edges
    if x_rect <= x_circle <= x_rect + TILE:
        if abs(y_rect - y_circle) <= r or abs(y_rect + TILE - y_circle) <= r:
            return True

    # check intersection with vertical edges
    if y_rect <= y_circle <= y_rect + TILE:
        if abs(x_rect - x_circle) <= r or abs(x_rect + TILE - x_circle) <= r:
            return True

    r_sq = COLLISION_SPHERE_RADIUS_SQUARED
    if (x_rect - x_circle) ** 2 + (y_rect - y_circle) ** 2 <= r_sq:
        return True
    if (x_rect + TILE - x_circle) ** 2 + (y_rect - y_circle) ** 2 <= r_sq:
        return True
    if (x_rect + TILE - x_circle) ** 2 + (y_rect + TILE - y_circle) ** 2 <= r_sq:
        return True
    if (x_rect - x_circle) ** 2 + (y_rect + TILE - y_circle) ** 2 <= r_sq:
        return True

    return False

import math

# game settings
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 100
TILE = 100

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
NUM_RAYS_HALF = NUM_RAYS / 2
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 2 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# player settings
player_pos = (HALF_WIDTH + TILE // 2, HALF_HEIGHT + TILE // 2)
player_angle = 3 * math.pi / 2 - math.pi / 4
player_speed = 100

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)

# texture settings
TEXTURE_WIDTH = 256
TEXTURE_HEIGHT = 256
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# physics settings
COLLISION_SPHERE_RADIUS = 20
COLLISION_SPHERE_RADIUS_SQUARED = 400
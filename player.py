from settings import *
import pygame
import math
from map import collision_detected, world_map


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self, fps):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        tmp_x = self.x
        tmp_y = self.y
        speed = player_speed / (fps + 1)
        if keys[pygame.K_w]:
            tmp_x += speed * cos_a
            tmp_y += speed * sin_a
        if keys[pygame.K_s]:
            tmp_x += -speed * cos_a
            tmp_y += -speed * sin_a
        if keys[pygame.K_a]:
            tmp_x += speed * sin_a
            tmp_y += -speed * cos_a
        if keys[pygame.K_d]:
            tmp_x += -speed * sin_a
            tmp_y += speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
        if not collision_detected(tmp_x, tmp_y, world_map):
            self.x = tmp_x
            self.y = tmp_y
        elif not collision_detected(self.x, tmp_y, world_map):
            self.y = tmp_y
        elif not collision_detected(tmp_x, self.y, world_map):
            self.x = tmp_x

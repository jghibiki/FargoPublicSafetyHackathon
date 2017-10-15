import math

import pygame

from drawable import Drawable

import config

class ROAD_DIRECTION:
    north = 1
    south = 2
    east = 3
    west = 4

class Road(Drawable):

    def __init__(self, x, y, direction):
        if direction == ROAD_DIRECTION.north or direction == ROAD_DIRECTION.south:
            Drawable.__init__(self, config.block_size + (2*config.road_size), config.road_size)

        else:
            Drawable.__init__(self, config.road_size, config.block_size + (2*config.road_size) )

        self.direction = direction
        self.x = x
        self.y = y

        self.color = pygame.Color("#4A4A4A")

    def update(self):
        return False


    def render(self):
        self.surf.fill(self.color)

    def draw(self, parent_surf):
        if self.direction == ROAD_DIRECTION.north:
            parent_surf.blit(self.surf, (
                 self.x * config.grid_offset,
                 self.y * config.grid_offset))

        if self.direction == ROAD_DIRECTION.south:
            parent_surf.blit(self.surf, (
                 self.x * config.grid_offset,
                 self.y * config.grid_offset + config.grid_offset))


        if self.direction == ROAD_DIRECTION.west:
            parent_surf.blit(self.surf, (
                 self.x * config.grid_offset,
                 self.y * config.grid_offset))

        if self.direction == ROAD_DIRECTION.east:
            parent_surf.blit(self.surf, (
                 self.x * config.grid_offset + config.grid_offset,
                 self.y * config.grid_offset))


class NorthRoad(Road):
    def __init__(self, x, y):
        Road.__init__(self, x, y, ROAD_DIRECTION.north)

class SouthRoad(Road):
    def __init__(self, x, y):
        Road.__init__(self, x, y, ROAD_DIRECTION.south)

class WestRoad(Road):
    def __init__(self, x, y):
        Road.__init__(self, x, y, ROAD_DIRECTION.west)

class EastRoad(Road):
    def __init__(self, x, y):
        Road.__init__(self, x, y, ROAD_DIRECTION.east)



import pygame

from drawable import Drawable
import config

class CityBlock(Drawable):

    def __init__(self, x, y, width=1, height=1, color="#5C5C5C"):
        Drawable.__init__(self, width * config.block_size, height * config.block_size)
        self.x = x
        self.y = y

        self.offset_x = self.__calculate_offset_coord(x)
        self.offset_y = self.__calculate_offset_coord(y)

        self.color = pygame.Color(color)

    def update(self):
        pass

    def render(self):
        self.surf.fill(self.color)

    def draw(self, parent_surf):
        return parent_surf.blit(self.surf, (self.offset_x, self.offset_y))


    def __calculate_offset_coord(self, coord):
        return (config.block_size * coord) + ((coord+1) * config.road_size)

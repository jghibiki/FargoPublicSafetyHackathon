import math
import pygame
import pygame.gfxdraw

from drawable import Drawable
import config


class Grid(Drawable):

    def __init__(self):
        w, h = config.grid_offset * config.map_size[0] + config.road_size*2, config.grid_offset * config.map_size[1] + config.road_size*2
        Drawable.__init__(self, w, h)

        self.color = pygame.Color("#141414")

    def update(self):
        pass

    def render(self):
        self.surf.fill(pygame.Color(0, 0, 0, 0))

        lines_wide = config.map_size[0] + 1
        for i in range(lines_wide):
            pygame.gfxdraw.vline(self.surf, i*config.block_size + (i+1)*config.road_size, 0, config.grid_offset * config.map_size[1] + config.road_size, self.color)
            pygame.gfxdraw.vline(self.surf, i*config.block_size + (i)*config.road_size, 0, config.grid_offset * config.map_size[1] + config.road_size, self.color)

        lines_high = config.map_size[1] + 1
        for i in range(lines_high):
            pygame.gfxdraw.hline(self.surf, 0, config.grid_offset * config.map_size[0] + config.road_size, i*config.block_size + (i+1)*config.road_size, self.color)
            pygame.gfxdraw.hline(self.surf, 0, config.grid_offset * config.map_size[0] + config.road_size, i*config.block_size + (i)*config.road_size, self.color)

    def draw(self, parent_surf):
        return parent_surf.blit(self.surf, (0, 0))

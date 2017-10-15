import pygame

from drawable import Drawable

import config

class Incident(Drawable):

    def __init__(self, x, y, metadata):
        Drawable.__init__(self, config.block_size, config.block_size)

        self.x = x
        self.y = y

        self.draw_priority = 2

        self.offset_x = self.__calculate_offset_coord(x)
        self.offset_y = self.__calculate_offset_coord(y)


        self.id = metadata["id"]
        self.description = metadata["description"]
        self.call_time = metadata["callTime"]
        self.leave_time = metadata["leaveTime"]
        self.travel_time = metadata["travelTime"]
        self.event_time = metadata["eventTime"]

        self.color = pygame.Color("#FFD900")


    def update(self):
        return False

    def render(self):

        sub_surf = pygame.Surface((config.block_size, config.block_size), pygame.SRCALPHA)
        sub_surf.fill(self.color)

        sub_surf = pygame.transform.rotate(sub_surf, 45)

        sub_surf = pygame.transform.smoothscale(sub_surf, (config.block_size, config.block_size))

        self.surf.blit(sub_surf, (0, 0))


    def draw(self, parent_surf):
        parent_surf.blit(self.surf, (self.offset_x, self.offset_y))

    def __calculate_offset_coord(self, coord):
        return (config.block_size * coord) + ((coord+1) * config.road_size)


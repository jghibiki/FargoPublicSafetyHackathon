import pygame

from city_block import CityBlock


class FireStation(CityBlock):

    def __init__(self, x, y):
        CityBlock.__init__(self, x, y)

        self.color = pygame.Color("#FF0000")

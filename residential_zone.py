import pygame

from city_block import CityBlock


class ResidentialZone(CityBlock):

    def __init__(self, x, y):
        CityBlock.__init__(self, x, y)

        self.color = pygame.Color("#229E00")



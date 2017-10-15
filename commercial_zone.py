import pygame

from city_block import CityBlock


class CommercialZone(CityBlock):

    def __init__(self, x, y):
        CityBlock.__init__(self, x, y)

        self.color = pygame.Color("#00719E")



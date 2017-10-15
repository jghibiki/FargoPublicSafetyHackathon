import pygame

from city_block import CityBlock


class IndustrialZone(CityBlock):

    def __init__(self, x, y):
        CityBlock.__init__(self, x, y, color="#9E2D00")



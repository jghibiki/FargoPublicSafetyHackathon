import pygame

from city_block import CityBlock


class FireStation(CityBlock):

    def __init__(self, x, y):
        CityBlock.__init__(self, x, y, color="#FF3D3D")


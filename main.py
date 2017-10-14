
import pygame
from pygame.locals import *

from city_block import CityBlock
from grid import Grid

import config

pygame.init()
clock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode(config.window_size)
pygame.display.set_caption("Slim Jitty Citty")

windowSurfaceObj.fill(pygame.Color("#FFFFFF"))

city_blocks = [
        CityBlock(0, 0, 1, 1),
        CityBlock(1, 1, 1, 1),
        CityBlock(1, 2, 1, 1),
        CityBlock(2, 3, 1, 1)
]

grid = Grid()


def quit():
    pygame.quit()
    exit()

def start():

    while True:


        grid.render()
        grid.draw(windowSurfaceObj)

        for obj in city_blocks:
            obj.update()

        for obj in city_blocks:
            obj._render()

        for obj in city_blocks:
            obj.draw(windowSurfaceObj)

        # event loop
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":

    start()

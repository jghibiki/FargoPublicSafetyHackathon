
import pygame
from pygame.locals import *

import config

pygame.init()
clock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode(config.window_size)
pygame.display.set_caption("Slim Jitty Citty")


def quit():
    pygame.quit()
    exit()

def start():

    while True:

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

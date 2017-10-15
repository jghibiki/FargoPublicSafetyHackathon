
import pygame
from pygame.locals import *

import config

from viewport import Viewport
from hud import Hud

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode(config.window_size)
pygame.display.set_caption("Slim Jitty Citty")

vp = Viewport()
hud = Hud()


def quit():
    pygame.quit()
    exit()

def start():

    while True:

        windowSurfaceObj.fill(pygame.Color("#000000"))

        vp.update()
        hud.update()

        vp._render()
        hud._render()

        vp._draw(windowSurfaceObj)
        hud._draw(windowSurfaceObj)

        # event loop
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()

            vp.handle_event(event)
            hud.handle_event(event)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":

    start()

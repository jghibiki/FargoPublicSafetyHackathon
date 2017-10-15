
import pygame
from pygame.locals import *

import config

from viewport import Viewport
from hud import Hud
from simulation_controller import sim_control

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

infoObject = pygame.display.Info()
if config.native_size:
    config.window_size = (infoObject.current_w, infoObject.current_h)
    windowSurfaceObj = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
else:
    windowSurfaceObj = pygame.display.set_mode(config.window_size)
pygame.display.set_caption("Slim Shi'-T Starring Aenemaeub")

vp = Viewport()
hud = Hud()

sim_control.set_viewport(vp)


def quit():
    pygame.quit()
    exit()

def start():

    while True:

        windowSurfaceObj.fill(pygame.Color("#000000"))

        sim_control.simulation_step()

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

            suppress = vp.handle_event(event)
            if not suppress:
                suppress = hud.handle_event(event)
            if not suppress:
                suppress = sim_control.handle_event(event)


        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":

    start()

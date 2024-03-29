import pygame
from pygame.locals import *

from drawable import Drawable
from eventable import Eventable

from grid import Grid
from simulation_controller import sim_control

import config

class Viewport(Drawable, Eventable):
    def __init__(self):
        w = config.grid_offset * config.map_size[0] + config.road_size*2
        h = config.grid_offset * config.map_size[1] + config.road_size*2
        Drawable.__init__(self, w, h)

        self.v_x = 0
        self.v_y = 0

        self.drag = False
        self.mouse_offset_x = 0
        self.mouse_offset_y = 0

        self.child_update = False

        self.children = [
            Grid(),
            sim_control
        ]

        self.dirty = 2

    def update(self):
        for obj in self.children:
            self.child_update = obj.update() or self.child_update

    def render(self):
        for obj in self.children:
            if self.child_update:
                obj.render() # force render
            else:
                obj._render()


    def draw(self, parent_surf):
        if self.child_update:
            self.surf.fill(pygame.Color(0, 0, 0, 0))

        for obj in self.children:
            if self.child_update:
                obj.draw(self.surf) # force draw
            else:
                obj._draw(self.surf)

        self.child_update = False
        parent_surf.blit(self.surf, (self.v_x, self.v_y))

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button is 3:
            self.drag = True

            mouse_x, mouse_y = event.pos
            self.mouse_offset_x = self.v_x - mouse_x
            self.mouse_offset_y = self.v_y - mouse_y

            return True

        elif event.type == MOUSEBUTTONUP and event.button is 3:
            self.drag = False
            return True

        elif self.drag and event.type == MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            self.v_x = mouse_x + self.mouse_offset_x
            self.v_y = mouse_y + self.mouse_offset_y

            if self.v_x > config.scroll_padding:
                self.v_x = config.scroll_padding

            elif self.v_x < -(self.w + config.scroll_padding - config.window_size[0]):
                self.v_x =  -(self.w + config.scroll_padding - config.window_size[0])

            if self.v_y > config.scroll_padding:
                self.v_y = config.scroll_padding

            elif self.v_y < -(self.h + config.scroll_padding - config.window_size[1]):
                self.v_y = - (self.h + config.scroll_padding - config.window_size[1])

            return True

        else:
            for c in self.children:
                if isinstance(c, Eventable):
                    if c.handle_event(event):
                        return True

        return False

    def project_coord_into_vp(self, coords):
        return ( coords[0] - self.v_x, coords[1] - self.v_y )





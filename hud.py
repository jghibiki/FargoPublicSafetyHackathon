import pygame
from pygame.locals import *

from drawable import Drawable
from eventable import Eventable
from simulation_controller import HUD_MODE, sim_control

import config


class ModeSwitchPanel(Drawable, Eventable):

    def __init__(self):
        Drawable.__init__(self, 200, 50)

        self.font = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.bg_color = pygame.Color("#242424")
        self.button_color = pygame.Color("#3B3B3B")
        self.button_color_alt = pygame.Color("#474747")
        self.fg_color = pygame.Color("#616161")

        self.button_build_hotzone = None
        self.button_run_hotzone = None

    def update(self):
        pass

    def render(self):
        self.surf.fill(self.bg_color)


        print(sim_control.mode)

        # draw build text
        padding = 15
        coords = (15, 6)
        text_surf = self.font.render("BUILD", True, self.fg_color)
        text_surf_rect = text_surf.get_rect()
        if sim_control.mode == HUD_MODE.build:
            self.surf.fill(self.button_color_alt, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        else:
            self.surf.fill(self.button_color, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        self.surf.blit(text_surf, (coords[0] + padding, coords[1] + padding/2))

        self.button_build_hotzone = pygame.Rect(
                (config.window_size[0] - self.w) + coords[0],
                coords[1],
                text_surf_rect.w + padding*2,
                text_surf_rect.h + padding)

        # draw run text
        padding = 15
        coords = (115, 6)
        text_surf = self.font.render("RUN", True, self.fg_color)
        text_surf_rect = text_surf.get_rect()
        if sim_control.mode == HUD_MODE.run:
            self.surf.fill(self.button_color_alt, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        else:
            self.surf.fill(self.button_color, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        self.surf.blit(text_surf, (coords[0] + padding, coords[1] + padding/2))

        self.button_run_hotzone = pygame.Rect(
                (config.window_size[0] - self.w) + coords[0],
                coords[1],
                text_surf_rect.w + padding*2,
                text_surf_rect.h + padding)

    def draw(self, parent_surf):
        parent_surf.blit(self.surf, (config.window_size[0] - self.w, 0))

    def handle_event(self, event):

        if event.type ==  MOUSEBUTTONDOWN and event.button is 1 and self.button_build_hotzone.collidepoint(event.pos):
            print("build")
            sim_control.set_mode(HUD_MODE.build)
            self.dirty = 1

        elif event.type == MOUSEBUTTONDOWN and event.button is 1 and self.button_run_hotzone.collidepoint(event.pos):
            print("run")
            sim_control.set_mode(HUD_MODE.run)
            self.dirty = 1



class Hud(Drawable, Eventable):

    def __init__(self):
        Drawable.__init__(self, *config.window_size)
        Eventable.__init__(self)

        self.children = [
            ModeSwitchPanel()
        ]

        self.dirty = 2


    def update(self):
        for obj in self.children:
            obj.update()


    def render(self):
        for obj in self.children:
            obj._render()


    def draw(self, parent_surf):
        for obj in self.children:
            obj._draw(self.surf)

        parent_surf.blit(self.surf, (0, 0))


    def handle_event(self, event):
        for obj in self.children:
            obj.handle_event(event)


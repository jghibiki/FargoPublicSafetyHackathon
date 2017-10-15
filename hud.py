import pygame
from pygame.locals import *

from drawable import Drawable
from eventable import Eventable
from simulation_controller import HUD_MODE, PLAYBACK_MODE, BUILD_MODE, sim_control

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

        sim_control.register_watcher("hud_mode_change", self)

        self.panel_mask = pygame.Rect(config.window_size[0] - self.w, 0, self.w, self.h)

    def update(self):
        pass

    def render(self):
        self.surf.fill(self.bg_color)


        # draw build text
        padding = 15
        coords = (15, 6)
        text_surf = self.font.render("BUILD", True, self.fg_color)
        text_surf_rect = text_surf.get_rect()
        if sim_control.hud_mode == HUD_MODE.build:
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
        if sim_control.hud_mode == HUD_MODE.run:
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

        if event.type ==  MOUSEBUTTONDOWN and event.button is 1:
            if self.button_build_hotzone.collidepoint(event.pos):
                sim_control.set_hud_mode(HUD_MODE.build)
                self.dirty = 1
                return True

            elif self.button_run_hotzone.collidepoint(event.pos):
                sim_control.set_hud_mode(HUD_MODE.run)
                self.dirty = 1
                return True

            elif self.panel_mask.collidepoint(event.pos):
                return True

        return False


class PlaybackControlPanel(Drawable, Eventable):

    def __init__(self):
        Drawable.__init__(self, 355, 50)

        self.font = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.bg_color = pygame.Color("#242424")
        self.button_color = pygame.Color("#3B3B3B")
        self.button_color_alt = pygame.Color("#474747")
        self.fg_color = pygame.Color("#616161")

        self.button_play_hotzone = None
        self.button_pause_hotzone = None
        self.button_play_x2_hotzone = None

        self.panel_mask = pygame.Rect(0, 0, self.w, self.h)

        sim_control.register_watcher("hud_mode_change", self)

    def update(self):
        pass

    def render(self):
        self.surf.fill(self.bg_color)

        # draw pause text
        padding = 15
        coords = (15, 6)
        text_surf = self.font.render("PAUSE", True, self.fg_color)
        text_surf_rect = text_surf.get_rect()
        if sim_control.playback_mode == PLAYBACK_MODE.pause:
            self.surf.fill(self.button_color_alt, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        else:
            self.surf.fill(self.button_color, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        self.surf.blit(text_surf, (coords[0] + padding, coords[1] + padding/2))

        self.button_pause_hotzone = pygame.Rect(
                coords[0],
                coords[1],
                text_surf_rect.w + padding*2,
                text_surf_rect.h + padding)

        # draw play text
        padding = 15
        coords = (120, 6)
        text_surf = self.font.render("PLAY", True, self.fg_color)
        text_surf_rect = text_surf.get_rect()
        if sim_control.playback_mode == PLAYBACK_MODE.play:
            self.surf.fill(self.button_color_alt, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        else:
            self.surf.fill(self.button_color, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        self.surf.blit(text_surf, (coords[0] + padding, coords[1] + padding/2))

        self.button_play_hotzone = pygame.Rect(
                coords[0],
                coords[1],
                text_surf_rect.w + padding*2,
                text_surf_rect.h + padding)

        # draw play (x2) text
        padding = 15
        coords = (210, 6)
        text_surf = self.font.render("PLAY (X2)", True, self.fg_color)
        text_surf_rect = text_surf.get_rect()
        if sim_control.playback_mode == PLAYBACK_MODE.play_x2:
            self.surf.fill(self.button_color_alt, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        else:
            self.surf.fill(self.button_color, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        self.surf.blit(text_surf, (coords[0] + padding, coords[1] + padding/2))

        self.button_play_x2_hotzone = pygame.Rect(
                coords[0],
                coords[1],
                text_surf_rect.w + padding*2,
                text_surf_rect.h + padding)

    def draw(self, parent_surf):
        if sim_control.hud_mode == HUD_MODE.run:
            parent_surf.blit(self.surf, (0, 0))

    def handle_event(self, event):
        if sim_control.hud_mode == HUD_MODE.run:
            if event.type == MOUSEBUTTONDOWN and event.button is 1:

                if self.button_pause_hotzone.collidepoint(event.pos):
                    sim_control.set_playback_mode(PLAYBACK_MODE.pause)
                    self.dirty = 1
                    return True

                elif self.button_play_hotzone.collidepoint(event.pos):
                    sim_control.set_playback_mode(PLAYBACK_MODE.play)
                    self.dirty = 1
                    return True

                elif self.button_play_x2_hotzone.collidepoint(event.pos):
                    sim_control.set_playback_mode(PLAYBACK_MODE.play_x2)
                    self.dirty = 1
                    return True

                elif self.panel_mask.collidepoint(event.pos):
                    return True
        return False


class EditorPanel(Drawable, Eventable):
    def __init__(self):
        Drawable.__init__(self, 200, 320)

        self.font = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.bg_color = pygame.Color("#242424")
        self.button_color = pygame.Color("#3B3B3B")
        self.button_color_alt = pygame.Color("#474747")
        self.fg_color = pygame.Color("#616161")

        self.button_play_hotzone = None
        self.button_pause_hotzone = None
        self.button_play_x2_hotzone = None

        self.panel_mask = pygame.Rect(0, config.window_size[1] - self.h, self.w, self.h)

        sim_control.register_watcher("hud_mode_change", self)

    def update(self):
        pass

    def render(self):
        self.surf.fill(self.bg_color)

        # draw residential text
        padding = 15
        coords = (15, 15)
        text_surf = self.font.render("Residential", True, self.fg_color)
        text_surf_rect = text_surf.get_rect()
        if sim_control.build_mode == BUILD_MODE.residential:
            self.surf.fill(self.button_color_alt, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        else:
            self.surf.fill(self.button_color, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        self.surf.blit(text_surf, (coords[0] + padding, coords[1] + padding/2))

        self.button_residential_hotzone = pygame.Rect(
                coords[0],
                ( config.window_size[1] - self.h ) + coords[1],
                text_surf_rect.w + padding*2,
                text_surf_rect.h + padding)

        # draw commercial text
        padding = 15
        coords = (15, 65)
        text_surf = self.font.render("Commercial", True, self.fg_color)
        text_surf_rect = text_surf.get_rect()
        if sim_control.build_mode == BUILD_MODE.commercial:
            self.surf.fill(self.button_color_alt, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        else:
            self.surf.fill(self.button_color, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        self.surf.blit(text_surf, (coords[0] + padding, coords[1] + padding/2))

        self.button_commercial_hotzone = pygame.Rect(
                coords[0],
                ( config.window_size[1] - self.h ) + coords[1],
                text_surf_rect.w + padding*2,
                text_surf_rect.h + padding)

        # draw industrial text
        padding = 15
        coords = (15, 115)
        text_surf = self.font.render("Industrial", True, self.fg_color)
        text_surf_rect = text_surf.get_rect()
        if sim_control.build_mode == BUILD_MODE.industrial:
            self.surf.fill(self.button_color_alt, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        else:
            self.surf.fill(self.button_color, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        self.surf.blit(text_surf, (coords[0] + padding, coords[1] + padding/2))

        self.button_industrial_hotzone = pygame.Rect(
                coords[0],
                ( config.window_size[1] - self.h ) + coords[1],
                text_surf_rect.w + padding*2,
                text_surf_rect.h + padding)

        # draw fire station text
        padding = 15
        coords = (15, 165)
        text_surf = self.font.render("Fire Station", True, self.fg_color)
        text_surf_rect = text_surf.get_rect()
        if sim_control.build_mode == BUILD_MODE.fire_station:
            self.surf.fill(self.button_color_alt, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        else:
            self.surf.fill(self.button_color, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        self.surf.blit(text_surf, (coords[0] + padding, coords[1] + padding/2))

        self.button_fire_station_hotzone = pygame.Rect(
                coords[0],
                ( config.window_size[1] - self.h ) + coords[1],
                text_surf_rect.w + padding*2,
                text_surf_rect.h + padding)


        # draw road text
        padding = 15
        coords = (15, 215)
        text_surf = self.font.render("Road", True, self.fg_color)
        text_surf_rect = text_surf.get_rect()
        if sim_control.build_mode == BUILD_MODE.road:
            self.surf.fill(self.button_color_alt, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        else:
            self.surf.fill(self.button_color, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        self.surf.blit(text_surf, (coords[0] + padding, coords[1] + padding/2))

        self.button_road_hotzone = pygame.Rect(
                coords[0],
                ( config.window_size[1] - self.h ) + coords[1],
                text_surf_rect.w + padding*2,
                text_surf_rect.h + padding)

        # draw remove text
        padding = 15
        coords = (15, 265)
        text_surf = self.font.render("Remove", True, self.fg_color)
        text_surf_rect = text_surf.get_rect()
        if sim_control.build_mode == BUILD_MODE.remove:
            self.surf.fill(self.button_color_alt, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        else:
            self.surf.fill(self.button_color, rect=(coords[0], coords[1], text_surf_rect.w + padding*2, text_surf_rect.h + padding))
        self.surf.blit(text_surf, (coords[0] + padding, coords[1] + padding/2))

        self.button_remove_hotzone = pygame.Rect(
                coords[0],
                ( config.window_size[1] - self.h ) + coords[1],
                text_surf_rect.w + padding*2,
                text_surf_rect.h + padding)

    def draw(self, parent_surf):
        if sim_control.hud_mode == HUD_MODE.build:
            parent_surf.blit(self.surf, (0, config.window_size[1] - self.h))

    def handle_event(self, event):
        if sim_control.hud_mode == HUD_MODE.build:
            if event.type == MOUSEBUTTONDOWN and event.button is 1:

                if self.button_residential_hotzone.collidepoint(event.pos):
                    sim_control.set_build_mode(BUILD_MODE.residential)
                    self.dirty = 1
                    return True

                elif self.button_commercial_hotzone.collidepoint(event.pos):
                    sim_control.set_build_mode(BUILD_MODE.commercial)
                    self.dirty = 1
                    return True

                elif self.button_industrial_hotzone.collidepoint(event.pos):
                    sim_control.set_build_mode(BUILD_MODE.industrial)
                    self.dirty = 1
                    return True

                elif self.button_fire_station_hotzone.collidepoint(event.pos):
                    sim_control.set_build_mode(BUILD_MODE.fire_station)
                    self.dirty = 1
                    return True

                elif self.button_road_hotzone.collidepoint(event.pos):
                    sim_control.set_build_mode(BUILD_MODE.road)
                    self.dirty = 1
                    return True

                elif self.button_remove_hotzone.collidepoint(event.pos):
                    sim_control.set_build_mode(BUILD_MODE.remove)
                    self.dirty = 1
                    return True
                elif self.panel_mask.collidepoint(event.pos):
                    return True # handle missing button but hitting panel



class Hud(Drawable, Eventable):

    def __init__(self):
        Drawable.__init__(self, *config.window_size)
        Eventable.__init__(self)

        self.children = [
            ModeSwitchPanel(),
            PlaybackControlPanel(),
            EditorPanel()
        ]

        self.dirty = 2


    def update(self):
        for obj in self.children:
            obj.update()


    def render(self):
        """ do not use _render - always render children"""
        self.surf.fill(pygame.Color(0, 0, 0, 0))
        for obj in self.children:
            obj.render()


    def draw(self, parent_surf):
        """ do not use _draw - always draw children"""
        for obj in self.children:
            obj.draw(self.surf)

        parent_surf.blit(self.surf, (0, 0))


    def handle_event(self, event):
        suppress = False
        for obj in self.children:
            if isinstance(obj, Eventable):
                suppress = obj.handle_event(event) or suppress
        return suppress


import math

import pygame
from pygame.locals import *

from eventable import Eventable
from drawable import Drawable

from city_block import CityBlock
from residential_zone import ResidentialZone
from industrial_zone import IndustrialZone
from commercial_zone import CommercialZone
from fire_station import FireStation

import config

class HUD_MODE:
    build = 1
    run = 2

class PLAYBACK_MODE:
    pause = 1
    play = 2
    play_x2 = 3

class BUILD_MODE:
    residential = 1
    commercial = 2
    industrial = 3
    road = 4
    fire_station = 5
    remove = 6

class SimulationControl(Drawable, Eventable):

    def __init__(self):
        w = config.grid_offset * config.map_size[0] + config.road_size*2
        h = config.grid_offset * config.map_size[1] + config.road_size*2
        Drawable.__init__(self, w, h)
        Eventable.__init__(self)

        self.dirty = 2

        self.updates = False
        self.child_updates = False

        self.hud_mode = HUD_MODE.build
        self.last_playback_mode = None
        self.playback_mode = PLAYBACK_MODE.pause
        self.build_mode = BUILD_MODE.residential

        self.vp = None

        self.children= [
            ResidentialZone(0, 0),
            CityBlock(1, 1),
            CityBlock(1, 2),
            CityBlock(2, 3),
            CityBlock(4, 4)
        ]

        self.watchers = {
            "hud_mode_change": [],
            "playback_mode_change": [],
            "build_mode_change": []
        }


    def set_hud_mode(self, mode):
        self.hud_mode = mode
        self.notify_event("hud_mode_change")

    def set_playback_mode(self, mode):
        self.playback_mode = mode
        self.notify_event("playback_mode_change")

    def set_build_mode(self, mode):
        self.build_mode = mode
        self.notify_event("build_mode_change")

    def set_viewport(self, vp):
        self.vp = vp

    def register_watcher(self, event_type, instance):
        if event_type in self.watchers and instance not in self.watchers[event_type]:
            self.watchers[event_type].append(instance)

    def notify_event(self, event_type):
        for obj in self.watchers[event_type]:
            obj.dirty = 1

    def simulation_step(self):

        if self.last_playback_mode != self.playback_mode:
            if self.playback_mode == PLAYBACK_MODE.pause:
                pass # this is where we should pause any timers
                print("Pause")

            elif self.playback_mode == PLAYBACK_MODE.play or self.playback_mode == PLAYBACK_MODE.play_x2:
                pass # this is where we should resume any paused timers
                print("Play X2")

        self.last_playback_mode = self.playback_mode

        if self.playback_mode == PLAYBACK_MODE.play or self.playback_mode == PLAYBACK_MODE.play_x2:
            pass # perform a simulation step
            print("Simulation step")

    def child_at(self, coords):
        for c in self.children:
            if c.x == coords[0] and c.y == coords[1]:
                return c
        return None

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button is 1:
                pos = event.pos

                reprojected = self.vp.project_coord_into_vp(pos)

                if self.hud_mode == HUD_MODE.build:
                    block_coords = (math.floor(reprojected[0] / config.grid_offset),
                             math.floor(reprojected[1] / config.grid_offset))

                    road_coords = ( math.floor(reprojected[0] / 1 ),
                                    math.floor(reprojected[1] / 1 ) )

                    if block_coords[0] < config.map_size[0] and block_coords[1] < config.map_size[1]:
                        if self.build_mode == BUILD_MODE.residential:
                            if not self.child_at(block_coords):
                                self.children.append( ResidentialZone(*block_coords))
                                self.updates = True

                        elif self.build_mode == BUILD_MODE.commercial:
                            if not self.child_at(block_coords):
                                self.children.append( CommercialZone(*block_coords) )
                                self.updates = True

                        elif self.build_mode == BUILD_MODE.industrial:
                            if not self.child_at(block_coords):
                                self.children.append( IndustrialZone(*block_coords) )
                                self.updates = True

                        elif self.build_mode == BUILD_MODE.fire_station:
                            if not self.child_at(block_coords):
                                self.children.append( FireStation(*block_coords) )
                                self.updates = True

                        elif self.build_mode == BUILD_MODE.road:
                            if self.child_at(road_coords):
                                pass
                                #self.children.append( 0 ) # add new road

                        elif self.build_mode == BUILD_MODE.remove:
                            # Handles removing blocks if they exist
                            obj = self.child_at(block_coords)
                            if obj:
                                self.children.remove(obj)
                                self.updates = True

                            # TODO: add step that handles removing roads if they exsist

    def update(self):
        self.child_updates = False
        for c in self.children:
            self.child_updates = c.update() or self.child_updates

        return self.child_updates or self.updates

    def render(self):
        if self.updates or self.child_updates:
            self.surf.fill(pygame.Color(0, 0, 0, 0))

        for c in self.children:
            if self.updates or self.child_updates:
                c.render()
            else:
                c._render()

    def draw(self, parent_surf):
        for c in self.children:
            if self.updates or self.child_updates:
                c.draw(self.surf)
            else:
                c._draw(self.surf)

        self.updates = False
        self.child_updates = False

        parent_surf.blit(self.surf, (0, 0))


sim_control = SimulationControl()

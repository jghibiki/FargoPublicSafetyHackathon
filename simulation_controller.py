import math

from pygame.locals import *

from eventable import Eventable
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

class SimulationControl(Eventable):

    def __init__(self):

        self.hud_mode = HUD_MODE.build
        self.last_playback_mode = None
        self.playback_mode = PLAYBACK_MODE.pause
        self.build_mode = BUILD_MODE.residential

        self.vp = None

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

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button is 1:
                pos = event.pos

                reprojected = self.vp.project_coord_into_vp(pos)

                if self.build_mode == BUILD_MODE.residential:
                    self.vp.children.append(
                            ResidentialZone(
                                math.floor(reprojected[0] / config.grid_offset),
                                math.floor(reprojected[1] / config.grid_offset)))
                elif self.build_mode == BUILD_MODE.commercial:
                    self.vp.children.append(
                            CommercialZone(
                                math.floor(reprojected[0] / config.grid_offset),
                                math.floor(reprojected[1] / config.grid_offset)))
                elif self.build_mode == BUILD_MODE.industrial:
                    self.vp.children.append(
                            IndustrialZone(
                                math.floor(reprojected[0] / config.grid_offset),
                                math.floor(reprojected[1] / config.grid_offset)))

                elif self.build_mode == BUILD_MODE.fire_station:
                    self.vp.children.append(
                            FireStation(
                                math.floor(reprojected[0] / config.grid_offset),
                                math.floor(reprojected[1] / config.grid_offset)))



sim_control = SimulationControl()



class HUD_MODE:
    build = 1
    run = 2

class SimulationControl:

    def __init__(self):

        self.mode = HUD_MODE.build


    def set_mode(self, mode):
        self.mode = mode


sim_control = SimulationControl()

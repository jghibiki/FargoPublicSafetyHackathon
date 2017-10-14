import pygame

class Drawable:

    def __init__(self, width, height, dirty=1):
        self.w = width
        self.h = height
        self.surf = pygame.Surface((width, height), pygame.SRCALPHA)

        self.dirty = dirty


    def update(self):
        raise Exception("{0} must override {0}.update()".format(type(self).__name__))


    def _render(self):
        """ Automatically called in leu of self.render(). handles dirty state"""
        if self.dirty in [1, 2]:
            self.render()

    def render(self):
        raise Exception("{0} must override {0}.render()".format(type(self).__name__))


    def _draw(self, parent_surf):
        if self.dirty in [1, 2]:
            if self.dirty is 1:
                self.dirty = 0
            self.draw(parent_surf)

    def draw(self, parent_surf):
        raise Exception("{0} must override {0}.draw()".format(type(self).__name__))



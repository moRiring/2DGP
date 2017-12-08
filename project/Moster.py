from pico2d import *

class Moster:
    ALIVE, DIE = 0, 1

    image = None

    type = None

    def __init__(self):
        self.state = self.ALIVE

    def draw(self, right):
        pass

    def get_bb(self):
        pass
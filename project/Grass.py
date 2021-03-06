from pico2d import *

class Grass:
    image = None

    PIXEL_PER_METER = (10.0 / 0.3)

    MOVE_SPEED_KMPH = 50.0
    MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
    MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
    MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self, y):
        if Grass.image == None:
            Grass.image = load_image("resource/grass.png")
        self.x = 0
        self.y = y

    def draw(self):
        if self.x <= 600:
            Grass.image.clip_draw(self.x, 0, 600, 48, 300, 24 + self.y)
        else:
            Grass.image.clip_draw(self.x, 0, 1200 - self.x, 48, (1200 - self.x) / 2, 24 + self.y)
            Grass.image.clip_draw(0, 0, 600 - (1200 - self.x), 48, (1200 - self.x) + (600 - (1200 - self.x)) / 2, 24 + self.y)

    def update(self,frame_time):
        distance = Grass.MOVE_SPEED_PPS * frame_time
        self.x = (int)(self.x + distance) % 1200
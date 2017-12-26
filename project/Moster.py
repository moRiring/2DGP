from pico2d import *

class Monster:
    object_TYPE = "MONSTER"

    ALIVE, HIT, DIE = 0, 1, 2
    DIGLETT, PIDGEOT = 0, 1

    TIME_PER_ACTION = 1
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 2

    image = None
    map = None
    type = None

    diglett_image = None
    pidgeot_image = None

    def __init__(self, type):
        self.state = self.ALIVE
        self.total_frames = 0.0
        self.frame = 0
        self.time = 0
        self.opacify = 1

        if Monster.diglett_image == None:
            Monster.diglett_image = load_image('resource/diglett.png')

        if Monster.pidgeot_image == None:
            Monster.pidgeot_image = load_image('resource/pidgeot.png')

        if type == self.DIGLETT:
            self.type = self.DIGLETT
            self.image = Monster.diglett_image
        elif type == self.PIDGEOT:
            self.type = self.PIDGEOT
            self.image = Monster.pidgeot_image

        self.w = (int)(self.image.w / 2)
        self.h = (int)(self.image.h / 2)



    def set_map(self, map):
        Monster.map = map

    def draw(self):
        right = self.map.right

        if self.state in (self.HIT, self.DIE):
            self.image.opacify(self.opacify)

        self.image.clip_draw(self.frame * self.w, self.state * self.h, self.w, self.h, (640 - (right - self.x)), self. y)

        self.image.opacify(1)

    def get_bb(self):
        right = self.map.right

        return 640 - (right - self.x) - self.w / 2 + 10, self.y - self.h / 2 + 10, 640 - (right - self.x) + self.w / 2 - 10, self.y + self.h / 2 - 10


    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def update(self, frame_time):
        self.total_frames += Monster.FRAMES_PER_ACTION * Monster.ACTION_PER_TIME * frame_time
        self.frame = (int)(self.total_frames) % 2

        if self.state == self.HIT:
            self.frame = 0
            self.opacify -= frame_time

            if self.opacify < 0:
                self.opacify = 0
                self.state = self.DIE


    def hit(self):
        self.state = self.HIT
        self.opacify = 1

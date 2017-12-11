from pico2d import *

class Moster:
    object_TYPE = "MONSTER"


    ALIVE, DIE = 0, 1
    RATTATA = 0

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 2

    image = None
    map = None
    type = None

    rattata_image = None

    def __init__(self, type):
        self.state = self.ALIVE
        self.total_frames = 0.0
        self.frame = 0

        if Moster.rattata_image == None:
            Moster.rattata_image = load_image('resource/rattata.png')

        if type == self.RATTATA:
            self.type = self.RATTATA
            self.image = Moster.rattata_image
            self.w = 58
            self.h = 42


    def set_map(self, map):
        Moster.map = map

    def draw(self):
        right = self.map.right

        if self.state == self.DIE:
            self.image.opacify(0)

        self.draw_bb()

        self.image.clip_draw(self.frame * self.w, 0, self.w, self.h, (640 - (right - self.x)), self. y)

        self.image.opacify(1)

    def get_bb(self):
        right = self.map.right

        return 640 - (right - self.x) - self.w / 2 + 10, self.y - self.h / 2 + 10, 640 - (right - self.x) + self.w / 2 - 10, self.y + self.h / 2 - 10


    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def update(self, frame_time):
        self.total_frames += Moster.FRAMES_PER_ACTION * Moster.ACTION_PER_TIME * frame_time
        self.frame = (int)(self.total_frames) % 2


    def die(self):
        self.state = self.DIE
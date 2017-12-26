from pico2d import *

class Animation:
    door_image = None
    black = None

    def __init__(self):
        if(self.door_image == None):
            self.door_image = load_image("resource/door.png")
        if self.black == None:
            self.black = load_image("resource/black.png")

        self.black.opacify(0.5)
        self.time = 0

    def draw_door(self):
        frame = (int)(self.time * 1.5 % 5)
        w = (int)(self.door_image.w // 5)
        h = (int)(self.door_image.h)
        self.black.draw(300, 600)
        self.door_image.clip_draw((int)(w * frame), 0, w, h, 300, 450)

    def open_door(self, frame_time):
        self.time += frame_time
        opacify = (3 - self.time) / 3
        self.door_image.opacify(opacify)
        self.black.opacify(opacify/2)

        if(self.time > 3):
            self.time = 0
            return 1
from pico2d import *

class Eevee:
    image = None

    PIXEL_PER_METER = (10.0 / 0.3)
    JUMP_SPEED_KMPH = 70.0
    JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
    JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
    JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 3

    RUN, JUMP, DROP, ATTACK, HIT = 0, 1, 2, 3, 4
    NOMAL, FIRE, ELECTRIC, WATER = 0, 1, 2, 3, 4

    FRUIT, KEY = 0, 1

    item_num = {"fruit" : 0, "key" : 0}

    def __init__(self):
        if Eevee.image == None:
            Eevee.image = load_image("resource/Eevee_Run.png")
        self.frame = 0
        self.x = 80
        self.y = 45
        self.w = (int)((Eevee.image.w) / 3)
        self.h = (int)(Eevee.image.h)
        self.state = self.RUN
        self.dir =  1
        self.total_frames = 0.0


    def draw(self):
        #self.draw_bb()
        self.image.clip_draw(self.frame * self.w, 0, self.w, self.h, self.x, self.y)


    def update(self, frame_time):
        self.total_frames += Eevee.FRAMES_PER_ACTION * Eevee.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 3

        if self.state in (self.JUMP, self.DROP):
            distance = Eevee.JUMP_SPEED_PPS * frame_time
            self.y += (self.dir * distance)
            if self.y > 150:
                self.state = self.DROP
                self.dir = -1
                self.y = 150
            elif self.y < 45:
                self.state = self.RUN
                self.y = 45


    def get_item(self, item_type):
        if item_type == self.FRUIT:
            self.item_num["fruit"] += 1
        elif item_type == self.KEY:
            self.item_num["key"] += 1

    def handle_event(self, event, frame_time):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.state == self.RUN:
                self.state = self.JUMP
                self.dir = 1


    def get_bb(self):
        return self.x - self.w / 2 + 5, self.y - self.h / 2 + 5, self.x + self.w / 2 - 5, self.y + self.h / 2 - 5

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
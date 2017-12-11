from pico2d import *

class Eevee:
    image = None

    PIXEL_PER_METER = (10.0 / 0.3)

    ATTACK_SPEED_KMPH = 25.0
    ATTACK_SPEED_MPM = (ATTACK_SPEED_KMPH * 1000.0 / 60.0)
    ATTACK_SPEED_MPS = (ATTACK_SPEED_MPM / 60.0)
    ATTACK_SPEED_PPS = (ATTACK_SPEED_MPS * PIXEL_PER_METER)

    JUMP_SPEED_KMPH = 50.0
    JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
    JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
    JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 3

    RUN, JUMP, DROP, ATTACK, HIT = 0, 1, 2, 3, 4
    NOMAL, FIRE, ELECTRIC, WATER = 0, 1, 2, 3

    FRUIT, KEY = 0, 1

    item_num = {"fruit" : 0, "key" : 0}

    def __init__(self):
        if Eevee.image == None:
            Eevee.image = load_image("resource/eevee.png")
        self.frame_row = 0
        self.frame_col = 0
        self.x = 80
        self.y = 45
        self.w = (int)((Eevee.image.w) / 3)
        self.h = (int)(Eevee.image.h / 3)
        self.state = self.RUN
        self.heart = 6
        self.x_dir = 1
        self.y_dir =  1
        self.alpha = 1
        self.time = 0
        self.total_frames = 0.0


    def draw(self):
        self.draw_bb()
        self.image.opacify(self.alpha)
        self.image.clip_draw(self.frame_row * self.w, self.h * self.frame_col, self.w, self.h, self.x, self.y)


    def update(self, frame_time):
        self.total_frames += Eevee.FRAMES_PER_ACTION * Eevee.ACTION_PER_TIME * frame_time

        if self.state in (self.RUN, self.JUMP):
            self.frame_row = int(self.total_frames) % 3

        if self.state in (self.JUMP, self.DROP):
            distance = Eevee.JUMP_SPEED_PPS * frame_time
            self.y += (self.y_dir * distance)

            if self.y > 150:
                self.state = self.DROP
                self.y_dir = -1
                self.y = 150
            elif self.y < 45:
                self.state = self.RUN
                self.y = 45

        if self.state == self.ATTACK:
            distance = Eevee.ATTACK_SPEED_PPS * frame_time
            self.x += (self.x_dir * distance)

            if self.x_dir == 0:
                self.frame_row = int(self.total_frames) % 3

            if self.x > 120:
                self.x_dir = -1
                self.x = 120
                self.state = self.RUN
                self.frame_col = 0


        if self.state == self.HIT:
            self.time += frame_time

            if (int)(self.total_frames) % 2 == 0:
                self.alpha = 1
                self.frame_row = 0
            else:
                self.alpha = 0.5
                self.frame_row = 1
            if self.time > 1:
                self.state = self.RUN
                self.frame_col = 0
                self.frame_row = int(self.total_frames) % 3
                self.alpha = 1
                self.time = 0

        if self.state not in (self.JUMP, self.DROP) and self.y != 45:
            distance = Eevee.JUMP_SPEED_PPS * frame_time
            self.y += (self.y_dir * distance)
            if self.y < 45:
                self.y = 45
            elif self.y > 150:
                self.y_dir = -1
                self.y = 150

        if self.x != 80 and self.state != self.ATTACK:
            distance = Eevee.ATTACK_SPEED_PPS * frame_time
            self.x += (self.x_dir * distance)

            if self.x < 80:
                self.x = 80
                self.state = self.RUN



    def get_item(self, item_type):
        if item_type == self.FRUIT and self.item_num["fruit"] < 9:
            self.item_num["fruit"] += 1

    def handle_event(self, event, frame_time):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.state == self.RUN:
                self.state = self.JUMP
                self.y_dir = 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
            if self.state in (self.RUN, self.JUMP):
                self.state = self.ATTACK
                self.x_dir = 1
                self.frame_col = 1
                self.frame_row = 2

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_x):
            if self.item_num["fruit"] >= 1 and self.heart < 6:
                self.item_num["fruit"] -= 1
                self.heart += 1


    def hit(self):
        if self.state != self.HIT:
            self.state = self.HIT
            self.heart -= 1
            self.frame_col = 1
            self.frame_row = 0

            if self.heart == 0:
                pass


    def get_bb(self):
        return self.x - self.w / 2 + 10, self.y - self.h / 2 + 10, self.x + self.w / 2 - 10, self.y + self.h / 2 - 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
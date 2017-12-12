from pico2d import *

class Eevee:
    image = None

    nomal_image = None
    fire_image = None
    electric_image = None
    water_image = None

    eat_efffect_image = None

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

    RUN, JUMP, DROP, ATTACK, HIT, EAT, EVOLVE, INVINCIBILITY = 0, 1, 2, 3, 4, 5, 6, 7
    NOMAL, FIRE, ELECTRIC, WATER = 0, 1, 2, 3

    FARMING_ROOM, BOSS_ROOM = 0, 1

    KEY, FRUIT, FIRE_STONE, ELECTRIC_STONE, WATER_STONE = 0, 1, 2, 3, 4

    def __init__(self):
        if Eevee.nomal_image == None:
            Eevee.nomal_image = load_image("resource/eevee.png")
        if Eevee.fire_image == None:
            Eevee.fire_image = load_image("resource/fire.png")
        if Eevee.electric_image == None:
            Eevee.electric_image = load_image("resource/electric.png")
        if Eevee.water_image == None:
            Eevee.water_image = load_image("resource/water.png")

        self.image = self.nomal_image
        self.frame_row = 0
        self.frame_col = 0
        self.w = (int)((self.image.w) / 3)
        self.h = (int)(self.image.h / 3)
        self.x = 80
        self.y = 60 - self.h / 2
        self.state = self.RUN
        self.type = self.NOMAL
        self.heart = 6
        self.x_dir = 1
        self.y_dir =  1
        self.alpha = 1
        self.time = 0
        self.area = 0
        self.rotation = self.FARMING_ROOM
        self.total_frames = 0.0

        self.item_num = {
        self.KEY : 0, self.FRUIT : 0, self.FIRE_STONE: 0, self.ELECTRIC_STONE: 0, self.WATER_STONE: 0
    }


    def draw(self):
        #self.draw_bb()
        self.image.opacify(self.alpha)
        self.image.clip_draw(self.frame_row * self.w, self.h * self.frame_col, self.w, self.h, self.x, self.y + self.area)


    def update(self, frame_time):
        self.total_frames += Eevee.FRAMES_PER_ACTION * Eevee.ACTION_PER_TIME * frame_time

        if self.state in (self.RUN, self.JUMP, self.INVINCIBILITY):
            self.frame_row = int(self.total_frames) % 3

        if self.state == self.INVINCIBILITY:
            self.time += frame_time
            if (int)(self.total_frames) % 2 == 0:
                self.alpha = 1
            else:
                self.alpha = 0.5
            if self.time > 1:
                self.state = self.RUN
                self.alpha = 1
                self.time = 0


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
                if self.type != self.NOMAL:
                    self.type = self.NOMAL
                    self.image = self.nomal_image
                    self.w = (int)((self.image.w) / 3)
                    self.h = (int)(self.image.h / 3)
                    self.y = 60 - self.h / 2

                self.state = self.RUN
                self.frame_col = 0
                self.frame_row = int(self.total_frames) % 3
                self.alpha = 1
                self.time = 0

        if self.state not in (self.JUMP, self.DROP) and self.y != 45:
            distance = Eevee.JUMP_SPEED_PPS * frame_time
            self.y += (self.y_dir * distance)
            if self.y < 45 :
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
        if self.item_num[item_type] < 9:
            self.item_num[item_type] += 1


    def handle_event(self, event, frame_time):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.state == self.RUN:
                self.state = self.JUMP
                self.y_dir = 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
            if self.state == self.RUN:
                self.state = self.ATTACK
                self.x_dir = 1
                self.frame_col = 1
                self.frame_row = 2

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_x):
            if self.item_num[self.FRUIT] >= 1 and self.heart < 6:
                self.item_num[self.FRUIT] -= 1
                self.heart += 1

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP) and self.item_num[self.KEY] == 1 and self.state == self.RUN:
            self.area = 300
            self.rotation = self.BOSS_ROOM

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN) and self.state == self.RUN:
            self.area = 0
            self.rotation = self.FARMING_ROOM



    def hit(self):
        if self.state not in (self.HIT, self.INVINCIBILITY):
            self.state = self.HIT
            self.frame_col = 1
            self.frame_row = 0

            if self.type == self.NOMAL:
                self.heart -= 1

            if self.heart == 0:
                pass


    def get_bb(self):
        return self.x - self.w / 2 + 10, self.y + self.area - self.h / 2 + 10, self.x + self.w / 2 - 10, self.y + self.area + self.h / 2 - 10


    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def evolution(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_1 and self.item_num[self.FIRE_STONE] > 0:
            self.type = self.FIRE
            self.image = self.fire_image
            self.state = self.INVINCIBILITY
            self.time = 0

            self.w = (int)((self.image.w) / 3)
            self.h = (int)(self.image.h / 3)
            self.y = 60 - self.h / 2
            return True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2 and self.item_num[self.ELECTRIC_STONE] > 0:
            self.type = self.ELECTRIC
            self.image = self.electric_image
            self.state = self.INVINCIBILITY
            self.time = 0

            self.w = (int)((self.image.w) / 3)
            self.h = (int)(self.image.h / 3)
            self.y = 60 - self.h / 2
            return True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_3 and self.item_num[self.WATER_STONE] > 0:
            self.type = self.WATER
            self.image = self.water_image
            self.state = self.INVINCIBILITY
            self.time = 0

            self.w = (int)((self.image.w) / 3)
            self.h = (int)(self.image.h / 3)
            self.y = 60 - self.h / 2
            return True
        else:
            return False

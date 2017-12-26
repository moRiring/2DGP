from pico2d import *

class Skill:
    fire_image = None
    electric_image = None
    water_image = None

    fire_sound = None

    NOMAL, FIRE, ELECTRIC, WATER = 0, 1, 2, 3

    TIME_PER_ACTION = 3
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

    image = None

    def __init__(self):
        self.cool_time = 0
        self.time = 0
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.on = 0
        self.sound_re = 0

        if self.fire_image == None:
            self.fire_image = load_image("resource/fire_skill.png")
        if Skill.fire_sound == None:
            Skill.fire_sound = load_wav("resource/fire.wav")

    def set(self, eevee):
        self.eevee = eevee

    def skill_on(self):
        if self.eevee.type != self.NOMAL:
            self.on = 1
        if  self.eevee.type == self.FIRE:
            self.image = self.fire_image
            self.clip = 15
            self.w = (int)(self.image.w // self.clip)
            self.h = (int)(self.image.h)
            self.frame = 0
            self.fire_sound.play()

    def update(self, frame_time):
        if self.on:
            self.time += frame_time
            self.total_frames = self.clip * self.ACTION_PER_TIME * self.time

            if self.time > 1.5 and self.sound_re == 0:
                self.fire_sound.play()
                self.sound_re = 1

            self.frame = self.total_frames % self.clip
            if self.time > 3:
                self.time = 0
                self.on = 0


    def get_bb(self):
        return  self.eevee.x - self.w // 2 + 20, self.eevee.y - self.h // 2 + 20 + 10 + self.eevee.area,self.eevee.x + self.w // 2 - 20, self.eevee.y + self.h // 2 - 20 + 10 + self.eevee.area


    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        if self.on == 1:
            self.image.clip_draw((int)(self.w * (int)(self.frame)), 0, self.w, self.h, self.eevee.x, self.eevee.y + 10 + self.eevee.area)
            #self.draw_bb()


class Eevee:
    image = None

    nomal_image = None
    fire_image = None
    electric_image = None
    water_image = None

    eat_effect_image = None

    jump_sound = None
    evol_sound = None
    hit_evol_sound = None
    gameover_sound = None
    eat_sound = None
    hit_sound = None
    get_sound = None
    attack_sound = None

    skill = None

    PIXEL_PER_METER = (10.0 / 0.3)

    MOVE_SPEED_KMPH = 50.0
    MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
    MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
    MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)

    ATTACK_SPEED_KMPH = 50.0
    ATTACK_SPEED_MPM = (ATTACK_SPEED_KMPH * 1000.0 / 60.0)
    ATTACK_SPEED_MPS = (ATTACK_SPEED_MPM / 60.0)
    ATTACK_SPEED_PPS = (ATTACK_SPEED_MPS * PIXEL_PER_METER)

    BACK_SPEED_KMPH = 8.0
    BACK_SPEED_MPM = (BACK_SPEED_KMPH * 1000.0 / 60.0)
    BACK_SPEED_MPS = (BACK_SPEED_MPM / 60.0)
    BACK_SPEED_PPS = (BACK_SPEED_MPS * PIXEL_PER_METER)

    JUMP_SPEED_KMPH = 40.0
    JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
    JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
    JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 3

    RUN, JUMP, DROP, ATTACK, BACK, HIT, EVOLVE, INVINCIBILITY, CLEAR, DIE = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
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

        if Eevee.eat_effect_image == None:
            Eevee.eat_effect_image = load_image("resource/eat_effect.png")
            Eevee.eat_effect_image.opacify(0.5)

        if Eevee.jump_sound == None:
            Eevee.jump_sound = load_wav("resource/jump.wav")

        if Eevee.evol_sound == None:
            Eevee.evol_sound = load_wav("resource/evol.wav")

        if Eevee.hit_evol_sound == None:
            Eevee.hit_evol_sound = load_wav("resource/hit_evol.wav")

        if Eevee.eat_sound == None:
            Eevee.eat_sound = load_wav("resource/eat.wav")

        if Eevee.gameover_sound == None:
            Eevee.gameover_sound = load_wav("resource/gameover.wav")

        if Eevee.hit_sound == None:
            Eevee.hit_sound = load_wav("resource/hit.wav")

        if Eevee.get_sound == None:
            Eevee.get_sound = load_wav("resource/get.wav")

        if Eevee.attack_sound == None:
            Eevee.attack_sound = load_wav("resource/attack.wav")

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
        self.eat_state = 0

        self.area_move_time = 0

        self.skill = Skill()
        self.skill.set(self)

        self.item_num = {
        self.KEY : 0, self.FRUIT : 0, self.FIRE_STONE: 0, self.ELECTRIC_STONE: 0, self.WATER_STONE: 0
    }


    def draw(self):
        #self.draw_bb()
        self.image.opacify(self.alpha)
        self.image.clip_draw(self.frame_row * self.w, self.h * self.frame_col, self.w, self.h, self.x, self.y + self.area)
        if self.eat_state == 1:
            self.eat_effect()

        self.skill.draw()


    def update(self, frame_time):
        self.total_frames += Eevee.FRAMES_PER_ACTION * Eevee.ACTION_PER_TIME * frame_time

        self.area_move_time += frame_time

        if self.state in (self.RUN, self.JUMP, self.BACK, self.INVINCIBILITY, self.CLEAR, self.DIE):
            self.frame_row = int(self.total_frames) % 3

        if self.eat_state == 1:
            self.time += frame_time
            if self.time > 0.5:
                self.time = 0
                self.eat_state = 0

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

            if self.x > 130:
                self.x_dir = -1
                self.x = 130
                self.state = self.BACK
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

            distance = Eevee.ATTACK_SPEED_PPS * frame_time
            self.x_dir = -1
            self.x += (self.x_dir * distance)

            if self.x < 80:
                self.x = 80
                self.x_dir = 1

        if self.state not in (self.JUMP, self.DROP) and self.y != 45:
            distance = Eevee.JUMP_SPEED_PPS * frame_time
            self.y += (self.y_dir * distance)
            if self.y < 45 :
                self.y = 45
            elif self.y > 150:
                self.y_dir = -1
                self.y = 150

        if self.state == self.BACK:
            distance = Eevee.BACK_SPEED_PPS * frame_time
            self.x += (self.x_dir * distance)

            if self.x < 80:
                self.x = 80
                self.state = self.RUN

        if self.state == self.CLEAR:
            self.time += frame_time
            self.frame_col = 0
            distance = frame_time * self.MOVE_SPEED_PPS
            if self.time > 5:
                self.x += distance

                if self.x > 800:
                    return True

        if self.state == self.DIE:
            self.time += frame_time
            if self.time > 3:
                self.time = 3
            self.frame_col = 1
            self.alpha = ((3 - self.time) / 3)

        self.skill.update(frame_time)

    def get_item(self, item_type):
        if self.item_num[item_type] < 9:
            self.item_num[item_type] += 1
            self.get_sound.play()


    def handle_event(self, event, frame_time):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.state == self.RUN:
                self.state = self.JUMP
                self.y_dir = 1
                self.jump_sound.play()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
            if self.state == self.RUN:
                self.state = self.ATTACK
                self.x_dir = 1
                self.frame_col = 1
                self.frame_row = 2
                self.attack_sound.play()

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_x):
            if self.item_num[self.FRUIT] >= 1 and self.heart < 6:
                self.item_num[self.FRUIT] -= 1
                self.eat_sound.play()
                self.eat_state = 1
                self.time = 0
                self.heart += 1

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP) and self.item_num[self.KEY] == 2 and self.state == self.RUN and self.area_move_time > 5:
            self.area = 300
            self.rotation = self.BOSS_ROOM
            self.state = self.INVINCIBILITY
            self.area_move_time = 0

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN) and self.state == self.RUN  and self.area_move_time > 5:
            self.area = 0
            self.rotation = self.FARMING_ROOM
            self.state = self.INVINCIBILITY
            self.area_move_time = 0

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_s) and self.state == self.RUN:
            self.skill.skill_on()


    def hit(self):
        if self.state not in (self.HIT, self.INVINCIBILITY, self.DIE):
            self.state = self.HIT
            self.frame_col = 1
            self.frame_row = 0

            if self.type == self.NOMAL:
                self.heart -= 1
                if self.heart > 0:
                    self.hit_sound.play()
            else:
                self.hit_evol_sound.play()

            if self.heart <= 0:
                self.state = self.DIE
                self.gameover_sound.play()
                return True


    def get_bb(self):
        return self.x - self.w / 2 + 10, self.y + self.area - self.h / 2 + 10, self.x + self.w / 2 - 10, self.y + self.area + self.h / 2 - 10


    def eat_effect(self):
        frame = (int)(self.time * 100 % 13)
        w = (int)(Eevee.eat_effect_image.w // 13)
        h = (int)(Eevee.eat_effect_image.h)
        Eevee.eat_effect_image.clip_draw((int)(frame * w), 0, w, h, self.x, self.area + self.y + 5)


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

            self.item_num[self.FIRE_STONE] -= 1
            self.evol_sound.play()
            return True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2 and self.item_num[self.ELECTRIC_STONE] > 0:
            self.type = self.ELECTRIC
            self.image = self.electric_image
            self.state = self.INVINCIBILITY
            self.time = 0

            self.w = (int)((self.image.w) / 3)
            self.h = (int)(self.image.h / 3)
            self.y = 60 - self.h / 2

            self.item_num[self.ELECTRIC_STONE] -= 1
            self.evol_sound.play()
            return True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_3 and self.item_num[self.WATER_STONE] > 0:
            self.type = self.WATER
            self.image = self.water_image
            self.state = self.INVINCIBILITY
            self.time = 0

            self.w = (int)((self.image.w) / 3)
            self.h = (int)(self.image.h / 3)
            self.y = 60 - self.h / 2

            self.item_num[self.WATER_STONE] -= 1
            self.evol_sound.play()
            return True
        else:
            return False

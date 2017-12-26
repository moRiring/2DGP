from pico2d import *
import random

class Attack3:
    image = None

    PIXEL_PER_METER = (10.0 / 0.3)

    MOVE_SPEED_KMPH = 50.0
    MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
    MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
    MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)

    GO, HIT = 0, 1

    def __init__(self):
        if Attack3.image == None:
            Attack3.image = load_image("resource/attack3.png")

        self.x = 650 + random.randint(0, 100)
        self.y = random.randint(400, 600)

        self.dir = random.randint(0, 1)
        if self.dir == 0:
            self.dir = 1
        else:
            self.dir = -1

        self.w = (int)(self.image.w)
        self.h = (int)(self.image.h)

        self.state = self.GO

    def update(self, frame_time):
        distance = self.MOVE_SPEED_PPS * frame_time

        if(self.state == self.GO):
            self.x -= distance
        self.y += self.dir * distance

        if self.y < 300 + 40:
            self.y = 340
            self.dir = self.dir * -1
        elif self.y > 450:
            self.y = 450
            self.dir = self.dir * -1

        if self.x < -250:
            self.x = 650 + random.randint(0, 100)
            self.y = random.randint(400, 600)
            return True

    def get_bb(self):
        return self.x - self.w // 2 + 20, self.y - self.h // 2 + 20, self.x + self.w // 2 - 20, self.y + self.h // 2 - 20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        #self.draw_bb()
        self.image.draw(self.x, self.y)

    def hit(self):
        self.state = self.HIT
        self.x = 650 + random.randint(0, 100)



class Boss:

    PIXEL_PER_METER = (10.0 / 0.3)

    MOVE_SPEED_KMPH = 100.0
    MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
    MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
    MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)

    BACK_SPEED_KMPH = 25.0
    BACK_SPEED_MPM = (BACK_SPEED_KMPH * 1000.0 / 60.0)
    BACK_SPEED_MPS = (BACK_SPEED_MPM / 60.0)
    BACK_SPEED_PPS = (BACK_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 3

    image = None
    heart_image = None

    clear_sound = None

    IDLE, BACK, HIT, ATTACK2, ATTACK3, DIE = 0, 1, 2, 3, 4, 5

    def __init__(self):
        if Boss.image == None:
            Boss.image = load_image("resource/boss.png")
        if Boss.heart_image == None:
            Boss.heart_image = load_image("resource/boss_heart.png")
        if Boss.clear_sound == None:
            Boss.clear_sound = load_wav("resource/clear.wav")

        self.state = self.IDLE
        self.hp = 15
        self.x = 600 - 80
        self.y = 50 + 300

        self.w = self.image.w // 3
        self.h = self.image.h // 3

        self.frame = 0
        self.col = 1

        self.total_frames = 0
        self.total_time = 0

        self.time = 0
        self.hp_time = 0

        self.attack3 = [Attack3(), Attack3(), Attack3()]

    def set_eevee(self, eevee):
        self.eevee = eevee

    def get_bb(self):
        return self.x - self.w / 2 + 30, self.y - self.h / 2 + 10, self.x + self.w / 2 - 15, self.y  + self.h / 2 - 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def heart_ui(self):
        for i in range(3):
            for j in range(5):
                if i * 5 + j + 1<= self.hp:
                    self.heart_image.clip_draw(21, 0, 21, 21, self.x - 62 + 25 * j, self.y + 100 - i * 25)
                else:
                    self.heart_image.clip_draw(0, 0, 21, 21, self.x - 62 + 25 * j, self.y + 100 - i * 25)

    def draw(self):
        #self.draw_bb()

        self.heart_ui()

        self.image.clip_draw(self.frame * self.w, self.col * self.h, self.w, self.h, self.x, self.y)

        if self.state == self.ATTACK3:
            for attack3 in self.attack3:
                attack3.draw()

    def update(self, frame_time):
        self.total_frames += Boss.FRAMES_PER_ACTION * Boss.ACTION_PER_TIME * frame_time
        self.frame = (int)(self.total_frames) % 2

        if self.state == self.ATTACK3:
            self.time += frame_time
            for attack in self.attack3:
                if (attack.update(frame_time)):
                    self.state = self.IDLE
                    for attack in self.attack3:
                        attack.state = attack.GO
            if self.time > 3:
                self.state = self.IDLE
                self.time = 0

        self.total_time += frame_time

        self.image.opacify(1)

        if self.state == self.HIT:
            self.time += frame_time

            if (int)(self.total_frames) % 2 == 0:
                self.image.opacify(1)
            else:
                self.image.opacify(0.5)
            if self.time > 1:
                self.state =random.randint(self.IDLE, self.BACK)
                self.frame_col = 0
                self.image.opacify(1)
                self.time = 0

        if self.state == self.DIE:
            self.time += frame_time
            if self.time > 5:
                self.time = 5
            self.image.opacify((5 - self.time) / 5)
            self.heart_image.opacify((5 - self.time) / 5)

        if self.state == self.IDLE:
            self.col = 1
        if self.state == self.BACK:
            self.col = 0

        if self.eevee.area == 300:
            distance = self.MOVE_SPEED_PPS * frame_time
            self.x -= distance

            if self.total_time % 5 < 3.1 and self.total_time % 5 > 3.0 and self.state in (self.IDLE, self.BACK):
                self.state = self.ATTACK3
                self.time = 0

            if self.x < 50:
                if self.state not in (self.HIT, self.DIE):
                    self.state = self.BACK
                self.col = 0
                self.x = 50

            if self.state in (self.BACK, self.HIT, self.DIE, self.ATTACK3):
                self.x += distance
                distance = self.BACK_SPEED_PPS * frame_time
                self.x += distance
                if self.x > 600 - 80:
                    self.x = 600 - 80
                    if self.state not in (self.DIE, self.ATTACK3):
                        self.state = self.IDLE
                        self.col = 1
        else:
            self.total_time = 0
            self.hp_time += frame_time
            if self.hp_time > 1:
                self.hp_time = 0
                if self.hp % 5 != 0:
                    self.hp += 1
            if self.x != 600 -80:
                self.col = 0
                distance = self.BACK_SPEED_PPS * frame_time
                self.x += distance
                if self.x > 600 - 80:
                    self.x = 600 - 80
                    self.state = self.IDLE
                    self.col = 1

    def hit(self):
        if(self.state != self.HIT):
            self.hp -= 1
            self.state = self.HIT
            self.col = 2
            self.time = 0

        if self.hp <= 0:
            self.state = self.DIE
            self.clear_sound.play()
            return True

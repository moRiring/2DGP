from pico2d import *

class BackGround:
    image = None

    music = None

    PIXEL_PER_METER = (10.0 / 0.3)

    MOVE_SPEED_KMPH = 30.0
    MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
    MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
    MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self, y):
        if BackGround.image == None:
            BackGround.image = load_image("resource/background.png")
        if BackGround.music == None:
            BackGround.music = load_music("resource/background.mp3")
        self.x = 0
        self.y = y

        BackGround.music.repeat_play()

    def draw(self):
        if self.x <= 600:
            BackGround.image.clip_draw(self.x, 0, 600, 300, 300, 150 + self.y)
        else:
            BackGround.image.clip_draw(self.x, 0, 1200 - self.x, 300, (1200 - self.x) / 2, 150  + self.y)
            BackGround.image.clip_draw(0, 0, 600 - (1200 - self.x), 300, (1200 - self.x) + (600 - (1200 - self.x)) / 2, 150  + self.y)

    def update(self, frame_time):
        distance = BackGround.MOVE_SPEED_PPS * frame_time
        self.x = (int)(self.x  + distance) % 1200
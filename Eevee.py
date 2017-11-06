from pico2d import *

open_canvas(600, 300)

class BackGround:
    def __init__(self):
        self.image = load_image("background.png")
        self.x = 0

    def draw(self):
        if self.x <= 600:
            self.image.clip_draw(self.x, 0, 600, 300, 300, 150)
        else:
            self.image.clip_draw(self.x, 0, 1200 - self.x, 300, (1200 - self.x) / 2, 150)
            self.image.clip_draw(0, 0, 600 - (1200 - self.x), 300, (1200 - self.x) + (600 - (1200 - self.x)) / 2, 150)

    def update(self):
        self.x = (self.x  + 10) % 1200

class Grass:
    def __init__(self):
        self.image = load_image("Grass.png")
        self.x = 0

    def draw(self):
        if self.x <= 600:
            self.image.clip_draw(self.x, 0, 600, 48, 300, 24)
        else:
            self.image.clip_draw(self.x, 0, 1200 - self.x, 48, (1200 - self.x) / 2, 24)
            self.image.clip_draw(0, 0, 600 - (1200 - self.x), 48, (1200 - self.x) + (600 - (1200 - self.x)) / 2, 24)

    def update(self):
        self.x = (self.x  + 10) % 1200

class Eevee:
    def __init__(self):
        self.image = load_image("Eevee_Run.png")
        self.frame = 0
        self.x = 80
        self.y = 45
        self.w = (int)((self.image.w) / 3)
        self.h = (int)(self.image.h)

    def draw(self):
        self.image.clip_draw(self.frame * self.w, 0, self.w, self.h, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 3

eevee = Eevee()
background = BackGround()
grass = Grass()

while(True):
    clear_canvas()
    background.draw()
    grass.draw()
    eevee.draw()
    update_canvas()
    background.update()
    grass.update()
    eevee.update()
    delay(0.08)


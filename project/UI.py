from pico2d import *

class UI:
    font = None

    eevee_heart_image = None
    item_fruit_image = None


    def __init__(self):
        if UI.font == None:
            UI.font = load_font('soya8.ttf', 20)
        if UI.eevee_heart_image == None:
            UI.eevee_heart_image = load_image('resource/heart.png')
        if UI.item_fruit_image == None:
            UI.item_fruit_image = load_image('resource/tree_fruit.png')

    def set_eevee(self, eevee):
        self.eevee = eevee

    def draw(self, eevee):
        self.draw_heart()
        self.draw_item()


    def draw_heart(self):
        for i in range(3):
            if self.eevee.heart / ((i + 1) * 2) >= 1:
                self.eevee_heart_image.clip_draw(33 * 2, 0, 33, 33, 30 + 35 * i, 280)
            elif self.eevee.heart % 2 == 1 and self.eevee.heart > i * 2:
                self.eevee_heart_image.clip_draw(33 * 1, 0, 33, 33, 30 + 35 * i, 280)
            else:
                self.eevee_heart_image.clip_draw(33 * 0, 0, 33, 33, 30 + 35 * i, 280)



    def draw_item(self):
        self.item_fruit_image.draw(550, 280)
        self.font.draw(575, 280, "%d" % self.eevee.item_num["fruit"], (0,0,0))
from pico2d import *

class UI:
    font = None

    eevee_heart_image = None

    item_fruit_image = None
    item_fire_stone_image = None
    item_electric_stone_image = None
    item_water_stone_image = None

    KEY, FRUIT, FIRE_STONE, ELECTRIC_STONE, WATER_STONE = 0, 1, 2, 3, 4

    def __init__(self):
        if UI.font == None:
            UI.font = load_font('soya8.ttf', 20)
        if UI.eevee_heart_image == None:
            UI.eevee_heart_image = load_image('resource/heart.png')
        if UI.item_fruit_image == None:
            UI.item_fruit_image = load_image('resource/tree_fruit.png')
        if UI.item_fire_stone_image == None:
            UI.item_fire_stone_image = load_image('resource/fire_stone.png')
        if UI.item_electric_stone_image == None:
            UI.item_electric_stone_image = load_image('resource/electric_stone.png')
        if UI.item_water_stone_image == None:
            UI.item_water_stone_image = load_image('resource/water_stone.png')

    def set_eevee(self, eevee):
        self.eevee = eevee

    def draw(self):
        self.draw_heart()
        self.draw_item()


    def draw_heart(self):
        for i in range(3):
            if self.eevee.heart / ((i + 1) * 2) >= 1:
                self.eevee_heart_image.clip_draw(33 * 2, 0, 33, 33, 30 + 35 * i, 280 + self.eevee.area)
            elif self.eevee.heart % 2 == 1 and self.eevee.heart > i * 2:
                self.eevee_heart_image.clip_draw(33 * 1, 0, 33, 33, 30 + 35 * i, 280 + self.eevee.area)
            else:
                self.eevee_heart_image.clip_draw(33 * 0, 0, 33, 33, 30 + 35 * i, 280 + self.eevee.area)



    def draw_item(self):
        self.item_fruit_image.draw(550, 280 + self.eevee.area)
        self.font.draw(575, 280 + self.eevee.area, "%d" % self.eevee.item_num[self.FRUIT], (0,0,0))


    def draw_evolution(self):
        self.item_fire_stone_image.draw(self.eevee.x - 50, 120)
        self.font.draw(self.eevee.x - 50 + 10, 110 + self.eevee.area, "%d" % self.eevee.item_num[self.FIRE_STONE], (0, 0, 0))
        self.item_electric_stone_image.draw(self.eevee.x, 120)
        self.font.draw(self.eevee.x + 10, 110 + self.eevee.area, "%d" % self.eevee.item_num[self.ELECTRIC_STONE], (0, 0, 0))
        self.item_water_stone_image.draw(self.eevee.x + 50, 120)
        self.font.draw(self.eevee.x + 50 + 10, 110 + self.eevee.area, "%d" % self.eevee.item_num[self.WATER_STONE], (0, 0, 0))
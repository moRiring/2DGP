from pico2d import *

from Item import TreeFruit, Key

class UI:
    font = None

    item_fruit = None
    item_key = None

    def __init__(self):
        if UI.font == None:
            UI.font = load_font('soya8.ttf', 20)
        if UI.item_fruit == None:
            UI.item_fruit = TreeFruit()
            UI.item_fruit.x = 500
            UI.item_fruit.y = 280
        if UI.item_key == None:
            UI.item_key = Key()
            UI.item_key.x = 550
            UI.item_key.y = 280

    def draw(self, eevee):
        self.draw_item(eevee)

    def draw_item(self, eevee):
        self.item_fruit.draw_ui()
        self.font.draw(520, 280, "%d" % eevee.item_num["fruit"], (0,0,0))
        self.item_key.draw_ui()
        self.font.draw(570, 280, "%d" % eevee.item_num["key"], (0, 0, 0))
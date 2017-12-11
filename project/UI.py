from pico2d import *

from  Eevee import Eevee
from Item import Item

class UI:
    font = None

    item_fruit = None
    item_key = None



    def __init__(self):
        if UI.font == None:
            UI.font = load_font('soya8.ttf', 20)
        if UI.item_fruit == None:
            UI.item_fruit = Item(Item.FRUIT)
            UI.item_fruit.x = 550
            UI.item_fruit.y = 280

    def set_eevee(self, eevee):
        self.eevee = eevee

    def draw(self, eevee):
        self.draw_item()

    def draw_item(self):
        self.item_fruit.draw_ui()
        self.font.draw(575, 280, "%d" % self.eevee.item_num["fruit"], (0,0,0))
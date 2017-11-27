from pico2d import *

class Item:
    FRUIT, KEY = 0, 1
    NONE, GET = 0, 1

    image = None
    right = 0
    type = None

    ITEM = 0

    def __init__(self, y):
        Item.w = 40
        Item.h = 40
        self.x = 100
        self.y = 100
        self.state = self.GET

    def draw(self, right):
        self.right = right
        if self.state == self.GET:
            self.image.opacify(0)
        #self.draw_bb()
        self.image.draw(640 - (self.right - self.x), self.y)
        self.image.opacify(1)

    def draw_ui(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return 640 - (self.right - self.x) - 20, self.y - 20, 640 - (self.right - self.x) + 20, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get(self):
        self.state = self.GET


class TreeFruit(Item):

    image = None

    def __init__(self):
        self.type = self.FRUIT
        self.state = self.NONE
        self.state = self.NONE
        self.object_TYPE = self.ITEM
        if TreeFruit.image == None:
            TreeFruit.image = load_image('resource/Tree_Fruit.png')


class Key(Item):

    image = None

    def __init__(self):
        self.type = self.KEY
        self.state = self.NONE
        self.state = self.NONE
        self.object_TYPE = self.ITEM
        if Key.image == None:
            Key.image = load_image('resource/Key.png')
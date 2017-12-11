from pico2d import *

class Item:
    object_TYPE = "ITEM"

    FRUIT, KEY = 0, 1
    NONE, GET = 0, 1

    image = None
    map = None
    type = None

    key_image = None
    fruit_image = None
    firestone_image = None

    def __init__(self, type):
        self.state = self.NONE
        self.total_frames = 0.0

        if Item.fruit_image == None:
            Item.fruit_image = load_image('resource/Tree_Fruit.png')
        if Item.key_image == None:
            Item.key_image = load_image('resource/Key.png')

        if type == self.FRUIT:
            self.type = self.FRUIT
            self.image = Item.fruit_image
        elif type == self.KEY:
            self.type = self.KEY
            self.image = Item.key_image


    def set_map(self, map):
        Item.map = map

    def draw(self):
        right = self.map.right

        if self.state == self.GET:
            self.image.opacify(0)

        self.draw_bb()

        self.image.draw(640 - (right - self.x), self.y)

        self.image.opacify(1)

    def draw_ui(self):
        if self.type == self.FRUIT:
            self.fruit_image.draw(self.x, self.y)
        if self.type == self.KEY:
            self.key_image.draw(self.x, self.y)

    def get_bb(self):
        right = self.map.right

        return 640 - (right - self.x) - 10, self.y - 10, 640 - (right - self.x) + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        pass

    def get(self):
        self.state = self.GET

        if self.type == self.KEY:
            self.type = self.FRUIT

            type_table = {
                self.FRUIT:self.fruit_image,
            }

            self.image = type_table[self.type]
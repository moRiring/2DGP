from pico2d import *
import random

class Item:
    object_TYPE = "ITEM"

    KEY, FRUIT, FIRE_STONE, ELECTRIC_STONE, WATER_STONE = 0, 1, 2, 3, 4
    NONE, GET = 0, 1

    image = None
    map = None
    type = None

    key_image = None
    fruit_image = None
    firestone_image = None
    electricstone_image = None
    waterstone_image = None

    def __init__(self, type):
        self.state = self.NONE
        self.total_frames = 0.0

        if Item.fruit_image == None:
            Item.fruit_image = load_image('resource/Tree_Fruit.png')
        if Item.key_image == None:
            Item.key_image = load_image('resource/Key.png')
        if Item.firestone_image == None:
            Item.firestone_image = load_image('resource/fire_stone.png')
        if Item.electricstone_image == None:
            Item.electricstone_image = load_image('resource/electric_stone.png')
        if Item.waterstone_image == None:
            Item.waterstone_image = load_image('resource/water_stone.png')

        if type == self.FRUIT:
            self.type = self.FRUIT
            self.image = Item.fruit_image
        elif type == self.KEY:
            self.type = self.KEY
            self.image = Item.key_image
        elif type == self.FIRE_STONE:
            self.type = self.FIRE_STONE
            self.image = Item.firestone_image
        elif type == self.ELECTRIC_STONE:
            self.type = self.ELECTRIC_STONE
            self.image = Item.electricstone_image
        elif type == self.waterstone_image:
            self.type = self.WATER_STONE
            self.image = Item.waterstone_image


    def set_map(self, map):
        Item.map = map

    def draw(self):
        right = self.map.right

        if self.state == self.GET:
            self.image.opacify(0)

        #self.draw_bb()

        self.image.draw(640 - (right - self.x), self.y)

        self.image.opacify(1)


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
        elif self.type in (self.FIRE_STONE, self.ELECTRIC_STONE, self.WATER_STONE):
            type_table = {
                self.FIRE_STONE: self.firestone_image,
                self.ELECTRIC_STONE: self.electricstone_image,
                self.WATER_STONE: self.waterstone_image
            }
            self.type = random.randint(self.FIRE_STONE, self.WATER_STONE)
            self.image = type_table[self.type]
import json

from Item import Item
from Moster import Monster

class Map:

    PIXEL_PER_METER = (10.0 / 0.3)

    MOVE_SPEED_KMPH = 50.0
    MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
    MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
    MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)

    map = []

    def __init__(self):
        self.map = []
        self.create_map()
        self.left = -40
        self.right = 640

        item = Item(0)
        item.set_map(self)
        del item

        monster = Monster(0)
        monster.set_map(self)
        del monster

    def create_map(self):

        map_data_file = open('map_data.json').read()
        map_data = json.loads(map_data_file)

        item_table = {
            "FRUIT": Item.FRUIT,
            "KEY": Item.KEY,
            "FIRE_STONE": Item.FIRE_STONE,
            "ELECTRIC_STONE":Item.ELECTRIC_STONE,
            "WATER_STONE": Item.WATER_STONE
        }

        monster_table = {
            "DIGLETT" : Monster.DIGLETT,
            "PIDGEOT" : Monster.PIDGEOT
        }

        for data in map_data:
            if data['Object'] == 'ITEM':
                new_data = Item(item_table[data['Type']])
            elif data['Object'] == 'MONSTER':
                new_data = Monster(monster_table[data['Type']])
            new_data.x = data['x']
            new_data.y = data['y']
            self.map.append(new_data)

    def draw(self):
        for data in self.map:
            if self.left < data.x and data.x < self.right:
                data.draw()


    def update(self, frame_time):
        distance = self.MOVE_SPEED_PPS * frame_time
        self.right = (int)(self.right + distance)
        self.left = (int)(self.left + distance)

        for data in self.map:
            data.update(frame_time)

        if 6000 < self.right:
            self.left = -40
            self.right = 640
            for data in self.map:
                data.state = 0

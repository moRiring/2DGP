import json

from Item import Item
from Moster import Moster

class Map:

    PIXEL_PER_METER = (10.0 / 0.3)

    MOVE_SPEED_KMPH = 40.0
    MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
    MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
    MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)

    map = []

    def __init__(self):
        self.create_map()
        self.left = -40
        self.right = 640

        item = Item(0)
        item.set_map(self)
        del item

        monster = Moster(0)
        monster.set_map(self)
        del monster

    def create_map(self):
        map_data_file = '                                                   \
        [                                                               \
            {"Object": "ITEM", "Type" : "KEY", "x" : 600, "y" : 50}, \
            {"Object": "ITEM", "Type" : "FRUIT", "x" : 1000, "y" : 150}, \
            {"Object": "MONSTER", "Type" : "RATTATA", "x" : 1500, "y" : 50} \
        ]                                                                \
        '

        map_data = json.loads(map_data_file)

        #map_data_file = (str)(open('map_data.json', 'r'))
        #map_data = json.loads(map_data_file)
        #map_data_file.close()

        item_table = {
            "FRUIT": Item.FRUIT,
            "KEY": Item.KEY
        }

        monster_table = {
            "RATTATA" : Moster.RATTATA
        }

        for data in map_data:
            if data['Object'] == 'ITEM':
                new_data = Item(item_table[data['Type']])
            elif data['Object'] == 'MONSTER':
                new_data = Moster(monster_table[data['Type']])
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

        if 3000 < self.right:
            self.left = -40
            self.right = 640
            for data in self.map:
                data.state = 0

import json

import Item

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


    def create_map(self):
        map_data_file = '                                                   \
        {                                                                \
            "num1" : {"Object": "ITEM", "Type" : "KEY", "x" : 600, "y" : 50}, \
    	    "num2" : {"Object": "ITEM", "Type" : "FRUIT", "x" : 1000, "y" : 150} \
        }                                                                \
        '
        #map_data_file = (str)(open('map_data.txt', 'r'))
        map_data = json.loads(map_data_file)
        #map_data_file.close()

        item_table = {
            "FRUIT": Item.TreeFruit(),
            "KEY": Item.Key()
        }

        for data in map_data:
            data_name = data
            if map_data[data_name]['Object'] == 'ITEM':
                data = item_table[map_data[data_name]['Type']]
                data.x = map_data[data_name]['x']
                data.y = map_data[data_name]['y']
                self.map.append(data)
            elif map_data[data_name]['Object'] == 'MONSTER':
                pass


    def draw(self):
        for data in self.map:
            if self.left < data.x and data.x < self.right:
                data.draw(self.right)


    def update(self, frame_time):
        distance = self.MOVE_SPEED_PPS * frame_time
        self.right = (int)(self.right + distance)
        self.left = (int)(self.left + distance)
        if 2000 < self.right:
            self.left = -40
            self.right = 640
            for data in self.map:
                data.state = 0

import random
import json
from pico2d import *

hp_jelly_file1 = open('Stage_Data\\Stage1_Hp_jelly.txt', 'r')
hp_jelly = json.load(hp_jelly_file1)
hp_jelly_file1.close()


class Stage1_SPEED:

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Stage2_SPEED:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 30.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Stage3_SPEED:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 30.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Stage4_SPEED:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 40.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Stage1_Item_Jelly:
    image = None

    def __init__(self):
        self.x = random.randint(300, 8700)
        self.y = random.randint(170, 300)
        if Stage1_Item_Jelly.image == None:
            self.Item_Jelly = load_image('Resource\\Item\\item_Jelly.png')

    def update(self, frame_time):
        if Stage1_SPEED.RUN_SPEED_PPS * frame_time < 12:
            self.distance = Stage1_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Item_Jelly.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20


class Stage1_Hp_Jelly:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage1_Hp_Jelly.image == None:
            self.Hp_Jelly = load_image('Resource\\Item\\hp_jelly.png')

    def create(self):
        hp_state_table = {
            "Hp" : self.Hp_Jelly
        }

        hp = []
        for name in hp_jelly:
            item = Stage1_Hp_Jelly()
            item.name = name
            item.x = hp_jelly[name]['x']
            item.y = hp_jelly[name]['y']
            item.state = hp_state_table[hp_jelly[name]['state']]
            hp.append(item)

        return hp

    def update(self, frame_time):
        if Stage1_SPEED.RUN_SPEED_PPS * frame_time < 12:
            self.distance = Stage1_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Hp_Jelly.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
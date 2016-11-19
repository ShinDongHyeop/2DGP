import random
import json
from pico2d import *


############################ Stage1 Item ###################################
hp_jelly_data1 = open('Stage_Data\\Stage1_Hp_Jelly.txt', 'r')
hp_jelly = json.load(hp_jelly_data1)
hp_jelly_data1.close()

score_jelly_data1 = open('Stage_Data\\Stage1_Score_Jelly.txt', 'r')
score_jelly = json.load(score_jelly_data1)
score_jelly_data1.close()

############################ Stage2 Item ###################################
hp_jelly_data2 = open('Stage_Data\\Stage2_Hp_Jelly.txt', 'r')
hp_jelly2 = json.load(hp_jelly_data2)
hp_jelly_data2.close()

score_jelly_data2 = open('Stage_Data\\Stage2_Score_Jelly.txt', 'r')
score_jelly2 = json.load(score_jelly_data2)
score_jelly_data2.close()

############################ Stage3 Item ###################################
hp_jelly_data3 = open('Stage_Data\\Stage3_Hp_Jelly.txt', 'r')
hp_jelly3 = json.load(hp_jelly_data3)
hp_jelly_data3.close()

score_jelly_data3 = open('Stage_Data\\Stage3_Score_Jelly.txt', 'r')
score_jelly3 = json.load(score_jelly_data3)
score_jelly_data3.close()

############################ Stage4 Item ###################################
hp_jelly_data4 = open('Stage_Data\\Stage4_Hp_Jelly.txt', 'r')
hp_jelly4 = json.load(hp_jelly_data4)
hp_jelly_data4.close()

score_jelly_data4 = open('Stage_Data\\Stage4_Score_Jelly.txt', 'r')
score_jelly4 = json.load(score_jelly_data4)
score_jelly_data4.close()

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

class Stage1_Score_Jelly:
    image = None

    def __init__(self):
        self.x = random.randint(300, 8700)
        self.y = random.randint(170, 300)
        self.collision_time = 0
        self.state = "None"
        if Stage1_Score_Jelly.image == None:
            self.Score_Jelly = load_image('Resource\\Item\\item_Jelly.png')

    def create(self):
        score_state_table = {
            "Jelly" : self.Score_Jelly
        }

        score = []
        for name in score_jelly:
            item = Stage1_Score_Jelly()
            item.name = name
            item.x = score_jelly[name]['x']
            item.y = score_jelly[name]['y']
            item.state = score_state_table[score_jelly[name]['state']]
            score.append(item)

        return score

    def update(self, frame_time):
        if Stage1_SPEED.RUN_SPEED_PPS * frame_time < 12 and self.state != "Collide":
            self.distance = Stage1_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance
            self.collision_time = 0

        elif self.state == "Collide":
            if self.collision_time < 30:
                self.collision_time += 10
                for i in range(2):
                   if self.x > 150:
                      self.x += 20
                   else:
                     self.x -= 20

    def draw(self):
        self.Score_Jelly.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

class Stage1_Hp_Jelly:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        self.state = "None"
        self.collision_time = 0
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
        if Stage1_SPEED.RUN_SPEED_PPS * frame_time < 12 and self.state != "Collide":
            self.distance = Stage1_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance
            self.collision_time = 0

        elif self.state == "Collide":
            if self.collision_time < 30:
                self.collision_time += 10
                for i in range(2):
                   if self.x > 150:
                      self.x += 20
                   else:
                     self.x -= 20

    def draw(self):
        self.Hp_Jelly.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20


class Stage2_Score_Jelly:
    image = None

    def __init__(self):
        self.x = random.randint(300, 15000)
        self.y = random.randint(170, 300)
        if Stage2_Score_Jelly.image == None:
            self.Score_Jelly = load_image('Resource\\Item\\item_Jelly.png')

    def create(self):
        score_state_table = {
            "Jelly" : self.Score_Jelly
        }

        score = []
        for name in score_jelly2:
            item = Stage2_Score_Jelly()
            item.name = name
            item.x = score_jelly2[name]['x']
            item.y = score_jelly2[name]['y']
            item.state = score_state_table[score_jelly2[name]['state']]
            score.append(item)

        return score

    def update(self, frame_time):
        if Stage2_SPEED.RUN_SPEED_PPS * frame_time < 18:
            self.distance = Stage2_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Score_Jelly.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

class Stage2_Hp_Jelly:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage2_Hp_Jelly.image == None:
            self.Hp_Jelly = load_image('Resource\\Item\\hp_jelly.png')

    def create(self):
        hp_state_table = {
            "Hp" : self.Hp_Jelly
        }

        hp = []
        for name in hp_jelly2:
            item = Stage2_Hp_Jelly()
            item.name = name
            item.x = hp_jelly2[name]['x']
            item.y = hp_jelly2[name]['y']
            item.state = hp_state_table[hp_jelly2[name]['state']]
            hp.append(item)

        return hp

    def update(self, frame_time):
        if Stage2_SPEED.RUN_SPEED_PPS * frame_time < 18:
            self.distance = Stage2_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Hp_Jelly.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20


class Stage3_Score_Jelly:
    image = None

    def __init__(self):
        self.x = random.randint(300, 15000)
        self.y = random.randint(170, 300)
        if Stage3_Score_Jelly.image == None:
            self.Score_Jelly = load_image('Resource\\Item\\item_Jelly.png')

    def update(self, frame_time):
        if Stage3_SPEED.RUN_SPEED_PPS * frame_time < 24:
            self.distance = Stage3_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def create(self):
        score_state_table = {
            "Jelly" : self.Score_Jelly
        }

        score = []
        for name in score_jelly3:
            item = Stage3_Score_Jelly()
            item.name = name
            item.x = score_jelly3[name]['x']
            item.y = score_jelly3[name]['y']
            item.state = score_state_table[score_jelly3[name]['state']]
            score.append(item)

        return score

    def draw(self):
        self.Score_Jelly.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

class Stage3_Hp_Jelly:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage3_Hp_Jelly.image == None:
            self.Hp_Jelly = load_image('Resource\\Item\\hp_jelly.png')

    def create(self):
        hp_state_table = {
            "Hp" : self.Hp_Jelly
        }

        hp = []
        for name in hp_jelly3:
            item = Stage3_Hp_Jelly()
            item.name = name
            item.x = hp_jelly3[name]['x']
            item.y = hp_jelly3[name]['y']
            item.state = hp_state_table[hp_jelly3[name]['state']]
            hp.append(item)

        return hp

    def update(self, frame_time):
        if Stage3_SPEED.RUN_SPEED_PPS * frame_time < 24:
            self.distance = Stage3_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Hp_Jelly.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20


class Stage4_Score_Jelly:
    image = None

    def __init__(self):
        self.x = random.randint(300, 18700)
        self.y = random.randint(170, 300)
        if Stage4_Score_Jelly.image == None:
            self.Score_Jelly = load_image('Resource\\Item\\item_Jelly.png')

    def create(self):
        score_state_table = {
            "Jelly" : self.Score_Jelly
        }

        score = []
        for name in score_jelly4:
            item = Stage4_Score_Jelly()
            item.name = name
            item.x = score_jelly4[name]['x']
            item.y = score_jelly4[name]['y']
            item.state = score_state_table[score_jelly4[name]['state']]
            score.append(item)

        return score

    def update(self, frame_time):
        if Stage4_SPEED.RUN_SPEED_PPS * frame_time < 24:
            self.distance = Stage4_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Score_Jelly.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

class Stage4_Hp_Jelly:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage4_Hp_Jelly.image == None:
            self.Hp_Jelly = load_image('Resource\\Item\\hp_jelly.png')

    def create(self):
        hp_state_table = {
            "Hp" : self.Hp_Jelly
        }

        hp = []
        for name in hp_jelly4:
            item = Stage4_Hp_Jelly()
            item.name = name
            item.x = hp_jelly4[name]['x']
            item.y = hp_jelly4[name]['y']
            item.state = hp_state_table[hp_jelly4[name]['state']]
            hp.append(item)

        return hp

    def update(self, frame_time):
        if Stage4_SPEED.RUN_SPEED_PPS * frame_time < 24:
            self.distance = Stage4_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Hp_Jelly.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
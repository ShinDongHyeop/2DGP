from pico2d import *
import json

running = None

board_data_file1 = open('Stage_Data\\Stage1_Board.txt', 'r')
board_data1 = json.load(board_data_file1)
board_data_file1.close()

board_data_file2 = open('Stage_Data\\Stage2_Board.txt', 'r')
board_data2 = json.load(board_data_file2)
board_data_file2.close()


########################## Stage1_Obstacle #################################
obstacle_data_file1_1 = open('Stage_Data\\Stage1_NomalFork.txt', 'r')
obstacle_data1_1 = json.load(obstacle_data_file1_1)
obstacle_data_file1_1.close()

obstacle_data_file1_2 = open('Stage_Data\\Stage1_NomalThorn.txt', 'r')
obstacle_data1_2 = json.load(obstacle_data_file1_2)
obstacle_data_file1_2.close()

obstacle_data_file1_3 = open('Stage_Data\\Stage1_SpecialFork.txt', 'r')
obstacle_data1_3 = json.load(obstacle_data_file1_3)
obstacle_data_file1_3.close()

obstacle_data_file1_4 = open('Stage_Data\\Stage1_DoubleThorn.txt', 'r')
obstacle_data1_4 = json.load(obstacle_data_file1_4)
obstacle_data_file1_4.close()


########################## Stage2_Obstacle #################################
obstacle_data_file2_1 = open('Stage_Data\\Stage2_BrownSpear.txt', 'r')
obstacle_data2_1 = json.load(obstacle_data_file2_1)
obstacle_data_file2_1.close()

obstacle_data_file2_2 = open('Stage_Data\\Stage2_Thorn.txt', 'r')
obstacle_data2_2 = json.load(obstacle_data_file2_2)
obstacle_data_file2_2.close()

obstacle_data_file2_3 = open('Stage_Data\\Stage2_OatmealSpear.txt', 'r')
obstacle_data2_3 = json.load(obstacle_data_file2_3)
obstacle_data_file2_3.close()

obstacle_data_file2_4 = open('Stage_Data\\Stage2_NastyThorn.txt', 'r')
obstacle_data2_4 = json.load(obstacle_data_file2_4)
obstacle_data_file2_4.close()


########################## Stage3_Obstacle #################################
obstacle_data_file3_1 = open('Stage_Data\\Stage3_PalmTree.txt', 'r')
obstacle_data3_1 = json.load(obstacle_data_file3_1)
obstacle_data_file3_1.close()

obstacle_data_file3_2 = open('Stage_Data\\Stage3_Fence.txt', 'r')
obstacle_data3_2 = json.load(obstacle_data_file3_2)
obstacle_data_file3_2.close()

obstacle_data_file3_3 = open('Stage_Data\\Stage3_HatePalmTree.txt', 'r')
obstacle_data3_3 = json.load(obstacle_data_file3_3)
obstacle_data_file3_3.close()

obstacle_data_file3_4 = open('Stage_Data\\Stage3_Conch.txt', 'r')
obstacle_data3_4 = json.load(obstacle_data_file3_4)
obstacle_data_file3_4.close()

########################## Stage4_Obstacle #################################
obstacle_data_file4_1 = open('Stage_Data\\Stage4_DirtyTotem.txt', 'r')
obstacle_data4_1 = json.load(obstacle_data_file4_1)
obstacle_data_file4_1.close()

obstacle_data_file4_2 = open('Stage_Data\\Stage4_BlueFlower.txt', 'r')
obstacle_data4_2 = json.load(obstacle_data_file4_2)
obstacle_data_file4_2.close()

obstacle_data_file4_3 = open('Stage_Data\\Stage4_Totem.txt', 'r')
obstacle_data4_3 = json.load(obstacle_data_file4_3)
obstacle_data_file4_3.close()

obstacle_data_file4_4 = open('Stage_Data\\Stage4_RedFlower.txt', 'r')
obstacle_data4_4 = json.load(obstacle_data_file4_4)
obstacle_data_file4_4.close()

############################# Stage1 ########################################
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

class Stage1_Board:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage1_Board.image == None:
            self.Board = load_image('Resource\\Map\\Board.png')

    def create(self):
        board_state_table = {
            "Board" : self.Board
        }

        board = []
        for name in board_data1:
            ob = Stage1_Board()
            ob.name = name
            ob.x = board_data1[name]['x']
            ob.y = board_data1[name]['y']
            ob.state = board_state_table[board_data1[name]['state']]
            board.append(ob)

        return board

    def update(self, frame_time):
        if Stage1_SPEED.RUN_SPEED_PPS * frame_time < 12:
            self.distance = Stage1_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Board.clip_draw(0, 0, 150, 10, self.x, self.y)

class Stage1_Nomal_Fork:
    image = None
    state = "None"

    def __init__(self):
        self.x = 0
        self.y = 0
        self.collision_time = 0
        if Stage1_Nomal_Fork.image == None:
            self.Fork = load_image('Resource\\Map\\Stage1\\Stage1_Fork.png')

    def create(self):
        obstacle_state_table = {
            "Fork" : self.Fork
        }
        obstacle = []
        for name in obstacle_data1_1:
            ob = Stage1_Nomal_Fork()
            ob.name = name
            ob.x = obstacle_data1_1[name]['x']
            ob.y = obstacle_data1_1[name]['y']
            ob.state = obstacle_state_table[obstacle_data1_1[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if Stage1_SPEED.RUN_SPEED_PPS * frame_time < 12:
            self.distance = Stage1_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance
            self.collision_time = 0

    def draw(self):
        self.Fork.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 220, self.x + 40, self.y + 300

class Stage1_Special_Fork:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage1_Special_Fork.image == None:
            self.Fork = load_image('Resource\\Map\\Stage1\\Stage1_Fork2.png')

    def create(self):
        obstacle_state_table = {
            "Fork": self.Fork
        }

        obstacle = []
        for name in obstacle_data1_3:
            ob = Stage1_Special_Fork()
            ob.name = name
            ob.x = obstacle_data1_3[name]['x']
            ob.y = obstacle_data1_3[name]['y']
            ob.state = obstacle_state_table[obstacle_data1_3[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if Stage1_SPEED.RUN_SPEED_PPS * frame_time < 12:
            self.distance = Stage1_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Fork.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 220, self.x + 40, self.y + 300


class Stage1_Nomal_Thorn:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage1_Nomal_Thorn.image == None:
            self.Thorn = load_image('Resource\\Map\\Stage1\\Stage1_thorn3.png')

    def create(self):
        obstacle_state_table = {
            "Thorn": self.Thorn
        }

        obstacle = []
        for name in obstacle_data1_2:
            ob = Stage1_Nomal_Thorn()
            ob.name = name
            ob.x = obstacle_data1_2[name]['x']
            ob.y = obstacle_data1_2[name]['y']
            ob.state = obstacle_state_table[obstacle_data1_2[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if Stage1_SPEED.RUN_SPEED_PPS * frame_time < 12:
            self.distance = Stage1_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Thorn.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

class Stage1_Double_Thorn:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage1_Double_Thorn.image == None:
            self.Thorn = load_image('Resource\\Map\\Stage1\\Stage1_thorn2.png')

    def create(self):
        obstacle_state_table = {
            "Thorn": self.Thorn
        }

        obstacle = []
        for name in obstacle_data1_4:
            ob = Stage1_Double_Thorn()
            ob.name = name
            ob.x = obstacle_data1_4[name]['x']
            ob.y = obstacle_data1_4[name]['y']
            ob.state = obstacle_state_table[obstacle_data1_4[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if Stage1_SPEED.RUN_SPEED_PPS * frame_time < 12:
            self.distance = Stage1_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Thorn.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 50


#################################### Stage 2 #################################################
class Stage2_Board:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage2_Board.image == None:
            self.Board = load_image('Resource\\Map\\Board.png')

    def create(self):
        board_state_table = {
            "Board": self.Board
        }

        board = []
        for name in board_data2:
            ob = Stage2_Board()
            ob.name = name
            ob.x = board_data2[name]['x']
            ob.y = board_data2[name]['y']
            ob.state = board_state_table[board_data2[name]['state']]
            board.append(ob)

        return board

    def update(self, frame_time):
        if Stage2_SPEED.RUN_SPEED_PPS * frame_time < 18:
            self.distance = Stage2_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Board.clip_draw(0, 0, 150, 10, self.x, self.y)

class Stage2_Brown_Spear:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage2_Brown_Spear.image == None:
            self.Spear = load_image('Resource\\Map\\Stage2\\Stage2_Spear.png')

    def create(self):
        obstacle_state_table = {
            "Fork" : self.Spear
        }
        obstacle = []
        for name in obstacle_data2_1:
            ob = Stage2_Brown_Spear()
            ob.name = name
            ob.x = obstacle_data2_1[name]['x']
            ob.y = obstacle_data2_1[name]['y']
            ob.state = obstacle_state_table[obstacle_data2_1[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if Stage2_SPEED.RUN_SPEED_PPS * frame_time < 18:
            self.distance = Stage2_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Spear.draw(self.x, self.y)

class Stage2_Oatmeal_Spear:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage2_Oatmeal_Spear.image == None:
            self.Spear = load_image('Resource\\Map\\Stage2\\Stage2_Spear2.png')

    def create(self):
        obstacle_state_table = {
            "Fork": self.Spear
        }
        obstacle = []
        for name in obstacle_data2_3:
            ob = Stage2_Oatmeal_Spear()
            ob.name = name
            ob.x = obstacle_data2_3[name]['x']
            ob.y = obstacle_data2_3[name]['y']
            ob.state = obstacle_state_table[obstacle_data2_3[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if Stage2_SPEED.RUN_SPEED_PPS * frame_time < 18:
            self.distance = Stage2_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Spear.draw(self.x, self.y)

class Stage2_Thorn:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage2_Thorn.image == None:
            self.Thorn = load_image('Resource\\Map\\Stage2\\Stage2_thorn.png')

    def create(self):
        obstacle_state_table = {
            "Thorn" : self.Thorn
        }
        obstacle = []
        for name in obstacle_data2_2:
            ob = Stage2_Thorn()
            ob.name = name
            ob.x = obstacle_data2_2[name]['x']
            ob.y = obstacle_data2_2[name]['y']
            ob.state = obstacle_state_table[obstacle_data2_2[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if Stage2_SPEED.RUN_SPEED_PPS * frame_time < 18:
            self.distance = Stage2_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Thorn.draw(self.x, self.y)

class Stage2_Nasty_Thorn:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage2_Nasty_Thorn.image == None:
            self.Thorn = load_image('Resource\\Map\\Stage2\\Stage2_thorn3.png')

    def create(self):
        obstacle_state_table = {
            "Thorn": self.Thorn
        }
        obstacle = []
        for name in obstacle_data2_4:
            ob = Stage2_Nasty_Thorn()
            ob.name = name
            ob.x = obstacle_data2_4[name]['x']
            ob.y = obstacle_data2_4[name]['y']
            ob.state = obstacle_state_table[obstacle_data2_4[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if Stage2_SPEED.RUN_SPEED_PPS * frame_time < 18:
            self.distance = Stage2_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Thorn.draw(self.x, self.y)

############################ Stage 3 ###############################################
class Stage3_Board:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage3_Board.image == None:
            self.Board = load_image('Resource\\Map\\Board.png')

    def create(self):
        board_state_table = {
            "Board" : self.Board
        }

        board = []
        for name in board_data2:
            ob = Stage3_Board()
            ob.name = name
            ob.x = board_data2[name]['x']
            ob.y = board_data2[name]['y']
            ob.state = board_state_table[board_data2[name]['state']]
            board.append(ob)

        return board

    def update(self, frame_time):
        if Stage3_SPEED.RUN_SPEED_PPS * frame_time < 18:
            self.distance = Stage3_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Board.clip_draw(0, 0, 150, 10, self.x, self.y)

class Stage3_Palm_Tree:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage3_Palm_Tree.image == None:
            self.Spear = load_image('Resource\\Map\\Stage3\\Stage3_Spear.png')

    def create(self):
        obstacle_state_table = {
            "Fork" : self.Spear
        }
        obstacle = []
        for name in obstacle_data3_1:
            ob = Stage3_Palm_Tree()
            ob.name = name
            ob.x = obstacle_data3_1[name]['x']
            ob.y = obstacle_data3_1[name]['y']
            ob.state = obstacle_state_table[obstacle_data3_1[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if Stage3_SPEED.RUN_SPEED_PPS * frame_time < 18:
            self.distance = Stage3_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Spear.draw(self.x, self.y)

class Stage3_Hate_Palm_Tree:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage3_Hate_Palm_Tree.image == None:
            self.Spear = load_image('Resource\\Map\\Stage3\\Stage3_Spear2.png')

    def create(self):
        obstacle_state_table = {
            "Fork" : self.Spear
        }
        obstacle = []
        for name in obstacle_data3_3:
            ob = Stage3_Hate_Palm_Tree()
            ob.name = name
            ob.x = obstacle_data3_3[name]['x']
            ob.y = obstacle_data3_3[name]['y']
            ob.state = obstacle_state_table[obstacle_data3_3[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if Stage3_SPEED.RUN_SPEED_PPS * frame_time < 18:
            self.distance = Stage3_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Spear.draw(self.x, self.y)

class Stage3_Fence:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage3_Fence.image == None:
            self.Thorn = load_image('Resource\\Map\\Stage3\\Stage3_thorn.png')

    def create(self):
        obstacle_state_table = {
            "Thorn" : self.Thorn
        }

        obstacle = []
        for name in obstacle_data3_2:
            ob = Stage3_Fence()
            ob.name = name
            ob.x = obstacle_data3_2[name]['x']
            ob.y = obstacle_data3_2[name]['y']
            ob.state = obstacle_state_table[obstacle_data3_2[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if Stage3_SPEED.RUN_SPEED_PPS * frame_time < 18:
            self.distance = Stage3_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance
    def draw(self):
        self.Thorn.draw(self.x, self.y)

class Stage3_Conch:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage3_Conch.image == None:
            self.Thorn = load_image('Resource\\Map\\Stage3\\Stage3_thorn5.png')

    def create(self):
        obstacle_state_table = {
            "Thorn" : self.Thorn
        }

        obstacle = []
        for name in obstacle_data3_4:
            ob = Stage3_Conch()
            ob.name = name
            ob.x = obstacle_data3_4[name]['x']
            ob.y = obstacle_data3_4[name]['y']
            ob.state = obstacle_state_table[obstacle_data3_4[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if Stage3_SPEED.RUN_SPEED_PPS * frame_time < 18:
            self.distance = Stage3_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Thorn.draw(self.x, self.y)

############################ Stage 4 ###############################################

class Stage4_Dirty_Totem:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage4_Dirty_Totem.image == None:
            self.Spear = load_image('Resource\\Map\\Stage4\\Stage4_Spear.png')

    def create(self):
        obstacle_state_table = {
            "Fork" : self.Spear
        }
        obstacle = []
        for name in obstacle_data4_1:
            ob = Stage4_Dirty_Totem()
            ob.name = name
            ob.x = obstacle_data4_1[name]['x']
            ob.y = obstacle_data4_1[name]['y']
            ob.state = obstacle_state_table[obstacle_data4_1[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if Stage4_SPEED.RUN_SPEED_PPS * frame_time < 24:
            self.distance = Stage4_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Spear.draw(self.x, self.y)

class Stage4_Totem:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage4_Totem.image == None:
            self.Spear = load_image('Resource\\Map\\Stage4\\Stage4_Spear2.png')

    def create(self):
        obstacle_state_table = {
            "Fork": self.Spear
        }
        obstacle = []
        for name in obstacle_data4_3:
            ob = Stage4_Totem()
            ob.name = name
            ob.x = obstacle_data4_3[name]['x']
            ob.y = obstacle_data4_3[name]['y']
            ob.state = obstacle_state_table[obstacle_data4_3[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if Stage4_SPEED.RUN_SPEED_PPS * frame_time < 24:
            self.distance = Stage4_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Spear.draw(self.x, self.y)

class Stage4_Blue_Flower:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage4_Blue_Flower.image == None:
            self.Thorn = load_image('Resource\\Map\\Stage4\\Stage4_thorn3.png')

    def create(self):
        obstacle_state_table = {
            "Thorn" : self.Thorn
        }
        obstacle = []
        for name in obstacle_data4_2:
            ob = Stage4_Blue_Flower()
            ob.name = name
            ob.x = obstacle_data4_2[name]['x']
            ob.y = obstacle_data4_2[name]['y']
            ob.state = obstacle_state_table[obstacle_data4_2[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if Stage4_SPEED.RUN_SPEED_PPS * frame_time < 24:
            self.distance = Stage4_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Thorn.draw(self.x, self.y)

class Stage4_Red_Flower:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage4_Red_Flower.image == None:
            self.Thorn = load_image('Resource\\Map\\Stage4\\Stage4_thorn4.png')

    def create(self):
        obstacle_state_table = {
            "Thorn": self.Thorn
        }
        obstacle = []
        for name in obstacle_data4_4:
            ob = Stage4_Red_Flower()
            ob.name = name
            ob.x = obstacle_data4_4[name]['x']
            ob.y = obstacle_data4_4[name]['y']
            ob.state = obstacle_state_table[obstacle_data4_4[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        if Stage4_SPEED.RUN_SPEED_PPS * frame_time < 24:
            self.distance = Stage4_SPEED.RUN_SPEED_PPS * frame_time
            self.x -= self.distance

    def draw(self):
        self.Thorn.draw(self.x, self.y)
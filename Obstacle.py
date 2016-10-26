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


class Stage1_Board:
    image = None
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage1_Board.image == None:
            self.Board = load_image('Resource\\Map\\Board.png')

    def Board(self):
        self.Board()

    def create():
        board_state_table = {
            "Board" : Stage1_Board.Board
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
        distance = Stage1_Board.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.Board.clip_draw(0, 0, 150, 10, self.x, self.y)

class Stage1_NomalFork:
    image = None
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage1_NomalFork.image == None:
            self.Fork = load_image('Resource\\Map\\Stage1\\Stage1_Fork.png')

    def Fork(self):
        self.Fork()

    def create():
        obstacle_state_table = {
            "Fork" : Stage1_NomalFork.Fork
        }
        obstacle = []
        for name in obstacle_data1_1:
            ob = Stage1_NomalFork()
            ob.name = name
            ob.x = obstacle_data1_1[name]['x']
            ob.y = obstacle_data1_1[name]['y']
            ob.state = obstacle_state_table[obstacle_data1_1[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        distance = Stage1_NomalFork.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.Fork.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 220, self.x + 40, self.y + 300

class Stage1_SpecialFork:
    image = None
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage1_SpecialFork.image == None:
            self.Fork = load_image('Resource\\Map\\Stage1\\Stage1_Fork2.png')

    def Fork(self):
        self.Fork()

    def create():
        obstacle_state_table = {
            "Fork": Stage1_SpecialFork.Fork
        }

        obstacle = []
        for name in obstacle_data1_3:
            ob = Stage1_SpecialFork()
            ob.name = name
            ob.x = obstacle_data1_3[name]['x']
            ob.y = obstacle_data1_3[name]['y']
            ob.state = obstacle_state_table[obstacle_data1_3[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        distance = Stage1_SpecialFork.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.Fork.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 220, self.x + 40, self.y + 300


class Stage1_NomalThorn:
    image = None
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage1_NomalThorn.image == None:
            self.Thorn = load_image('Resource\\Map\\Stage1\\Stage1_thorn3.png')

    def Thorn(self):
        self.Thorn()

    def create():
        obstacle_state_table = {
            "Thorn": Stage1_NomalThorn.Thorn
        }

        obstacle = []
        for name in obstacle_data1_2:
            ob = Stage1_NomalThorn()
            ob.name = name
            ob.x = obstacle_data1_2[name]['x']
            ob.y = obstacle_data1_2[name]['y']
            ob.state = obstacle_state_table[obstacle_data1_2[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        distance = Stage1_NomalThorn.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.Thorn.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

class Stage1_DoubleThorn:
    image = None
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage1_DoubleThorn.image == None:
            self.Thorn = load_image('Resource\\Map\\Stage1\\Stage1_thorn2.png')

    def Thorn(self):
        self.Thorn()

    def create():
        obstacle_state_table = {
            "Thorn": Stage1_DoubleThorn.Thorn
        }

        obstacle = []
        for name in obstacle_data1_4:
            ob = Stage1_DoubleThorn()
            ob.name = name
            ob.x = obstacle_data1_4[name]['x']
            ob.y = obstacle_data1_4[name]['y']
            ob.state = obstacle_state_table[obstacle_data1_4[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        distance = Stage1_DoubleThorn.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.Thorn.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 50


#################################### Stage 2 #################################################
class Stage2_Board:
    image = None
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 30.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage2_Board.image == None:
            self.Board = load_image('Resource\\Map\\Board.png')

    def Board(self):
        self.Board()

    def create():
        board_state_table = {
            "Board": Stage2_Board.Board
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
        distance = Stage2_Board.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.Board.clip_draw(0, 0, 150, 10, self.x, self.y)

class Stage2_BrownSpear:
    image = None
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 30.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage2_BrownSpear.image == None:
            self.Spear = load_image('Resource\\Map\\Stage2\\Stage2_Spear.png')

    def Spear(self):
        self.Spear()

    def create():
        obstacle_state_table = {
            "Fork" : Stage2_BrownSpear.Spear
        }
        obstacle = []
        for name in obstacle_data2_1:
            ob = Stage2_BrownSpear()
            ob.name = name
            ob.x = obstacle_data2_1[name]['x']
            ob.y = obstacle_data2_1[name]['y']
            ob.state = obstacle_state_table[obstacle_data2_1[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        distance = Stage2_BrownSpear.RUN_SPEED_PPS * frame_time
        self.x -= distance
    def draw(self):
        self.Spear.draw(self.x, self.y)

class Stage2_OatmealSpear:
    image = None
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 30.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage2_OatmealSpear.image == None:
            self.Spear = load_image('Resource\\Map\\Stage2\\Stage2_Spear2.png')

    def Spear(self):
        self.Spear()

    def create():
        obstacle_state_table = {
            "Fork": Stage2_OatmealSpear.Spear
        }
        obstacle = []
        for name in obstacle_data2_3:
            ob = Stage2_OatmealSpear()
            ob.name = name
            ob.x = obstacle_data2_3[name]['x']
            ob.y = obstacle_data2_3[name]['y']
            ob.state = obstacle_state_table[obstacle_data2_3[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        distance = Stage2_OatmealSpear.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.Spear.draw(self.x, self.y)

class Stage2_Thorn:
    image = None
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 30.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage2_Thorn.image == None:
            self.Thorn = load_image('Resource\\Map\\Stage2\\Stage2_thorn.png')

    def Thorn(self):
        self.Thorn()

    def create():
        obstacle_state_table = {
            "Thorn" : Stage2_Thorn.Thorn
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
        distance = Stage2_Thorn.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.Thorn.draw(self.x, self.y)

class Stage2_NastyThorn:
    image = None
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 30.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage2_NastyThorn.image == None:
            self.Thorn = load_image('Resource\\Map\\Stage2\\Stage2_thorn3.png')

    def Thorn(self):
        self.Thorn()

    def create():
        obstacle_state_table = {
            "Thorn": Stage2_NastyThorn.Thorn
        }
        obstacle = []
        for name in obstacle_data2_4:
            ob = Stage2_NastyThorn()
            ob.name = name
            ob.x = obstacle_data2_4[name]['x']
            ob.y = obstacle_data2_4[name]['y']
            ob.state = obstacle_state_table[obstacle_data2_4[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        distance = Stage2_NastyThorn.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.Thorn.draw(self.x, self.y)

############################ Stage 3 ###############################################
class Stage3_Board:
    image = None
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 30.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage3_Board.image == None:
            self.Board = load_image('Resource\\Map\\Board.png')

    def Board(self):
        self.Board()

    def create():
        board_state_table = {
            "Board" : Stage3_Board.Board
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
        distance = Stage3_Board.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.Board.clip_draw(0, 0, 150, 10, self.x, self.y)

class Stage3_PalmTree:
    image = None
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 30.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage3_PalmTree.image == None:
            self.Spear = load_image('Resource\\Map\\Stage3\\Stage3_Spear.png')

    def Spear(self):
        self.Spear()

    def create():
        obstacle_state_table = {
            "Fork" : Stage3_PalmTree.Spear
        }
        obstacle = []
        for name in obstacle_data3_1:
            ob = Stage3_PalmTree()
            ob.name = name
            ob.x = obstacle_data3_1[name]['x']
            ob.y = obstacle_data3_1[name]['y']
            ob.state = obstacle_state_table[obstacle_data3_1[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        distance = Stage3_PalmTree.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.Spear.draw(self.x, self.y)

class Stage3_HatePalmTree:
    image = None
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 30.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage3_HatePalmTree.image == None:
            self.Spear = load_image('Resource\\Map\\Stage3\\Stage3_Spear2.png')

    def Spear(self):
        self.Spear()

    def create():
        obstacle_state_table = {
            "Fork" : Stage3_HatePalmTree.Spear
        }
        obstacle = []
        for name in obstacle_data3_3:
            ob = Stage3_HatePalmTree()
            ob.name = name
            ob.x = obstacle_data3_3[name]['x']
            ob.y = obstacle_data3_3[name]['y']
            ob.state = obstacle_state_table[obstacle_data3_3[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self, frame_time):
        distance = Stage3_HatePalmTree.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.Spear.draw(self.x, self.y)

class Stage3_Fence:
    image = None
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 30.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage3_Fence.image == None:
            self.Thorn = load_image('Resource\\Map\\Stage3\\Stage3_thorn.png')

    def Thorn(self):
        self.Thorn()

    def create():
        obstacle_state_table = {
            "Thorn" : Stage3_Fence.Thorn
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
        distance = Stage3_Fence.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.Thorn.draw(self.x, self.y)

class Stage3_Conch:
    image = None
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 30.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage3_Conch.image == None:
            self.Thorn = load_image('Resource\\Map\\Stage3\\Stage3_thorn5.png')

    def Thorn(self):
        self.Thorn()

    def create():
        obstacle_state_table = {
            "Thorn" : Stage3_Conch.Thorn
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
        distance = Stage3_Conch.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.Thorn.draw(self.x, self.y)
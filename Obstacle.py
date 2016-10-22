from pico2d import *
import json

running = None

board_data_file1 = open('Stage_Data\\Stage1_Board.txt', 'r')
board_data1 = json.load(board_data_file1)
board_data_file1.close()

board_data_file2 = open('Stage_Data\\Stage2_Board.txt', 'r')
board_data2 = json.load(board_data_file2)
board_data_file2.close()

obstacle_data_file1_1 = open('Stage_Data\\Stage1_Obstacle.txt', 'r')
obstacle_data1_1 = json.load(obstacle_data_file1_1)
obstacle_data_file1_1.close()

obstacle_data_file1_2 = open('Stage_Data\\Stage1_Obstacle2.txt', 'r')
obstacle_data1_2 = json.load(obstacle_data_file1_2)
obstacle_data_file1_2.close()

obstacle_data_file1_3 = open('Stage_Data\\Stage1_Obstacle3.txt', 'r')
obstacle_data1_3 = json.load(obstacle_data_file1_3)
obstacle_data_file1_3.close()

obstacle_data_file1_4 = open('Stage_Data\\Stage1_Obstacle4.txt', 'r')
obstacle_data1_4 = json.load(obstacle_data_file1_4)
obstacle_data_file1_4.close()

obstacle_data_file2_1 = open('Stage_Data\\Stage2_Obstacle.txt', 'r')
obstacle_data2_1 = json.load(obstacle_data_file2_1)
obstacle_data_file2_1.close()

obstacle_data_file2_2 = open('Stage_Data\\Stage2_Obstacle2.txt', 'r')
obstacle_data2_2 = json.load(obstacle_data_file2_2)
obstacle_data_file2_2.close()

obstacle_data_file2_3 = open('Stage_Data\\Stage2_Obstacle3.txt', 'r')
obstacle_data2_3 = json.load(obstacle_data_file2_3)
obstacle_data_file2_3.close()

obstacle_data_file2_4 = open('Stage_Data\\Stage2_Obstacle4.txt', 'r')
obstacle_data2_4 = json.load(obstacle_data_file2_4)
obstacle_data_file2_4.close()

obstacle_data_file3_1 = open('Stage_Data\\Stage3_Obstacle.txt', 'r')
obstacle_data3_1 = json.load(obstacle_data_file3_1)
obstacle_data_file3_1.close()

obstacle_data_file3_2 = open('Stage_Data\\Stage3_Obstacle2.txt', 'r')
obstacle_data3_2 = json.load(obstacle_data_file3_2)
obstacle_data_file3_2.close()

obstacle_data_file3_3 = open('Stage_Data\\Stage3_Obstacle3.txt', 'r')
obstacle_data3_3 = json.load(obstacle_data_file3_3)
obstacle_data_file3_3.close()

obstacle_data_file3_4 = open('Stage_Data\\Stage3_Obstacle4.txt', 'r')
obstacle_data3_4 = json.load(obstacle_data_file3_4)
obstacle_data_file3_4.close()

class Stage1_Board:
    image = None
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

    def update(self):
        self.x -= 5

    def draw(self):
        self.Board.clip_draw(0, 0, 150, 10, self.x, self.y)

class Stage1_Obstacle:
    image = None
    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage1_Obstacle.image == None:
            self.Fork1 = load_image('Resource\\Map\\Stage1\\Stage1_Fork.png')

    def Fork(self):
        self.Fork1()

    def create():
        obstacle_state_table = {
            "Fork" : Stage1_Obstacle.Fork
        }
        obstacle = []
        for name in obstacle_data1_1:
            ob = Stage1_Obstacle()
            ob.name = name
            ob.x = obstacle_data1_1[name]['x']
            ob.y = obstacle_data1_1[name]['y']
            ob.state = obstacle_state_table[obstacle_data1_1[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self):
        self.x -= 5

    def draw(self):
        self.Fork1.draw(self.x, self.y)

class Stage1_Obstacle2:
        image = None

        def __init__(self):
            self.x = 0
            self.y = 0
            if Stage1_Obstacle2.image == None:
                self.Thorn1 = load_image('Resource\\Map\\Stage1\\Stage1_thorn.png')

        def Thorn(self):
            self.Thorn1()

        def create():
            obstacle_state_table = {
                "Thorn": Stage1_Obstacle2.Thorn
            }

            obstacle = []
            for name in obstacle_data1_2:
                ob = Stage1_Obstacle2()
                ob.name = name
                ob.x = obstacle_data1_2[name]['x']
                ob.y = obstacle_data1_2[name]['y']
                ob.state = obstacle_state_table[obstacle_data1_2[name]['state']]
                obstacle.append(ob)

            return obstacle

        def update(self):
            self.x -= 5

        def draw(self):
            self.Thorn1.draw(self.x, self.y)

class Stage1_Obstacle3:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage1_Obstacle3.image == None:
            self.Fork = load_image('Resource\\Map\\Stage1\\Stage1_Fork2.png')

    def Fork(self):
        self.Fork()

    def create():
        obstacle_state_table = {
            "Fork": Stage1_Obstacle3.Fork
        }

        obstacle = []
        for name in obstacle_data1_3:
            ob = Stage1_Obstacle3()
            ob.name = name
            ob.x = obstacle_data1_3[name]['x']
            ob.y = obstacle_data1_3[name]['y']
            ob.state = obstacle_state_table[obstacle_data1_3[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self):
        self.x -= 5

    def draw(self):
        self.Fork.draw(self.x, self.y)

class Stage1_Obstacle4:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage1_Obstacle4.image == None:
            self.Thorn = load_image('Resource\\Map\\Stage1\\Stage1_thorn2.png')

    def Thorn(self):
        self.Thorn()

    def create():
        obstacle_state_table = {
            "Thorn": Stage1_Obstacle4.Thorn
        }

        obstacle = []
        for name in obstacle_data1_4:
            ob = Stage1_Obstacle4()
            ob.name = name
            ob.x = obstacle_data1_4[name]['x']
            ob.y = obstacle_data1_4[name]['y']
            ob.state = obstacle_state_table[obstacle_data1_4[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self):
        self.x -= 5

    def draw(self):
        self.Thorn.draw(self.x, self.y)


#################################### Stage 2 #################################################
class Stage2_Board:
    image = None
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

    def update(self):
        self.x -= 7

    def draw(self):
        self.Board.clip_draw(0, 0, 150, 10, self.x, self.y)

class Stage2_Obstacle:
    image = None
    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage2_Obstacle.image == None:
            self.Spear = load_image('Resource\\Map\\Stage2\\Stage2_Spear.png')

    def Spear(self):
        self.Spear()

    def create():
        obstacle_state_table = {
            "Fork" : Stage2_Obstacle.Spear
        }
        obstacle = []
        for name in obstacle_data2_1:
            ob = Stage2_Obstacle()
            ob.name = name
            ob.x = obstacle_data2_1[name]['x']
            ob.y = obstacle_data2_1[name]['y']
            ob.state = obstacle_state_table[obstacle_data2_1[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self):
        self.x -= 7

    def draw(self):
        self.Spear.draw(self.x, self.y)

class Stage2_Obstacle2:
    image = None
    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage2_Obstacle2.image == None:
            self.Thorn = load_image('Resource\\Map\\Stage2\\Stage2_thorn.png')

    def Thorn(self):
        self.Thorn()

    def create():
        obstacle_state_table = {
            "Thorn" : Stage2_Obstacle2.Thorn
        }
        obstacle = []
        for name in obstacle_data2_2:
            ob = Stage2_Obstacle2()
            ob.name = name
            ob.x = obstacle_data2_2[name]['x']
            ob.y = obstacle_data2_2[name]['y']
            ob.state = obstacle_state_table[obstacle_data2_2[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self):
        self.x -= 7

    def draw(self):
        self.Thorn.draw(self.x, self.y)

class Stage2_Obstacle3:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage2_Obstacle3.image == None:
            self.Spear = load_image('Resource\\Map\\Stage2\\Stage2_Spear2.png')

    def Spear(self):
        self.Spear()

    def create():
        obstacle_state_table = {
            "Fork": Stage2_Obstacle3.Spear
        }
        obstacle = []
        for name in obstacle_data2_3:
            ob = Stage2_Obstacle3()
            ob.name = name
            ob.x = obstacle_data2_3[name]['x']
            ob.y = obstacle_data2_3[name]['y']
            ob.state = obstacle_state_table[obstacle_data2_3[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self):
        self.x -= 7

    def draw(self):
        self.Spear.draw(self.x, self.y)

class Stage2_Obstacle4:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage2_Obstacle4.image == None:
            self.Thorn = load_image('Resource\\Map\\Stage2\\Stage2_thorn3.png')

    def Thorn(self):
        self.Thorn()

    def create():
        obstacle_state_table = {
            "Thorn": Stage2_Obstacle4.Thorn
        }
        obstacle = []
        for name in obstacle_data2_4:
            ob = Stage2_Obstacle4()
            ob.name = name
            ob.x = obstacle_data2_4[name]['x']
            ob.y = obstacle_data2_4[name]['y']
            ob.state = obstacle_state_table[obstacle_data2_4[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self):
        self.x -= 7

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

    def update(self):
        self.x -= 5

    def draw(self):
        self.Board.clip_draw(0, 0, 150, 10, self.x, self.y)

class Stage3_Obstacle:
    image = None
    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage3_Obstacle.image == None:
            self.Spear = load_image('Resource\\Map\\Stage3\\Stage3_Spear.png')

    def Spear(self):
        self.Spear()

    def create():
        obstacle_state_table = {
            "Fork" : Stage3_Obstacle.Spear
        }
        obstacle = []
        for name in obstacle_data3_1:
            ob = Stage3_Obstacle()
            ob.name = name
            ob.x = obstacle_data3_1[name]['x']
            ob.y = obstacle_data3_1[name]['y']
            ob.state = obstacle_state_table[obstacle_data3_1[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self):
        self.x -= 8

    def draw(self):
        self.Spear.draw(self.x, self.y)

class Stage3_Obstacle2:
    image = None
    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage3_Obstacle2.image == None:
            self.Thorn = load_image('Resource\\Map\\Stage3\\Stage3_thorn.png')

    def Thorn(self):
        self.Thorn()

    def create():
        obstacle_state_table = {
            "Thorn" : Stage3_Obstacle2.Thorn
        }

        obstacle = []
        for name in obstacle_data3_2:
            ob = Stage3_Obstacle2()
            ob.name = name
            ob.x = obstacle_data3_2[name]['x']
            ob.y = obstacle_data3_2[name]['y']
            ob.state = obstacle_state_table[obstacle_data3_2[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self):
        self.x -= 8

    def draw(self):
        self.Thorn.draw(self.x, self.y)

class Stage3_Obstacle3:
    image = None
    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage3_Obstacle3.image == None:
            self.Spear = load_image('Resource\\Map\\Stage3\\Stage3_Spear2.png')

    def Spear(self):
        self.Spear()

    def create():
        obstacle_state_table = {
            "Fork" : Stage3_Obstacle3.Spear
        }
        obstacle = []
        for name in obstacle_data3_3:
            ob = Stage3_Obstacle3()
            ob.name = name
            ob.x = obstacle_data3_3[name]['x']
            ob.y = obstacle_data3_3[name]['y']
            ob.state = obstacle_state_table[obstacle_data3_3[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self):
        self.x -= 8

    def draw(self):
        self.Spear.draw(self.x, self.y)

class Stage3_Obstacle4:
    image = None
    def __init__(self):
        self.x = 0
        self.y = 0
        if Stage3_Obstacle4.image == None:
            self.Thorn = load_image('Resource\\Map\\Stage3\\Stage3_thorn5.png')

    def Thorn(self):
        self.Thorn()

    def create():
        obstacle_state_table = {
            "Thorn" : Stage3_Obstacle4.Thorn
        }

        obstacle = []
        for name in obstacle_data3_4:
            ob = Stage3_Obstacle4()
            ob.name = name
            ob.x = obstacle_data3_4[name]['x']
            ob.y = obstacle_data3_4[name]['y']
            ob.state = obstacle_state_table[obstacle_data3_4[name]['state']]
            obstacle.append(ob)

        return obstacle

    def update(self):
        self.x -= 8

    def draw(self):
        self.Thorn.draw(self.x, self.y)
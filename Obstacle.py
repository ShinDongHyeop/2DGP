from pico2d import *
import json

running = None

obstacle_data_file1_1 = open('Stage_Data\\Stage1_Obstacle.txt', 'r')
obstacle_data1_1 = json.load(obstacle_data_file1_1)
obstacle_data_file1_1.close()

obstacle_data_file1_2 = open('Stage_Data\\Stage1_Obstacle2.txt', 'r')
obstacle_data1_2 = json.load(obstacle_data_file1_2)
obstacle_data_file1_2.close()

obstacle_data_file2_1 = open('Stage_Data\\Stage2_Obstacle.txt', 'r')
obstacle_data2_1 = json.load(obstacle_data_file2_1)
obstacle_data_file2_1.close()

obstacle_data_file2_2 = open('Stage_Data\\Stage2_Obstacle2.txt', 'r')
obstacle_data2_2 = json.load(obstacle_data_file2_2)
obstacle_data_file2_2.close()

obstacle_data_file3_1 = open('Stage_Data\\Stage3_Obstacle.txt', 'r')
obstacle_data3_1 = json.load(obstacle_data_file3_1)
obstacle_data_file3_1.close()

obstacle_data_file3_2 = open('Stage_Data\\Stage3_Obstacle2.txt', 'r')
obstacle_data3_2 = json.load(obstacle_data_file3_2)
obstacle_data_file3_2.close()

class Stage1_Obstacle():
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

class Stage1_Obstacle2():
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
            "Thorn" : Stage1_Obstacle2.Thorn
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

class Stage2_Obstacle():
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

class Stage2_Obstacle2():
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

class Stage3_Obstacle():
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
        self.x -= 10

    def draw(self):
        self.Spear.draw(self.x, self.y)

class Stage3_Obstacle2():
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
        self.x -= 10

    def draw(self):
        self.Thorn.draw(self.x, self.y)
'''
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def main():
    open_canvas()

    global running
    obstacle = Stage1_Obstacle.create()
    obstacle2 = Stage1_Obstacle2.create()
    running = True

    while running:
        handle_events()
        for i in obstacle:
            i.update()

        for i in obstacle2:
            i.update()

        clear_canvas()
        for i in obstacle:
            i.draw()
        for i in obstacle2:
            i.draw()

        update_canvas()

        delay(0.04)
    close_canvas()

if __name__ == '__main__':
    main()
'''
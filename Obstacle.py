from pico2d import *

class Stage1_Obstacle():
    global mapping
    image = None
    def __init__(self):
        self.x = 600
        self.y = 400
        self.xx = 500
        self.yy = 175
        if Stage1_Obstacle.image == None:
            self.Fork1 = load_image('Resource\\Map\\Stage1\\Stage1_Fork.png')
            self.Fork2 = load_image('Resource\\Map\\Stage1\\Stage1_Fork2.png')
            self.Thorn1 = load_image('Resource\\Map\\Stage1\\Stage1_Thorn.png')
            self.Thorn2 = load_image('Resource\\Map\\Stage1\\Stage1_Thorn2.png')
            self.Thorn3 = load_image('Resource\\Map\\Stage1\\Stage1_Thorn3.png')
            self.Thorn4 = load_image('Resource\\Map\\Stage1\\Stage1_Thorn4.png')
            self.Thorn5 = load_image('Resource\\Map\\Stage1\\Stage1_Thorn5.png')

    def coordinate(self, place):
        self.x *= place * 2 + 1
        self.xx *= place * 3 + 1

    def update(self):
        self.x -= 3
        self.xx -= 5

    def draw(self):
        self.Fork1.clip_draw(0, 0, 100, 400, self.x, self.y)
        self.Thorn1.clip_draw(0,0 ,50, 50, self.xx, self.yy)

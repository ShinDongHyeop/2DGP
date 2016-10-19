from pico2d import *

class Stage1_Background:
    def __init__(self):
        self.Background = load_image('Resource\\Map\\Stage1\\First_Background.png')
        self.Ground = load_image('Resource\\Map\\Stage1\\First_ground.png')

    def draw(self):
        self.Background.draw(400, 200)
        self.Ground.draw(400, 350)



class Stage2_Background:
    def __init__(self):
        self.Background = load_image('Resource\\Map\\Stage2\\Second_Background.png')
        self.Ground = load_image('Resource\\Map\\Stage2\\Second_ground.png')

    def draw(self):
        self.Background.draw(400, 200)


    def grounddraw(self):
        self.Ground.draw(400, 350)

class Stage3_Background:
    def __init__(self):
        self.Background = load_image('Resource\\Map\\Stage3\\Third_Background.png')
        self.Ground = load_image('Resource\\Map\\Stage3\\Third_ground.png')

    def draw(self):
        self.Background.draw(400, 200)
        self.Ground.draw(400, 350)

class Stage4_Background:
    def __init__(self):
        self.Background = load_image('Resource\\Map\\Stage4\\Fourth_Background.png')
        self.Ground = load_image('Resource\\Map\\Stage4\\Fourth_ground.png4')

    def draw(self):
        self.Background.draw(400, 200)
        self.Ground.draw(400, 350)

from pico2d import *
import os

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
        self.Ground.draw(400, 350)

class Stage3_Background:
    def __init__(self):
        self.Background = load_image('Resource\\Map\\Stage3\\Third_Background.png')
        self.Ground = load_image('Resource\\Map\\Stage3\\Third_ground.png')

    def draw(self):
        self.Background.draw(400, 200)
        self.Ground.draw(400, 350)

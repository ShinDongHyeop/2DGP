from pico2d import *

class Background:
    def __init__(self):
        self.Background = load_image('Resource\\Map\\Stage1\\First_Background.png')
        self.Ground = load_image('Resource\\Map\\Stage1\\First_ground.png')

    def draw(self):
        self.Background.draw(400, 200)
        self.Ground.draw(400, 350)
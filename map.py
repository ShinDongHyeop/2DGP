from pico2d import *

class Stage1_Background:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 20.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self, w, h):
        self.speed = 0
        self.left = 0
        self.screen_width = w
        self.screen_height = h

        self.Background = load_image('Resource\\Map\\Stage1\\First_Background.png')
        self.Ground = load_image('Resource\\Map\\Stage1\\First_ground.png')

    def draw(self):
        x = int(self.left)
        w = min(self.Background.w - x, self.screen_width)
        self.Background.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        self.Background.clip_draw_to_origin(0, 0, self.screen_width-w, self.screen_height, w, 0)
       # self.Background.draw(400, 200)
        self.Ground.draw(400, 350)

    def update(self, frame_time):
        self.speed = 100
        self.left = (self.left + frame_time * self.speed) % self.Background.w


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
        self.Ground = load_image('Resource\\Map\\Stage4\\Fourth_ground.png')

    def draw(self):
        self.Background.draw(400, 200)
        self.Ground.draw(400, 350)
from pico2d import *

class Stage1_Ground:
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
        self.ground = load_image('Resource\\Map\\Stage1\\First_ground.png')
        self.bgm = load_music('Resource\\Sound\\Stage1.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()


    def draw(self):
        x = int(self.left)
        w = min(self.ground.w - x, self.screen_width)
        self.ground.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        self.ground.clip_draw_to_origin(0, 0, self.screen_width - w, self.screen_height, w, 0)

    def update(self, frame_time):
        self.speed = 100
        self.left = (self.left + frame_time * self.speed) % self.ground.w


class Stage2_Ground:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 30.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self, w, h):
        self.speed = 0
        self.left = 0
        self.screen_width = w
        self.screen_height = h
        self.ground = load_image('Resource\\Map\\Stage2\\Second_ground.png')
        self.bgm = load_music('Resource\\Sound\\Stage2.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
        x = int(self.left)
        w = min(self.ground.w - x, self.screen_width)
        self.ground.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        self.ground.clip_draw_to_origin(0, 0, self.screen_width - w, self.screen_height, w, 0)

    def update(self, frame_time):
        self.speed = 100
        self.left = (self.left + frame_time * self.speed) % self.ground.w

class Stage3_Ground:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 30.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self, w, h):
        self.speed = 0
        self.left = 0
        self.left2 = 0
        self.screen_width = w
        self.screen_height = h
        self.ground = load_image('Resource\\Map\\Stage3\\Third_ground.png')
        self.bgm = load_music('Resource\\Sound\\Stage3.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
        x = int(self.left)
        w = min(self.ground.w - x, self.screen_width)
        self.ground.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        self.ground.clip_draw_to_origin(0, 0, self.screen_width - w, self.screen_height, w, 0)

    def update(self, frame_time):
        self.speed = 100
        self.left = (self.left + frame_time * self.speed) % self.ground.w

class Stage4_Ground:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 40.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self, w, h):
        self.speed = 0
        self.left = 0
        self.left2 = 0
        self.screen_width = w
        self.screen_height = h
        self.ground = load_image('Resource\\Map\\Stage4\\Fourth_ground.png')
        self.bgm = load_music('Resource\\Sound\\Stage4.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
        x = int(self.left)
        w = min(self.ground.w - x, self.screen_width)
        self.ground.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        self.ground.clip_draw_to_origin(0, 0, self.screen_width - w, self.screen_height, w, 0)

    def update(self, frame_time):
        self.speed = 100
        self.left = (self.left + frame_time * self.speed) % self.ground.w
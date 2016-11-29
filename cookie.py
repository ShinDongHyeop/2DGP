from pico2d import *
from score import *
import game_framework


class Brave_Cookie:
    image = None
    score_sound = None
    hp_sound = None
    state_sound = None
    hp = 250.0

    def __init__(self):
        self.x = 150
        self.y = 200
        self.frame = 0
        self.jump = 0
        self.jump_gravity = 0
        self.collision_time = 0
        self.map_size = 0.0
        self.state = "Run"

        if Brave_Cookie.image == None:
            self.Brave_Cookie_run = load_image('Resource\\Character1\\cookie_run.png')
            self.Brave_Cookie_dead = load_image('Resource\\Character1\\cookie_run_dead.png')
            self.Brave_Cookie_slide = load_image('Resource\\Character1\\cookie_run_slide.png')
            self.Brave_Cookie_jump1 = load_image('Resource\\Character1\\cookie_run_jump.png')
            self.Brave_Cookie_jump2 = load_image('Resource\\Character1\\cookie_run_jump2.png')
            self.Brave_Cookie_collide = load_image('Resource\\Character1\\cookie_run_collid.png')
            self.Brave_Cookie_hp = load_image('Resource\\Item\\hp.png')
        if Brave_Cookie.score_sound == None:
            Brave_Cookie.score_sound = load_wav('Resource\\Sound\\jelly.wav')
            Brave_Cookie.score_sound.set_volume(16)
        if Brave_Cookie.hp_sound == None:
            Brave_Cookie.hp_sound = load_wav('Resource\\Sound\\hp_jelly.wav')
            Brave_Cookie.hp_sound.set_volume(16)
        if Brave_Cookie.state_sound == None:
            self.jump_sound = load_wav('Resource\\Sound\\jump.wav')
            self.jump_sound.set_volume(16)
            self.slide_sound = load_wav('Resource\\Sound\\slide.wav')
            self.slide_sound.set_volume(16)
            self.collide_sound = load_wav('Resource\\Sound\\collide.wav')
            self.collide_sound.set_volume(16)

    def scoreSound(self, item):
        self.score_sound.play()
        Score.score += 50

    def bump(self):
        if self.collision_time < 1:
            Brave_Cookie.hp -= 60
            self.collision_time += 1
        else:
            self.state = "Run"

    def heal(self, item):
        Brave_Cookie.hp += 80
        self.hp_sound.play()

    def update(self, frame_time):
        if frame_time < 1:
            self.map_size += frame_time
        Brave_Cookie.hp -= 0.05

        self.gravity()
        if self.state == "Run":
            self.frame = (self.frame + 1) % 6
        elif self.state == "Dead":
            self.frame = (self.frame + 1) % 4
        elif self.state == "Jump" and self.y <= 210:
            self.state = "Run"
        elif self.state == "Run" or self.state == "Slide" or self.state == "Jump":
            self.collision_time = 0
        elif self.state == "Collide":
            self.bump()

        if self.state == "Jump" and (self.map_size >= 51.5 and self.map_size <= 55.0):
            if (self.y - 40 - self.jump_gravity) > 210:
                self.jump_gravity += 2
                self.y -= self.jump_gravity / 2
            else:
                self.y = 250
                self.jump_gravity = 0

    def gravity(self):
        if (self.y - 40 - self.jump_gravity) > 160:
            self.jump_gravity += 2
            self.y -= self.jump_gravity / 2
        else:
            self.y = 200
            self.jump_gravity = 0

    def draw(self):
        if self.state == "Run":
            self.Brave_Cookie_run.clip_draw(self.frame * 75, 0, 75, 100, self.x, self.y)
        elif self.state == "Slide":
            self.Brave_Cookie_slide.draw(self.x, self.y - 30)
        elif self.state == "Collide":
            self.Brave_Cookie_collide.draw(self.x, self.y)
        elif self.state == "Jump":
            if self.jump % 2 == 1:
                self.Brave_Cookie_jump1.draw(self.x, self.y)
            elif self.jump % 2 == 0:
                self.Brave_Cookie_jump2.draw(self.x, self.y)
        self.Brave_Cookie_hp.draw_to_origin(0, 500, Brave_Cookie.hp, 50)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if self.state == "Run":
            return self.x - 20, self. y - 30, self.x + 15, self.y + 10
        elif self.state == "Slide":
            return self.x - 5 , self. y - 50, self.x + 25, self.y - 30
        elif self.state == "Jump":
            return self.x - 15, self. y - 10, self.x + 25, self.y + 10
        elif self.state == "Collide":
            return self.x - 0, self. y - 0, self.x + 0, self.y + 0

    def handle_events(self, event):
        events = get_events()

        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_DOWN:
                self.state = "Slide"

            elif event.key == SDLK_UP:
                self.state = "Jump"
                self.jump += 1
                if (self.y - 40) == 160:
                    self.jump_gravity = -30

                if (self.map_size >= 1440 and self.map_size <= 1550) and (self.y - 40) == 210:
                    self.jump_gravity = -30


        elif event.type == SDL_KEYUP:
            if event.key == SDLK_DOWN:
                self.state = "Run"

class Ginger_Brave_Cookie:
    image = None
    sound = None
    state_sound = None
    hp = 250.0

    def __init__(self):
        self.x = 150
        self.y = 200
        self.frame = 0
        self.map_size = 0
        self.jump = 0
        self.jump_gravity = 0
        self.collision_time = 0
        self.state = "Run"
        if Ginger_Brave_Cookie.image == None:
            self.Ginger_Brave_Cookie_run = load_image('Resource\\Character2\\Cookie2_Run.png')
            self.Ginger_Brave_Cookie_dead = load_image('Resource\\Character2\\Cookie2_Dead.png')
            self.Ginger_Brave_Cookie_slide = load_image('Resource\\Character2\\Cookie2_Slide.png')
            self.Ginger_Brave_Cookie_jump = load_image('Resource\\Character2\\Cookie2_Jump.png')
            self.Ginger_Brave_Cookie_collide = load_image('Resource\\Character2\\Cookie2_Collide.png')
            self.Ginger_Brave_Cookie_hp = load_image('Resource\\Item\\hp.png')
        if Ginger_Brave_Cookie.sound == None:
            self.score_sound = load_wav('Resource\\Sound\\jelly.wav')
            self.score_sound.set_volume(32)
            self.hp_sound = load_wav('Resource\\Sound\\hp_jelly.wav')
            self.hp_sound.set_volume(32)
        if Ginger_Brave_Cookie.state_sound == None:
            self.jump_sound = load_wav('Resource\\Sound\\jump.wav')
            self.jump_sound.set_volume(32)
            self.slide_sound = load_wav('Resource\\Sound\\slide.wav')
            self.slide_sound.set_volume(32)
            self.collide_sound = load_wav('Resource\\Sound\\collide.wav')
            self.collide_sound.set_volume(32)

    def scoreSound(self, item):
        self.score_sound.play()
        Score.score += 50

    def bump(self):
        if self.collision_time < 1:
            Ginger_Brave_Cookie.hp -= 60
            self.collision_time += 1
        else:
            self.state = "Run"

    def heal(self, item):
        Ginger_Brave_Cookie.hp += 80
        self.hp_sound.play()

    def update(self, frame_time):
        Ginger_Brave_Cookie.hp -= 0.1
        if frame_time < 1:
            self.map_size += frame_time

        self.gravity()
        if self.state == "Run":
            self.frame = (self.frame + 1) % 3
        elif self.state == "Dead":
            self.frame = (self.frame + 1) % 2
        elif self.state == "Jump" and self.y <= 210:
            self.state = "Run"
        elif self.state == "Run" or self.state == "Slide" or self.state == "Jump":
            self.collision_time = 0
            self.frame = 0
        elif self.state == "Collide":
            self.bump()

        if self.state == "Jump" and (self.map_size >= 51.5 and self.map_size <= 55):
            if (self.y - 40 - self.jump_gravity) > 210:
                self.jump_gravity += 2
                self.y -= self.jump_gravity / 2
            else:
                self.y = 250
                self.jump_gravity = 0

    def gravity(self):
        if(self.y - 40 - self.jump_gravity) > 160:
            self.jump_gravity += 2
            self.y -= self.jump_gravity / 2
        else:
            self.y = 200
            self.jump_gravity = 0

    def draw(self):
        if self.state == "Run":
            self.Ginger_Brave_Cookie_run.clip_draw(self.frame * 47, 0, 47, 100, self.x, self.y)
        elif self.state == "Slide":
            self.Ginger_Brave_Cookie_slide.clip_draw(self.frame * 69, 0, 69, 69, self.x, self.y - 30)
        elif self.state == "Jump":
            self.Ginger_Brave_Cookie_jump.clip_draw(self.frame * 51, 0, 51, 100, self.x, self.y)
        elif self.state == "Collide":
            self.Ginger_Brave_Cookie_collide.draw(self.x, self.y)
        self.Ginger_Brave_Cookie_hp.draw_to_origin(0, 500, self.hp, 50)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if self.state == "Run":
            return self.x - 20, self. y - 40, self.x + 15, self.y + 10
        elif self.state == "Slide":
            return self.x - 5 , self. y - 50, self.x + 25, self.y - 30
        elif self.state == "Jump":
            return self.x - 15, self. y - 10, self.x + 25, self.y + 10
        elif self.state == "Collide":
            return self.x - 0, self. y - 0, self.x + 0, self.y + 0

    def handle_events(self, event):
        events = get_events()

        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_DOWN:
                self.state = "Slide"

            elif event.key == SDLK_UP:
                self.state = "Jump"

                if (self.y - 40) == 160:
                    self.jump_gravity = -30

                if (self.map_size >= 1440 and self.map_size <= 1550) and (self.y - 40) == 210:
                    self.jump_gravity = -30

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_DOWN:
                self.state = "Run"

class Brave_Cookie_Select:
    image = None

    def __init__(self):
        self.x = 250
        self.y = 200
        self.frame = 0
        self.state = "Run"

        if Brave_Cookie.image == None:
            self.Brave_Cookie_run = load_image('Resource\\Character1\\cookie_run.png')
            self.Brave_Cookie_select = load_image('Resource\\game_start_button.png')
            self.Brave_Cookie_hp = load_image('Resource\\Item\\hp.png')

    def update(self):
        self.state = "Run"
        self.frame = (self.frame + 1) % 6

    def draw(self):
        if self.state == "Run":
            self.Brave_Cookie_run.clip_draw(self.frame * 75, 0, 75, 100, self.x, self.y)
            self.Brave_Cookie_select.draw(250, 100)
            self.Brave_Cookie_hp.draw_to_origin(125, 300, Brave_Cookie.hp, 50)

class Ginger_Brave_Cookie_Select:
    image = None

    def __init__(self):
        self.x = 550
        self.y = 200
        self.frame = 0
        self.state = "Run"

        if Brave_Cookie.image == None:
            self.Ginger_Brave_Cookie_run = load_image('Resource\\Character2\\Cookie2_Run.png')
            self.Ginger_Brave_Cookie_select = load_image('Resource\\game_start_button.png')
            self.Ginger_Brave_Cookie_hp = load_image('Resource\\Item\\hp.png')
    def update(self):
        self.state = "Run"
        self.frame = (self.frame + 1) % 3

    def draw(self):
        if self.state == "Run":
            self.Ginger_Brave_Cookie_run.clip_draw(self.frame * 47, 0, 47, 100, self.x, self.y)
        self.Ginger_Brave_Cookie_select.draw(550, 100)
        self.Ginger_Brave_Cookie_hp.draw_to_origin(425, 300, Ginger_Brave_Cookie.hp, 50)
from pico2d import *
import game_framework

xsize = 0


class Brave_Cookie:
    image = None

    def __init__(self, state):
        self.x = 150
        self.y = 200
        self.frame = 0
        self.jump = 0
        self.jump_gravity = 0
        self.state = state
        self.state = "Run"

        if Brave_Cookie.image == None:
            self.Cookie1_run = load_image('Resource\\Character1\\cookie_run.png')
            self.Cookie1_dead = load_image('Resource\\Character1\\cookie_run_dead.png')
            self.Cookie1_slide = load_image('Resource\\Character1\\cookie_run_slide.png')
            self.Cookie1_jump1 = load_image('Resource\\Character1\\cookie_run_jump.png')
            self.Cookie1_jump2 = load_image('Resource\\Character1\\cookie_run_jump2.png')

    def update(self):
        global xsize
        xsize += 1

        if xsize > 2200:
            xsize = 0

        if self.state == "Jump":
            self.gravity()
        if self.state == "Run":
            self.frame = (self.frame + 1) % 6
        elif self.state == "Dead":
            self.frame = (self.frame + 1) % 4
        elif self.state == "Jump" and self.y <= 210:
            self.state = "Run"
        elif self.state == "Jump" and self.state == "Slide":
            self.frame = 0

        if self.state == "Jump" and (xsize >= 2050 and xsize <= 2200):
            if (self.y - 40 - self.jump_gravity) > 210:
                self.jump_gravity += 2
                self.y -= self.jump_gravity / 2
            else:
                self.y = 250
                self.jump_gravity = 0
                self.state = "Run"

        print("xsize : ", xsize)

    def gravity(self):
        if (self.y - 40 - self.jump_gravity) > 160:
            self.jump_gravity += 2
            self.y -= self.jump_gravity / 2
        else:
            self.y = 200
            self.jump_gravity = 0

    def draw(self):
        if self.state == "Run":
            self.Cookie1_run.clip_draw(self.frame * 75, 0, 75, 100, self.x, self.y)
        elif self.state == "Slide":
            self.Cookie1_slide.draw(self.x, self.y - 30)
        elif self.state == "Jump":
            if self.jump % 2 == 1:
                self.Cookie1_jump1.draw(self.x, self.y)
            elif self.jump % 2 == 0:
                self.Cookie1_jump2.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if self.state == "Run":
            return self.x - 20, self. y - 10, self.x + 15, self.y + 10
        elif self.state == "Slide":
            return self.x - 5 , self. y - 60, self.x + 25, self.y + -5
        elif self.state == "Jump":
            return self.x - 15, self. y - 10, self.x + 25, self.y + 10


    def handle_events(self, event):
        global xsize
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

                if (xsize >= 2050 and xsize <= 2200) and (self.y - 40) == 210:
                    self.jump_gravity = -30


        elif event.type == SDL_KEYUP:
            if event.key == SDLK_DOWN:
                self.state = "Run"


class Ginger_Brave_Cookie:
    image = None

    def __init__(self, state):
        self.x = 150
        self.y = 200
        self.frame = 0
        self.jump = 0
        self.jump_gravity = 0
        self.state = state
        self.state = "Run"

        if Ginger_Brave_Cookie.image == None:
            self.Cookie2_run = load_image('Resource\\Character2\\Cookie2_Run.png')
            self.Cookie2_dead = load_image('Resource\\Character2\\Cookie2_Dead.png')
            self.Cookie2_slide = load_image('Resource\\Character2\\Cookie2_Slide.png')
            self.Cookie2_jump = load_image('Resource\\Character2\\Cookie2_Jump.png')

    def __del__(self):
        pass

    def update(self):
        global xsize
        xsize += 1

        if xsize > 2200:
            xsize = 0

        if self.state == "Jump":
            self.gravity()
        if self.state == "Run":
            self.frame = (self.frame + 1) % 3
        elif self.state == "Dead":
            self.frame = (self.frame + 1) % 2
        elif self.state == "Jump" and self.y <= 210:
            self.state = "Run"
        elif self.state == "Slide":
            self.frame = 0

        if self.state == "Jump" and (xsize >= 2050 and xsize <= 2200):
            if (self.y - 40 - self.jump_gravity) > 210:
                self.jump_gravity += 2
                self.y -= self.jump_gravity / 2
            else:
                self.y = 250
                self.jump_gravity = 0
                self.state = "Run"

    def gravity(self):
        if(self.y - 40 - self.jump_gravity) > 160:
            self.jump_gravity += 2
            self.y -= self.jump_gravity / 2
        else:
            self.y = 200
            self.jump_gravity = 0

    def draw(self):
        if self.state == "Run":
            self.Cookie2_run.clip_draw(self.frame * 47, 0, 47, 100, self.x, self.y)
        elif self.state == "Slide":
            self.Cookie2_slide.clip_draw(self.frame * 69, 0, 69, 69, self.x, self.y - 30)
        elif self.state == "Jump":
            self.Cookie2_jump.clip_draw(self.frame * 51, 0, 51, 100, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if self.state == "Run":
            return self.x - 20, self. y - 10, self.x + 15, self.y + 10
        elif self.state == "Slide":
            return self.x - 5 , self. y - 60, self.x + 25, self.y + -5
        elif self.state == "Jump":
            return self.x - 15, self. y - 10, self.x + 25, self.y + 10

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

                if (xsize >= 2050 and xsize <= 2200) and (self.y - 40) == 210:
                    self.jump_gravity = -30

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_DOWN:
                self.state = "Run"
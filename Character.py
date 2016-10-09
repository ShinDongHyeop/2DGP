from pico2d import *
import game_framework

class Character:
    image = None
    global running

    def __init__(self):
        self.x = 150
        self.y = 200
        self.frame = 0
        self.jump = 0
        self.jump_gravity = 0
        self.state = "Run"

        if Character.image == None:
            self.Cookie1_run = load_image('Resource\\Character1\\cookie_run.png')
            self.Cookie1_dead = load_image('Resource\\Character1\\cookie_run_dead.png')
            self.Cookie1_slide = load_image('Resource\\Character1\\cookie_run_slide.png')
            self.Cookie1_jump1 = load_image('Resource\\Character1\\cookie_run_jump.png')
            self.Cookie1_jump2 = load_image('Resource\\Character1\\cookie_run_jump2.png')

    def __del__(self):
        pass

    def update(self):
        self.gravity()
        if self.state == "Run":
            self.frame = (self.frame + 1) % 6
        elif self.state == "Dead":
            self.frame = (self.frame + 1) % 4
        elif self.state == "Jump":
            self.State = "Run"
        elif self.state == "Slide":
            self.frame = 0


    def gravity(self):
        if(self.y - 40 - self.jump_gravity) > 160:
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
                #self.gravity()
            elif self.jump % 2 == 0:
                self.Cookie1_jump2.draw(self.x, self.y)
                #self.gravity()

    def handle_events(self, event):
        events = get_events()

        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_DOWN:
                self.state = "Slide"

            elif event.key == SDLK_UP :
                self.state = "Jump"
                self.jump += 1
                if (self.y - 40) == 160:
                    self.jump_gravity = -30
        else:
            self.state = "Run"
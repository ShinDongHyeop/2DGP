from pico2d import *
import game_framework
import title_state

class Brave_Cookie:
    image = None

    def __init__(self, state):
        self.x = 150
        self.y = 200
        self.frame = 0
        self.map_size = 0
        self.hp = 400.0
        self.jump = 0
        self.jump_gravity = 0
        self.collision_time = 0
        self.state = state
        self.state = "Run"

        if Brave_Cookie.image == None:
            self.Brave_Cookie_run = load_image('Resource\\Character1\\cookie_run.png')
            self.Brave_Cookie_dead = load_image('Resource\\Character1\\cookie_run_dead.png')
            self.Brave_Cookie_slide = load_image('Resource\\Character1\\cookie_run_slide.png')
            self.Brave_Cookie_jump1 = load_image('Resource\\Character1\\cookie_run_jump.png')
            self.Brave_Cookie_jump2 = load_image('Resource\\Character1\\cookie_run_jump2.png')
            self.Brave_Cookie_collide = load_image('Resource\\Character1\\cookie_run_collid.png')
            self.Brave_Cookie_hp = load_image('Resource\\Item\\hp.png')

    def bump(self, state):
        self.state = state
        self.hp -= 40
        if self.collision_time < 3:
            self.collision_time += 1
            self.map_size += 0

        else:
            self.state = "Run"
            self.collision_time = 0

    def heal(self):
        self.hp += 60

    def update(self):
        self.hp -= 0.1

        if self.map_size > 1550:
            self.map_size = 0

        self.gravity()
        if self.state == "Run":
            self.map_size += 1
            self.frame = (self.frame + 1) % 6
        elif self.state == "Dead":
            self.frame = (self.frame + 1) % 4
        elif self.state == "Jump" and self.y <= 210:
            self.state = "Run"
        elif self.state == "Slide" or self.state == "Jump":
            self.map_size += 1
        elif self.state == "Collide":
            self.bump("Collide")

        if self.state == "Jump" and (self.map_size >= 1440 and self.map_size <= 1550):
            if (self.y - 40 - self.jump_gravity) > 210:
                self.jump_gravity += 2
                self.y -= self.jump_gravity / 2
            else:
                self.y = 250
                self.jump_gravity = 0
        print("map_size : ", self.map_size)

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
        self.Brave_Cookie_hp.draw_to_origin(0, 500, self.hp, 50)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if self.state == "Run":
            return self.x - 20, self. y - 30, self.x + 15, self.y + 10
        elif self.state == "Slide":
            return self.x - 5 , self. y - 50, self.x + 25, self.y - 20
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

    def __init__(self, state):
        self.x = 150
        self.y = 200
        self.frame = 0
        self.map_size = 0
        self.hp = 400.0
        self.jump = 0
        self.jump_gravity = 0
        self.collision_time = 0
        self.state = state
        self.state = "Run"

        if Ginger_Brave_Cookie.image == None:
            self.Ginger_Brave_Cookie_run = load_image('Resource\\Character2\\Cookie2_Run.png')
            self.Ginger_Brave_Cookie_dead = load_image('Resource\\Character2\\Cookie2_Dead.png')
            self.Ginger_Brave_Cookie_slide = load_image('Resource\\Character2\\Cookie2_Slide.png')
            self.Ginger_Brave_Cookie_jump = load_image('Resource\\Character2\\Cookie2_Jump.png')
            self.Ginger_Brave_Cookie_collide = load_image('Resource\\Character2\\Cookie2_Collide.png')
            self.Ginger_Brave_Cookie_hp = load_image('Resource\\Item\\hp.png')

    def bump(self, state):
        self.state = state
        self.hp -= 40
        if self.collision_time < 3:
            self.collision_time += 1
            self.map_size += 0

        else:
            self.state = "Run"
            self.collision_time = 0

    def heal(self):
        self.hp += 60

    def update(self):
        self.hp -= 0.1

        if self.map_size > 1550:
            self.map_size = 0


        self.gravity()
        if self.state == "Run":
            self.map_size += 1
            self.frame = (self.frame + 1) % 3
        elif self.state == "Dead":
            self.frame = (self.frame + 1) % 2
        elif self.state == "Jump" and self.y <= 210:
            self.state = "Run"
        elif self.state == "Slide" or self.state == "Jump":
            self.map_size += 1
            self.frame = 0
        elif self.state == "Collide":
            self.bump("Collide")

        if self.state == "Jump" and (self.map_size >= 1440 and self.map_size <= 1550):
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
            return self.x - 5 , self. y - 50, self.x + 25, self.y - 20
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
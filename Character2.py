from pico2d import *
from Map import *


running = None


class Character2:
    image_init = None
    global running

    def __init__(self):
        self.x = 150
        self.y = 200
        self.frame = 0
        self.jump = 0
        self.jump_gravity = 0
        self.state = "Run"

        if Character2.image_init == None:
            self.Cookie2_run = load_image('Resource\\Character2\\Cookie2_Run.png')
            self.Cookie2_dead = load_image('Resource\\Character2\\Cookie2_Dead.png')
            self.Cookie2_slide = load_image('Resource\\Character2\\Cookie2_Slide.png')
            self.Cookie2_jump = load_image('Resource\\Character2\\Cookie2_Jump.png')

    def __del__(self):
        pass

    def update(self):
        if self.state == "Run":
            self.frame = (self.frame + 1) % 3
        elif self.state == "Dead":
            self.frame = (self.frame + 1) % 2
        elif self.state == "Jump":
            self.frame = (self.frame + 1) % 3
        elif self.state == "Slide":
            self.frame = (self.frame + 1) % 2

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

    def handle_event(self):
        events = get_events()

        global running
        global speed

        for event in events:
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                running = False

            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_DOWN:
                    self.state = "Slide"

                elif event.key == SDLK_UP:
                    self.state = "Jump"

                    if (self.y - 40) == 160:
                        self.jump_gravity = -30
                #elif event.key == SDLK_SPACE:
                    #self.state = "Run"
                    #speed = 0.03

            elif event.type == SDL_KEYUP:
                if self.state != "slide" or self.state != "Jump":
                    self.state = "Run"



def main():

    open_canvas()
    global speed
    speed = 0.05
    character2 = Character2()
    map = Background()
    global running
    running = True

    while running:
        character2.handle_event()
        character2.update()
        character2.gravity()

        clear_canvas()

        map.draw()

        character2.draw()

        update_canvas()

        delay(speed)
    close_canvas()


if __name__ == '__main__':
    main()





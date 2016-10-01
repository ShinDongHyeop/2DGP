from Map import *
from pico2d import *

running = None


class Character:
    image_init = None
    global running

    def __init__(self):
        self.x = 150
        self.y = 200
        self.frame = 0
        self.jump = 0
        self.jump_gravity = 0
        self.state = "Run"

        if Character.image_init == None:
            self.Cookie1_run = load_image('Resource\\Character1\\cookie_run.png')
            self.Cookie1_dead = load_image('Resource\\Character1\\cookie_run_dead.png')
            self.Cookie1_slide = load_image('Resource\\Character1\\cookie_run_slide.png')
            self.Cookie1_jump1 = load_image('Resource\\Character1\\cookie_run_jump.png')
            self.Cookie1_jump2 = load_image('Resource\\Character1\\cookie_run_jump2.png')

    def __del__(self):
        pass

    def update(self):
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
            elif self.jump % 2 == 0:
                self.Cookie1_jump2.draw(self.x, self.y)

    def handle_event(self):
        events = get_events()

        global running

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
                    self.jump += 1

                    if (self.y - 40) == 160:
                        self.jump_gravity = -30

            elif event.type == SDL_KEYUP:
                if self.state != "slide" or self.state != "Jump":
                    self.state = "Run"

            #elif event.type == SDL_KEYDOWN and event.type != SDL_KEYUP:
                #if event.key == SDLK_SPACE:


'''def main():

    open_canvas()

    character = Character()
    map = Background()
    global running
    running = True

    while running:
        character.handle_event()
        character.update()
        character.gravity()
        clear_canvas()
        map.draw()
        character.draw()
        update_canvas()

        delay(0.05)
    close_canvas()


if __name__ == '__main__':
    main()'''





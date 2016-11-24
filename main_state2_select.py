from back_ground import *
from ground import *
from pico2d import *
from cookie import *
import game_framework
import main_state2

name = "MainState2Select"
background = None
ground = None
brave_cookie = None
ginger_brave_cookie = None
brave_select = None
ginger_select = None
cookie_select = None
current_time = 0.0

def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def enter():
    global background, ground, brave_cookie, ginger_brave_cookie, brave_select, ginger_select, \
            brave_hp, ginger_hp, x, y

    background = Stage2_Background(800,600)
    ground = Stage2_Ground(800,150)
    brave_cookie = Brave_Cookie_Select()
    ginger_brave_cookie = Ginger_Brave_Cookie_Select()
    x = 0
    y = 0

def exit():
    global background, ground, brave_cookie, ginger_brave_cookie
    del(background)
    del(ground)
    del(brave_cookie)
    del(ginger_brave_cookie)

def handle_events():
    global x, y, cookie_select
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif event.type == SDL_MOUSEMOTION:
                x ,y = event.x, 599 - event.y

            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                if (x >= 124 and x <= 373) and (y >= 70 and y <= 127):
                    cookie_select = Brave_Cookie()
                    game_framework.change_state(main_state2)
                elif (x >= 425 and x <= 674) and (y >= 70 and y <= 127):
                    cookie_select = Ginger_Brave_Cookie()
                    game_framework.change_state(main_state2)

def draw():
    global brave_cookie, ginger_brave_cookie, brave_select, ginger_select

    clear_canvas()
    background.draw()
    ground.draw()
    brave_cookie.draw()
    ginger_brave_cookie.draw()

    update_canvas()

def update():
    frame_time = get_frame_time()
    background.update(frame_time)
    ground.update(frame_time)
    brave_cookie.update()
    ginger_brave_cookie.update()
    delay(0.03)


def pause():
    pass


def resume():
    pass







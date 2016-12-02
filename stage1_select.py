from back_ground import *
from ground import *
from pico2d import *
from cookie import *
from score import *
import game_framework
import stage1
import stage2_select
import stage3_select
import stage4_select

name = "MainState1Select"
background = None
ground = None
brave_cookie = None
ginger_brave_cookie = None
get_cookie = None
brave_cookie_select = None
ginger_brave_cookie_select = None
current_time = 0.0

def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def enter():
    global background, ground, brave_cookie, ginger_brave_cookie, font, score, x, y, brave_cookie_select, ginger_brave_cookie_select

    background = Stage1_Background(800,600)
    ground = Stage1_Ground(800,150)
    brave_cookie = Brave_Cookie_Select()
    ginger_brave_cookie = Ginger_Brave_Cookie_Select()
    brave_cookie_select = None
    ginger_brave_cookie_select = None
    score = Score()
    font = load_font('Resource\\ENCR10B.TTF')
    x = 0
    y = 0

def exit():
    global background, ground, brave_cookie, ginger_brave_cookie
    del(background)
    del(ground)
    del(brave_cookie)
    del(ginger_brave_cookie)


def handle_events():
    global x, y, get_cookie, brave_cookie_select, ginger_brave_cookie_select
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
                game_framework.change_state(stage2_select)
            elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
                game_framework.change_state(stage3_select)
            elif event.type == SDL_KEYDOWN and event.key == SDLK_4:
                game_framework.change_state(stage4_select)

            elif event.type == SDL_MOUSEMOTION:
                x, y = event.x, 599 - event.y

            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                if (x >= 124 and x <= 373) and (y >= 70 and y <= 127) and Brave_Cookie().hp > 0:
                    get_cookie = Brave_Cookie()
                    brave_cookie_select = True
                    game_framework.change_state(stage1)

                if (x >= 425 and x <= 674) and (y >= 70 and y <= 127) and Ginger_Brave_Cookie().hp > 0:
                    get_cookie = Ginger_Brave_Cookie()
                    ginger_brave_cookie_select = True
                    game_framework.change_state(stage1)


def draw():
    global brave_cookie, ginger_brave_cookie, font, score
    clear_canvas()
    background.draw()
    ground.draw()
    brave_cookie.draw()
    ginger_brave_cookie.draw()
    font.draw(100, 550, 'Score : %3.2d' % score.score, (255, 255, 255))
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







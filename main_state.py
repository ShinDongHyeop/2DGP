import random
import json
import os
import time

from pico2d import *
from cookie import *
from back_ground import *
from ground import *
from obstacle import *
from item import *
import game_framework
import title_state
import main_state2
import main_state3
import main_state4

name = "MainState"

brave_cookie = None
ginger_brave_cookie = None
background = None
nomal_fork = None
nomal_thorn = None
special_fork = None
double_thorn = None
board = None
item_jelly = None
hp_jelly = None
object = []
current_time = 0.0

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def enter():
    global brave_cookie, ginger_brave_cookie, background, ground, nomal_fork, nomal_thorn, special_fork, double_thorn, board, \
            start, score_jelly, hp_jelly, font, object

    brave_cookie = Brave_Cookie("Run")
    ginger_brave_cookie = Ginger_Brave_Cookie("Run")
    background = Stage1_Background(800, 600)
    ground = Stage1_Ground(800, 150)
    board = Stage1_Board().create()
    nomal_fork = Stage1_Nomal_Fork().create()
    nomal_thorn = Stage1_Nomal_Thorn().create()
    special_fork = Stage1_Special_Fork().create()
    double_thorn = Stage1_Double_Thorn().create()
    score_jelly = Stage1_Score_Jelly().create()
    hp_jelly = Stage1_Hp_Jelly().create()
    object = [board, nomal_fork, special_fork, nomal_thorn, double_thorn, score_jelly, hp_jelly]
    font = load_font('Resource\\ENCR10B.TTF')
    start = time.time()

def exit():
    global brave_cookie, ginger_brave_cookie, background, ground, nomal_fork, nomal_thorn, special_fork, double_thorn, board, start, \
            score_jelly, hp_jelly, object
    del(brave_cookie)
    del(ginger_brave_cookie)
    del(background)
    del(ground)

    for list in object:
        for dict in list:
            list.remove(dict)
            del(dict)
        del(list)


    end = time.time()

    print("Stage1 Clear Time : ", (end - start))


def pause():
    pass


def resume():
    pass


def handle_events():
    global brave_cookie, ginger_brave_cookie
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            game_framework.change_state(main_state2)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
            game_framework.change_state(main_state3)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_4:
            game_framework.change_state(main_state4)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if type(brave_cookie) == Brave_Cookie:
                brave_cookie = Ginger_Brave_Cookie(brave_cookie.state)
            elif type(brave_cookie) == Ginger_Brave_Cookie:
                brave_cookie = Brave_Cookie(brave_cookie.state)

        else:
            brave_cookie.handle_events(event)
            ginger_brave_cookie.handle_events(event)

def update():
    global brave_cookie, ginger_brave_cookie, background, ground, nomal_fork, nomal_thorn, special_fork, double_thorn, board, \
            score_jelly, hp_jelly, object

    frame_time = get_frame_time()
    brave_cookie.update()
    ginger_brave_cookie.update()
    background.update(frame_time)
    ground.update(frame_time)

    for list in object:
        for dict in list:
            dict.update(frame_time)
            if collide(brave_cookie, dict):
                if list == score_jelly:
                    score_jelly.remove(dict)
                    brave_cookie.scoreSound(dict)
                elif list == hp_jelly:
                    hp_jelly.remove(dict)
                    brave_cookie.heal(dict)
                else:
                    if collide(brave_cookie, dict):
                        brave_cookie.state = "Collide"
                        brave_cookie.bump()
                        dict.bump("Collide")

    if brave_cookie.map_size == 1550 and brave_cookie.y == 200:
        game_framework.change_state(main_state2)
    elif brave_cookie.map_size == 1550 and brave_cookie.y == 250:
        game_framework.change_state(main_state3)

def draw():
    global brave_cookie, ginger_brave_cookie, background, ground, \
            score_jelly, hp_jelly, object
    clear_canvas()
    background.draw()
    ground.draw()

    for list in object:
        for dict in list:
            dict.draw()

    font.draw(100, 550, 'Score : %3.2d' % brave_cookie.score, (255, 255, 255))
    brave_cookie.draw()

    delay(0.03)
    update_canvas()
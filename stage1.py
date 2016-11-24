import random
import json
import os
import time

from back_ground import *
from ground import *
from obstacle import *
from item import *
from score import *
import game_framework
import title_state
import stage2
import stage2_select
import stage3
import stage3_select
import stage4
import stage1_select
name = "MainState"

cookie = None
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
    global cookie, background, ground, nomal_fork, nomal_thorn, special_fork, double_thorn, board, \
            start, score_jelly, hp_jelly, font, objects, score
    
    cookie = stage1_select.get_cookie
    background = Stage1_Background(800, 600)
    score = Score()
    ground = Stage1_Ground(800, 150)
    board = Stage1_Board().create()
    nomal_fork = Stage1_Nomal_Fork().create()
    nomal_thorn = Stage1_Nomal_Thorn().create()
    special_fork = Stage1_Special_Fork().create()
    double_thorn = Stage1_Double_Thorn().create()
    score_jelly = Stage1_Score_Jelly().create()
    hp_jelly = Stage1_Hp_Jelly().create()
    objects = [nomal_fork, special_fork, nomal_thorn, double_thorn, score_jelly, hp_jelly, board]
    font = load_font('Resource\\ENCR10B.TTF')
    start = time.time()

def exit():
    global cookie, background, ground, nomal_fork, nomal_thorn, special_fork, double_thorn, board, start, \
            score_jelly, hp_jelly, objects, score
    del(cookie)
    del(background)
    del(ground)

    for list in objects:
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
    global cookie
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            game_framework.change_state(stage2)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
            game_framework.change_state(stage3)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_4:
            game_framework.change_state(stage4)

        else:
            cookie.handle_events(event)

def update():
    global cookie, background, ground, nomal_fork, nomal_thorn, special_fork, double_thorn, board, \
            score_jelly, hp_jelly, objects, score

    frame_time = get_frame_time()
    cookie.update(frame_time)
    background.update(frame_time)
    ground.update(frame_time)
    score.stage1_score()

    for list in objects:
        for dict in list:
            dict.update(frame_time)
            if collide(cookie, dict):
                if list == score_jelly:
                    list.remove(dict)
                    cookie.scoreSound(dict)
                elif list == hp_jelly:
                    list.remove(dict)
                    cookie.heal(dict)
                elif list == board:
                    for dict in list:
                        dict.state = "None"
                else:
                    cookie.state = "Collide"
    if background.map_size >= 55 and cookie.y == 200:
        game_framework.change_state(stage2_select)
    elif background.map_size >= 55 and cookie.y == 250:
        game_framework.change_state(stage3_select)

def draw():
    global cookie, background, ground, objects, score
    clear_canvas()
    background.draw()
    ground.draw()

    for list in objects:
        for dict in list:
            dict.draw()

    font.draw(100, 550, 'Score : %3.2d' % score.score, (255, 255, 255))
    cookie.draw()

    delay(0.03)
    update_canvas()
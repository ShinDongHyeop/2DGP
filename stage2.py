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
from score import *
import game_framework
import title_state
import stage1
import stage3
import stage4
import stage2_select

name = "MainState2"

background = None
brown_spear = None
oatmeal_spear = None
thorns = None
nasty_thorn = None
board = None
item_jelly = None
hp_jelly = None
objects = []
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
    global background, ground, brown_spear, oatmeal_spear, thorns, nasty_thorn, board, start, \
            score_jelly, hp_jelly, font, objects, cookie, score

    cookie = stage2_select.get_cookie
    background = Stage2_Background(800, 600)
    score = Score()
    ground = Stage2_Ground(800, 150)
    board = Stage2_Board().create()
    brown_spear = Stage2_Brown_Spear().create()
    oatmeal_spear = Stage2_Oatmeal_Spear().create()
    thorns = Stage2_Thorn().create()
    nasty_thorn = Stage2_Nasty_Thorn().create()
    score_jelly = Stage2_Score_Jelly().create()
    hp_jelly = Stage2_Hp_Jelly().create()
    objects = [brown_spear, oatmeal_spear, thorns, nasty_thorn, score_jelly, hp_jelly, board]
    font = load_font('Resource\\ENCR10B.TTF')
    start = time.time()

def exit():
    global background, ground, brown_spear, oatmeal_spear, thorns, nasty_thorn, board, start, end, \
            score_jelly, hp_jelly
    del(cookie)
    del(background)
    del(ground)

    for list in objects:
        for dict in list:
            list.remove(dict)
            del(dict)
        del(list)

    end = time.time()

    print("Stage2 Clear Time : ", (end - start))

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

        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            game_framework.change_state(stage1)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
            game_framework.change_state(stage3)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_4:
            game_framework.change_state(stage4)

        else:
            cookie.handle_events(event)

def update():
    global cookie, brown_spear, oatmeal_spear, thorns, nasty_thorn, board, \
            score_jelly, hp_jelly, objects

    frame_time = get_frame_time()
    cookie.update(frame_time)
    background.update(frame_time)
    ground.update(frame_time)
    score.stage2_score()

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
        game_framework.change_state(stage4)
    elif background.map_size >= 55 and cookie.y == 250:
        game_framework.change_state(stage3)



def draw():
    global cookie, background, ground, objects, score

    clear_canvas()
    background.draw()

    for list in objects:
        for dict in list:
            dict.draw()

    font.draw(100, 550, 'Score : %3.2d' % score.score, (255, 255, 255))
    ground.draw()
    cookie.draw()

    delay(0.03)
    update_canvas()
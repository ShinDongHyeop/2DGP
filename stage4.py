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
import stage1
import stage2
import stage3

name = "MainState4"

brave_cookie = None
ginger_brave_cookie = None
background = None
blue_flowe = None
red_flowe = None
totem = None
dirty_totem = None
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
    global brave_cookie, ginger_brave_cookie, background, ground, blue_flower, red_flower, totem, dirty_totem, start, \
            score_jelly, hp_jelly, font, objects

    brave_cookie = Brave_Cookie()
    ginger_brave_cookie = Ginger_Brave_Cookie()
    background = Stage4_Background(800, 600)
    ground = Stage4_Ground(800, 150)
    blue_flower = Stage4_Blue_Flower().create()
    red_flower = Stage4_Red_Flower().create()
    totem = Stage4_Totem().create()
    dirty_totem = Stage4_Dirty_Totem().create()
    score_jelly = Stage4_Score_Jelly().create()
    hp_jelly = Stage4_Hp_Jelly().create()
    objects = [blue_flower, red_flower, totem, dirty_totem, score_jelly, hp_jelly]
    font = load_font('Resource\\ENCR10B.TTF')
    start = time.time()

def exit():
    global brave_cookie, ginger_brave_cookie, background, ground, blue_flower, red_flower, totem, dirty_totem, start, end, \
            score_jelly, hp_jelly, objects

    del(brave_cookie)
    del(ginger_brave_cookie)
    del(background)
    del(ground)

    for list in objects:
        for dict in list:
            list.remove(dict)
            del(dict)
        del(list)

    end = time.time()

    print("Stage4 Clear Time : ", (end - start))

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

        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            game_framework.change_state(stage1)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            game_framework.change_state(stage2)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
            game_framework.change_state(stage3)

        else:
            brave_cookie.handle_events(event)
            ginger_brave_cookie.handle_events(event)

def update():
    global brave_cookie, ginger_brave_cookie, background, ground, blue_flower, red_flower, totem, dirty_totem, \
            score_jelly, hp_jelly, objects

    frame_time = get_frame_time()
    brave_cookie.update(frame_time)
    ginger_brave_cookie.update(frame_time)
    background.update(frame_time)
    ground.update(frame_time)

    for list in objects:
        for dict in list:
            dict.update(frame_time)
            if collide(brave_cookie, dict):
                if list == score_jelly:
                    list.remove(dict)
                    brave_cookie.scoreSound(dict)
                elif list == hp_jelly:
                    list.remove(dict)
                    brave_cookie.heal(dict)
                else:
                    brave_cookie.state = "Collide"

    if brave_cookie.map_size >= 51 and brave_cookie.y == 200:
        game_framework.change_state(title_state)

def draw():
    global brave_cookie, background, ground, blue_flower, red_flower, totem, dirty_totem, score_jelly, hp_jelly, \
            objects

    clear_canvas()
    background.draw()
    ground.draw()

    for list in objects:
        for dict in list:
            dict.draw()

    font.draw(100, 550, 'Score : %3.2d' % brave_cookie.score, (255, 255, 255))
    brave_cookie.draw()

    delay(0.03)
    update_canvas()
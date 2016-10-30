import random
import json
import os
import time

from pico2d import *
from cookie import *
from map import *
from obstacle import *
import game_framework
import title_state
import main_state
import main_state2
import main_state3

name = "MainState"

brave_cookie = None
ginger_brave_cookie = None
background = None
blue_flowe = None
red_flowe = None
totem = None
dirty_totem = None
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
    global brave_cookie, ginger_brave_cookie, background, blue_flower, red_flower, totem, dirty_totem, w_len, start
    brave_cookie = Brave_Cookie("Run")
    ginger_brave_cookie = Ginger_Brave_Cookie("Run")
    background = Stage4_Background()
    blue_flower = Stage4_Blue_Flower().create()
    red_flower = Stage4_Red_Flower().create()
    totem = Stage4_Totem().create()
    dirty_totem = Stage4_Dirty_Totem().create()
    w_len = 0
    start = time.time()

def exit():
    global brave_cookie, ginger_brave_cookie, background, blue_flower, red_flower, totem, dirty_totem, start, end
    del(brave_cookie)
    del(ginger_brave_cookie)
    del(background)

    for Spear in totem:
        totem.remove(Spear)
        del (Spear)
    del (totem)

    for Spear in dirty_totem:
        dirty_totem.remove(Spear)
        del (Spear)
    del (dirty_totem)

    for Thorn in blue_flower:
        blue_flower.remove(Thorn)
        del(Thorn)
    del (blue_flower)

    for Thorn in red_flower:
        red_flower.remove(Thorn)
        del (Thorn)
    del (red_flower)

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
            game_framework.change_state(main_state)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            game_framework.change_state(main_state2)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
            game_framework.change_state(main_state3)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if brave_cookie == Brave_Cookie:
                brave_cookie = Ginger_Brave_Cookie(brave_cookie.state)
            elif brave_cookie == Ginger_Brave_Cookie:
                brave_cookie = Brave_Cookie(brave_cookie.state)
        else:
            brave_cookie.handle_events(event)
            ginger_brave_cookie.handle_events(event)

def update():
    global brave_cookie, ginger_brave_cookie, blue_flower, red_flower, totem, dirty_totem, w_len
    w_len += 1

    frame_time = get_frame_time()
    brave_cookie.update()
    ginger_brave_cookie.update()

    for Spear in dirty_totem:
        Spear.update(frame_time)
        if collide(brave_cookie, Spear):
            brave_cookie.bump()
            dirty_totem.remove(Spear)
    for Spear in totem:
        Spear.update(frame_time)
        if collide(brave_cookie, Spear):
            brave_cookie.bump()
            totem.remove(Spear)
    for Thorn in blue_flower:
        Thorn.update(frame_time)
        if collide(brave_cookie, Thorn):
            brave_cookie.bump()
            blue_flower.remove(Thorn)
    for Thorn in red_flower:
        Thorn.update(frame_time)
        if collide(brave_cookie, Thorn):
            brave_cookie.bump()
            red_flower.remove(Thorn)

    if w_len == 1550 and brave_cookie.y == 200:
        game_framework.change_state(title_state)


def draw():
    global brave_cookie, background, blue_flower, red_flower, totem, dirty_totem
    clear_canvas()
    background.draw()

    for Spear in dirty_totem:
        Spear.draw()
        Spear.draw_bb()
    for Spear in totem:
        Spear.draw()
        Spear.draw_bb()
    for Thorn in blue_flower:
        Thorn.draw()
        Thorn.draw_bb()
    for Thorn in red_flower:
        Thorn.draw()
        Thorn.draw_bb()

    brave_cookie.draw()

    delay(0.03)
    update_canvas()
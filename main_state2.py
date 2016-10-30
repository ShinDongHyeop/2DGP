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
import main_state3
import main_state4

name = "MainState"

brave_cookie = None
ginger_brave_cookie = None
background = None
brown_spear = None
oatmeal_spear = None
thorns = None
nasty_thorn = None
board = None
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
    global brave_cookie, ginger_brave_cookie, background, brown_spear, oatmeal_spear, thorns, nasty_thorn, w_len, board, start
    brave_cookie = Brave_Cookie("Run")
    ginger_brave_cookie = Ginger_Brave_Cookie("Run")
    background = Stage2_Background()
    board = Stage2_Board().create()
    brown_spear = Stage2_Brown_Spear().create()
    oatmeal_spear = Stage2_Oatmeal_Spear().create()
    thorns = Stage2_Thorn().create()
    nasty_thorn = Stage2_Nasty_Thorn().create()
    w_len = 0
    start = time.time()

def exit():
    global brave_cookie, ginger_brave_cookie, background, brown_spear, oatmeal_spear, thorns, nasty_thorn, board, start, end
    del(brave_cookie)
    del(ginger_brave_cookie)
    del(background)

    for spear in brown_spear:
        brown_spear.remove(spear)
        del (spear)
    del (brown_spear)

    for spear in oatmeal_spear:
        oatmeal_spear.remove(spear)
        del (spear)
    del (oatmeal_spear)

    for thorn in thorns:
        thorns.remove(thorn)
        del (thorn)
    del (thorns)

    for thorn in nasty_thorn:
        nasty_thorn.remove(thorn)
        del (thorn)
    del (nasty_thorn)

    for foothold in board:
        board.remove(foothold)
        del(foothold)
    del(board)

    end = time.time()

    print("Stage2 Clear Time : ", (end - start))

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

        elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
            game_framework.change_state(main_state3)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_4:
            game_framework.change_state(main_state4)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if brave_cookie == Brave_Cookie:
                brave_cookie = Ginger_Brave_Cookie(brave_cookie.state)
            elif brave_cookie == Ginger_Brave_Cookie:
                brave_cookie = Brave_Cookie(brave_cookie.state)
        else:
            brave_cookie.handle_events(event)
            ginger_brave_cookie.handle_events(event)

def update():
    global brave_cookie, ginger_brave_cookie, brown_spear, oatmeal_spear, thorns, nasty_thorn, w_len, board
    w_len += 1

    brave_cookie.update()
    ginger_brave_cookie.update()
    frame_time = get_frame_time()

    for Spear in brown_spear:
        Spear.update(frame_time)
    for Spear in oatmeal_spear:
        Spear.update(frame_time)
    for Thorn in thorns:
        Thorn.update(frame_time)
    for Thorn in nasty_thorn:
        Thorn.update(frame_time)

    for foothold in board:
        foothold.update(frame_time)

    if w_len == 1550 and brave_cookie.y == 200:
        game_framework.change_state(main_state3)
    elif w_len == 1550 and brave_cookie.y == 250:
        game_framework.change_state(main_state4)


def draw():
    global brave_cookie, background, brown_spear, oatmeal_spear, thorns, nasty_thorn,board
    clear_canvas()
    background.draw()

    for Spear in brown_spear:
        Spear.draw()
        Spear.draw_bb()
    for Spear in oatmeal_spear:
        Spear.draw()
        Spear.draw_bb()
    for Thorn in thorns:
        Thorn.draw()
        Thorn.draw_bb()
    for Thorn in nasty_thorn:
        Thorn.draw()
        Thorn.draw_bb()

    for foothold in board:
        foothold.draw()

    background.grounddraw()
    brave_cookie.draw()
    brave_cookie.draw_bb()

    delay(0.03)
    update_canvas()
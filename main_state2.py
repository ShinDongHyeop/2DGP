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
    global brave_cookie, ginger_brave_cookie, background, ground, brown_spear, oatmeal_spear, thorns, nasty_thorn, board, start, \
            score_jelly, hp_jelly, font

    brave_cookie = Brave_Cookie("Run")
    ginger_brave_cookie = Ginger_Brave_Cookie("Run")
    background = Stage2_Background(800, 600)
    ground = Stage2_Ground(800, 150)
    board = Stage2_Board().create()
    brown_spear = Stage2_Brown_Spear().create()
    oatmeal_spear = Stage2_Oatmeal_Spear().create()
    thorns = Stage2_Thorn().create()
    nasty_thorn = Stage2_Nasty_Thorn().create()
    score_jelly = Stage2_Score_Jelly().create()
    hp_jelly = Stage2_Hp_Jelly().create()
    font = load_font('Resource\\ENCR10B.TTF')
    start = time.time()

def exit():
    global brave_cookie, ginger_brave_cookie, background, ground, brown_spear, oatmeal_spear, thorns, nasty_thorn, board, start, end, \
            score_jelly, hp_jelly
    del(brave_cookie)
    del(ginger_brave_cookie)
    del(background)
    del(ground)

    for item in score_jelly:
        score_jelly.remove(item)
        del(item)
    del(score_jelly)

    for item in hp_jelly:
        hp_jelly.remove(item)
        del(item)
    del(hp_jelly)

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
            if type(brave_cookie) == Brave_Cookie:
                brave_cookie = Ginger_Brave_Cookie(brave_cookie.state)
            elif type(brave_cookie) == Ginger_Brave_Cookie:
                brave_cookie = Brave_Cookie(brave_cookie.state)
        else:
            brave_cookie.handle_events(event)
            ginger_brave_cookie.handle_events(event)

def update():
    global brave_cookie, ginger_brave_cookie, brown_spear, oatmeal_spear, thorns, nasty_thorn, board, \
            score_jelly, hp_jelly

    frame_time = get_frame_time()
    brave_cookie.update()
    ginger_brave_cookie.update()
    background.update(frame_time)
    ground.update(frame_time)

    for item in score_jelly:
        item.update(frame_time)
        if collide(brave_cookie, item):
            score_jelly.remove(item)
            brave_cookie.scoreSound(item)
    for item in hp_jelly:
        item.update(frame_time)
        if collide(brave_cookie, item):
            hp_jelly.remove(item)
            brave_cookie.heal(item)

    for Spear in brown_spear:
        Spear.update(frame_time)
        if collide(brave_cookie, Spear) and brave_cookie.state != "Collide":
            brave_cookie.bump("Collide")
    for Spear in oatmeal_spear:
        Spear.update(frame_time)
        if collide(brave_cookie, Spear) and brave_cookie.state != "Collide":
            brave_cookie.bump("Collide")
    for Thorn in thorns:
        Thorn.update(frame_time)
        if collide(brave_cookie, Thorn) and brave_cookie.state != "Collide":
            brave_cookie.bump("Collide")
    for Thorn in nasty_thorn:
        Thorn.update(frame_time)
        if collide(brave_cookie, Thorn) and brave_cookie.state != "Collide":
            brave_cookie.bump("Collide")

    for foothold in board:
        foothold.update(frame_time)

    if brave_cookie.hp <= 0:
        # brave_cookie.map_size += 0
        # print(brave_cookie.map_size)
        game_framework.change_state(title_state)

    if brave_cookie.map_size == 1550 and brave_cookie.y == 200:
        game_framework.change_state(main_state4)
    elif brave_cookie.map_size == 1550 and brave_cookie.y == 250:
        game_framework.change_state(main_state3)



def draw():
    global brave_cookie, ginger_brave_cookie, background, ground, brown_spear, oatmeal_spear, thorns, nasty_thorn, board, \
        score_jelly, hp_jelly

    clear_canvas()
    background.draw()

    for item in score_jelly:
        item.draw()
    for item in hp_jelly:
        item.draw()

    for Spear in brown_spear:
        Spear.draw()
    for Spear in oatmeal_spear:
        Spear.draw()
    for Thorn in thorns:
        Thorn.draw()
    for Thorn in nasty_thorn:
        Thorn.draw()

    for foothold in board:
        foothold.draw()

    font.draw(100, 550, 'Score : %3.2d' % brave_cookie.score, (255, 255, 255))
    ground.draw()
    brave_cookie.draw()

    delay(0.03)
    update_canvas()
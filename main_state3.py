import random
import json
import os
import time

from pico2d import *
from cookie import *
from map import *
from obstacle import *
from item import *
import game_framework
import title_state
import main_state
import main_state2
import main_state4

name = "MainState"

brave_cookie = None
ginger_brave_Cookie = None
background = None
palm_tree = None
hate_palm_tree = None
fence = None
conch = None
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
    global brave_cookie, ginger_brave_cookie, background, ground, palm_tree, hate_palm_tree, fence, conch, board, start, \
            score_jelly, hp_jelly

    brave_cookie = Brave_Cookie("Run")
    ginger_brave_cookie = Ginger_Brave_Cookie("Run")
    background = Stage3_Background(800, 600)
    ground = Stage3_Background(800, 150)
    palm_tree = Stage3_Palm_Tree().create()
    hate_palm_tree = Stage3_Hate_Palm_Tree().create()
    fence = Stage3_Fence().create()
    conch = Stage3_Conch().create()
    board = Stage2_Board().create()
    score_jelly = Stage3_Score_Jelly().create()
    hp_jelly = Stage3_Hp_Jelly().create()

    start = time.time()

def exit():
    global brave_cookie, ginger_brave_cookie, background, ground, palm_tree, hate_palm_tree, fence, conch, board, start, end, \
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

    for Spear in palm_tree:
        palm_tree.remove(Spear)
        del (Spear)
    del (palm_tree)
    for Spear in hate_palm_tree:
        hate_palm_tree.remove(Spear)
        del (Spear)
    del (hate_palm_tree)
    for Thorn in fence:
        fence.remove(Thorn)
        del(Thorn)
    del (fence)
    for Thorn in conch:
        conch.remove(Thorn)
        del (Thorn)
    del (conch)

    for foothold in board:
        board.remove(foothold)
        del(foothold)
    del(board)

    end = time.time()

    print("Stage3 Clear Time : ", (end - start))

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
    global brave_cookie, ginger_brave_cookie, background, ground, palm_tree, hate_palm_tree, fence, conch, board, \
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
    for item in hp_jelly:
        item.update(frame_time)
        if collide(brave_cookie, item):
            hp_jelly.remove(item)
            brave_cookie.heal()

    for Spear in palm_tree:
        Spear.update(frame_time)
        if collide(brave_cookie, Spear) and brave_cookie.state != "Collide":
            brave_cookie.bump("Collide")
    for Spear in hate_palm_tree:
        Spear.update(frame_time)
        if collide(brave_cookie, Spear) and brave_cookie.state != "Collide":
            brave_cookie.bump("Collide")
    for thorn in conch:
        thorn.update(frame_time)
        if collide(brave_cookie, thorn) and brave_cookie.state != "Collide":
            brave_cookie.bump("Collide")
    for Thorn in fence:
        Thorn.update(frame_time)
        if collide(brave_cookie, Thorn) and brave_cookie.state != "Collide":
            brave_cookie.bump("Collide")

    for foothold in board:
        foothold.update(frame_time)

    if brave_cookie.hp <= 0:
        brave_cookie.map_size += 0
        print(brave_cookie.map_size)
        brave_cookie = ginger_brave_cookie

    if brave_cookie.map_size == 1550 and brave_cookie.y == 200:
        game_framework.change_state(main_state2)
    elif brave_cookie.map_size == 1550 and brave_cookie.y == 250:
        game_framework.change_state(main_state4)

def draw():
    global brave_cookie, ginger_brave_cookie, background, ground, palm_tree, hate_palm_tree, fence, conch, board, \
            score_jelly, hp_jelly

    clear_canvas()
    background.draw()
    ground.ground_draw()

    for item in score_jelly:
        item.draw()
        #item.draw_bb()
    for item in hp_jelly:
        item.draw()
        #item.draw_bb()

    for Spear in palm_tree:
        Spear.draw()
        #Spear.draw_bb()
    for Spear in hate_palm_tree:
        Spear.draw()
        #Spear.draw_bb()
    for Thorn in fence:
        Thorn.draw()
        #Thorn.draw_bb()
    for Thorn in conch:
        Thorn.draw()
        #Thorn.draw_bb()

    for foothold in board:
        foothold.draw()

    brave_cookie.draw()
    delay(0.03)
    update_canvas()
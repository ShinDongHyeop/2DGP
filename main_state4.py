import random
import json
import os
import time

from pico2d import *
from character import *
from map import *
from obstacle import *
import game_framework
import title_state
import main_state
import main_state2
import main_state3

name = "MainState"

brave_cookie = None
ginger_brave_Cookie = None
background = None
palm_tree = None
hate_palm_tree = None
fence = None
conch = None
board = None

def enter():
    global brave_cookie, ginger_brave_cookie, background, palm_tree, hate_palm_tree, fence, conch, board, w_len, start
    brave_cookie = Brave_Cookie("Run")
    ginger_brave_cookie = Ginger_Brave_Cookie("Run")
    background = Stage4_Background()
    palm_tree = Stage3_PalmTree.create()
    hate_palm_tree = Stage3_HatePalmTree.create()
    fence = Stage3_Fence.create()
    conch = Stage3_Conch.create()
    board = Stage2_Board.create()
    w_len = 0
    start = time.time()

def exit():
    global brave_cookie, ginger_brave_cookie, background, palm_tree, hate_palm_tree, fence, conch, board, start, end
    del(brave_cookie)
    del(ginger_brave_cookie)
    del(background)

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

        elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
            game_framework.change_state(main_state3)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if type(brave_cookie) == Brave_Cookie:
                brave_cookie = Ginger_Brave_Cookie(brave_cookie.state)
            elif type(brave_cookie) == Ginger_Brave_Cookie:
                brave_cookie = Brave_Cookie(brave_cookie.state)

        else:
            brave_cookie.handle_events(event)
            ginger_brave_cookie.handle_events(event)

def update():
    global brave_cookie, palm_tree, hate_palm_tree, fence, conch, w_len, board
    w_len += 1
    brave_cookie.update()

    for Spear in palm_tree:
        Spear.update()
    for Spear in hate_palm_tree:
        Spear.update()
    for Thorn in fence:
        Thorn.update()
    for Thorn in conch:
        Thorn.update()

    for foothold in board:
        foothold.update()

    if w_len == 2200 and brave_cookie.y == 200:
        game_framework.change_state(main_state2)
    elif w_len == 2200 and brave_cookie.y == 250:
        game_framework.change_state(main_state3)

def draw():
    global brave_cookie, ginger_brave_cookie, background, palm_tree, hate_palm_tree, fence, conch, board
    clear_canvas()
    background.draw()

    for Spear in palm_tree:
        Spear.draw()
    for Spear in hate_palm_tree:
        Spear.draw()
    for Thorn in fence:
        Thorn.draw()
    for Thorn in conch:
        Thorn.draw()

    for foothold in board:
        foothold.draw()

    brave_cookie.draw()
    delay(0.03)
    update_canvas()
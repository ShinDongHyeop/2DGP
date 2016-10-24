import random
import json
import os
import time

from pico2d import *
from Character import *
from Map import *
from Obstacle import *
import game_framework
import title_state
import main_state2
import main_state3
import main_state4

name = "MainState"

character = None
character2 = None
background = None
obstacle = None
obstacle2 = None
obstacle3 = None
obstacle4 = None
board = None

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def enter():
    global character, character2, background, obstacle, obstacle2, obstacle3, obstacle4,  w_len, board, start
    character = Character("Run")
    character2 = Character2("Run")
    background = Stage1_Background()
    board = Stage1_Board.create()
    obstacle = Stage1_Obstacle.create()
    obstacle2 = Stage1_Obstacle2.create()
    obstacle3 = Stage1_Obstacle3.create()
    obstacle4 = Stage1_Obstacle4.create()
    w_len = 0
    start = time.time()

def exit():
    global character, character2, background, obstacle, obstacle2, obstacle3, obstacle4, board, start
    del(character)
    del(character2)
    del(background)

    for i in obstacle:
        obstacle.remove(i)
        del(i)
    del(obstacle)

    for i in obstacle2:
        obstacle2.remove(i)
        del(i)
    del(obstacle2)

    for i in obstacle3:
        obstacle3.remove(i)
        del(i)
    del(obstacle3)

    for i in obstacle4:
        obstacle4.remove(i)
        del(i)
    del(obstacle4)

    for i in board:
        board.remove(i)
        del(i)
    del(board)

    end = time.time()

    print("Stage1 Clear Time : ", (end - start))


def pause():
    pass


def resume():
    pass


def handle_events():
    global character, character2
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
            if type(character) == Character:
                character = Character2(character.state)
            elif type(character) == Character2:
                character = Character(character.state)

        else:
            character.handle_events(event)
            character2.handle_events(event)

def update():
    global character, obstacle, obstacle2, obstacle3, obstacle4, w_len, board
    w_len += 1
    character.update()
    for Fork1 in obstacle:
        Fork1.update()
        if collide(character, Fork1):
            print("collision")
    for Thorn1 in obstacle2:
        Thorn1.update()
        if collide(character, Thorn1):
            print("collision")
    for Fork2 in obstacle3:
        Fork2.update()
        if collide(character, Fork2):
            print("collision")
    for Thorn2 in obstacle4:
        Thorn2.update()
        if collide(character, Thorn2):
            print("collision")

    for i in board:
        i.update()
    if w_len == 2200 and character.y == 200:
        game_framework.change_state(main_state2)
    elif w_len == 2200 and character.y == 250:
        game_framework.change_state(main_state3)

def draw():
    global character, background, obstacle, obstacle2, obstacle3, obstacle4, board
    clear_canvas()
    background.draw()

    for Fork1 in obstacle:
        Fork1.draw()
        Fork1.draw_bb()
    for Thorn1 in obstacle2:
        Thorn1.draw()
        Thorn1.draw_bb()
    for Fork2 in obstacle3:
        Fork2.draw()
        Fork2.draw_bb()
    for Thorn2 in obstacle4:
        Thorn2.draw()
        Thorn2.draw_bb()
    for i in board:
        i.draw()
    character.draw()
    character.draw_bb()

    delay(0.03)
    update_canvas()
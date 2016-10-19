import random
import json
import os

from pico2d import *
from Character import *
from Map import *
from Obstacle import *
import game_framework
import title_state
import main_state
import main_state2
import main_state4

name = "MainState"

character = None
character2 = None
background = None
obstacle = None
obstacle2 = None
board = None

def enter():
    global character, character2, background, obstacle, obstacle2, board, w_len
    character = Character("Run")
    character2 = Character2("Run")
    background = Stage3_Background()
    obstacle = Stage3_Obstacle.create()
    obstacle2 = Stage3_Obstacle2.create()
    board = Stage2_Board.create()
    w_len = 0

def exit():
    global character, character2, background, obstacle, obstacle2, board
    del(character)
    del(character2)
    del(background)

    for i in obstacle:
        obstacle.remove(i)
        del (i)
    del (obstacle)

    for i in obstacle2:
        obstacle2.remove(i)
        del (i)
    del (obstacle2)

    for i in board:
        board.remove(i)
        del(i)
    del(board)

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

        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            game_framework.change_state(main_state)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            game_framework.change_state(main_state2)

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
    global obstacle, obstacle2, board, w_len
    character.update()
    for i in obstacle:
        i.update()
    for i in obstacle2:
        i.update()

    for i in board:
        i.update()

    if w_len == 2200 and character.y == 200:
        game_framework.change_state(main_state2)
    elif w_len == 2200 and character.y == 250:
        game_framework.change_state(main_state4)

def draw():
    global character, character2, background, obstacle, obstacle2, board
    clear_canvas()
    background.draw()

    for i in obstacle:
        i.draw()
    for i in obstacle2:
        i.draw()

    for i in board:
        i.draw()
    character.draw()
    delay(0.03)
    update_canvas()
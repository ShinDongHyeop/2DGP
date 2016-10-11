import random
import json
import os

from pico2d import *
from Character import *
from Map import *
from Obstacle import *
import game_framework
import title_state

name = "MainState"

character = None
character2 = None
background = None
obstacle = None

def enter():
    global character, character2, background, obstacle
    character = Character()
    character2 = Character2()
    background = Stage1_Background()
    obstacle = Stage1_Obstacle()

def exit():
    global character, character2, background, obstacle
    del(character)
    del(character2)
    del(background)
    del(obstacle)

def pause():
    pass


def resume():
    pass


def handle_events():
    global character
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            character.handle_events(event)
            character2.handle_events(event)

def update():
    character.update()
    character2.update()
    obstacle.update()

def draw():
    global character, background, obstacle
    clear_canvas()
    background.draw()
    character.draw()
    character2.draw()
    obstacle.draw()
    delay(0.03)
    update_canvas()









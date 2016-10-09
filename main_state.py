import random
import json
import os

from pico2d import *
from Character import *
from Character2 import *
from Map import *
import game_framework
import title_state


name = "MainState"

character = None
character2 = None
background = None

def enter():
    global character, character2, background
    character = Character()
    character2 = Character2()
    background = Stage1_Background()

def exit():
    global character, character2, background
    del(character)
    del(character2)
    del(background)

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

def draw():
    global character
    clear_canvas()
    background.draw()
    character.draw()
    character2.draw()
    delay(0.03)
    update_canvas()









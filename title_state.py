import game_framework
import stage1_select
import stage2_select
import stage3_select
import stage4_select

from pico2d import *


name = "TitleState"
image = None


def enter():
    global image
    image = load_image('Resource\\title.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(stage1_select)
            elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
                game_framework.change_state(stage2_select)
            elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
                game_framework.change_state(stage3_select)
            elif event.type == SDL_KEYDOWN and event.key == SDLK_4:
                game_framework.change_state(stage4_select)


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass







import game_framework
from score import *

from pico2d import *


name = "TitleState"
image = None


def enter():
    global title, result, font, x, y, score
    title = load_image('Resource\\title.png')
    result = load_image('Resource\\result.png')
    font = load_font('Resource\\ENCR10B.TTF', 100)
    score = Score()
    x = 0
    y = 0

def exit():
    global image
    del(image)


def handle_events():
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

            elif event.type == SDL_MOUSEMOTION:
                x, y = event.x, 599 - event.y

            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                if (x >= 191 and x <= 387) and (y >= 27 and y <= 103):
                    game_framework.quit()
def draw():
    global x, y, font, score
    clear_canvas()
    result.draw(400, 300)
    font.draw(290, 380, '%3.2d' % score.score, (81, 35, 200))
    print("x좌표 : ",x , "y좌표 : ", y)

    update_canvas()

def update():
    pass


def pause():
    pass


def resume():
    pass







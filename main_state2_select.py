from back_ground import *
from ground import *
from pico2d import *
from cookie import *
import game_framework
import main_state2



name = "MainState2Select"
background = None
ground = None
brave_cookie = None
ginger_brave_cookie = None
brave_select = None
ginger_select = None
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
    global background, ground, brave_cookie, ginger_brave_cookie, brave_select, ginger_select, \
            brave_hp, ginger_hp, x, y
    background = Stage2_Background(800,600)
    ground = Stage2_Ground(800,150)
    brave_cookie = Brave_Cookie_Select("Run")
    ginger_brave_cookie = Ginger_Brave_Cookie_Select("Run")
    brave_select = load_image('Resource\\game_start_button.png')
    ginger_select = load_image('Resource\\game_start_button.png')
    brave_hp = load_image('Resource\\Item\\hp.png')
    ginger_hp = load_image('Resource\\Item\\hp.png')
    x = 0
    y = 0
def exit():
    global background, ground, brave_cookie, ginger_brave_cookie
    del(background)
    del(ground)
    del(brave_cookie)
    del(ginger_brave_cookie)


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
                x ,y = event.x, 599 - event.y


def draw():
    global brave_cookie, ginger_brave_cookie, brave_select, ginger_select
    clear_canvas()
    background.draw()
    ground.draw()

    brave_cookie.draw()
    ginger_brave_cookie.draw()

    brave_select.draw(250, 100)
    ginger_select.draw(550, 100)

    brave_hp.draw_to_origin(150, 300, Brave_Cookie.hp, 50)
    ginger_hp.draw_to_origin(450, 300, Ginger_Brave_Cookie.hp, 50)

    brave_cookie.draw_bb()
    ginger_brave_cookie.draw_bb()

    update_canvas()

def update():
    global x, y
    frame_time = get_frame_time()
    background.update(frame_time)
    ground.update(frame_time)
    brave_cookie.update()
    ginger_brave_cookie.update()
    print(x, y)
    delay(0.03)


def pause():
    pass


def resume():
    pass







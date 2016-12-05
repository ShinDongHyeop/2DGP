import game_framework
from pico2d import *


import result_state


name = "RankingState"
image = None

def enter():
    global image, font
    font = load_font('Resource\\ENCR10B.TTF', 40)
    image = load_image('Resource\\blackboard.png')

def exit():
    global image, font
    del(image)
    del(font)


def pause():
    pass

def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()



def update():
    pass

def draw_ranking():
    def my_sort(a):
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i]['score'] < a[j]['score']:
                    a[i], a[j] = a[j], a[i]
    y = 0
    f = open('ranking_data.txt', 'r')
    ranking_data = json.load(f)
    f.close()

    my_sort(ranking_data)
    for data in ranking_data[:10]:
        y += 1
        font.draw(100, 450-40 * y, 'Score:%4.1f' % (data['score']), (255,255,255))
    font.draw(300, 500, "[RANKING]", (255, 255, 255))
def draw():
    global image, font
    clear_canvas()
    image.draw(400, 300)
    draw_ranking()
    update_canvas()




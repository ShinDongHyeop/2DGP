from pico2d import *
open_canvas()
character = load_image('cookie_run_dead.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

x = 0
frame = 0
running = True
while(running):
    clear_canvas()
    #grass.draw(400, 30)
    #cookie_run
    #character.clip_draw(frame * 75, 0, 75, 100, x, 90)
    #frame = (frame + 1 ) % 6

    # cookie_run_dead
    #character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    #frame = (frame + 1 ) % 3

    # cookie_run_jump,jump2, slide
    #character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    #frame = (frame + 1 ) % 1
    update_canvas()
    x += 10
    delay(0.05)
    handle_events()

close_canvas()


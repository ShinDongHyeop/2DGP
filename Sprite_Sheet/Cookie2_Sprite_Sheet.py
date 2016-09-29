from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('Cookie2_Slide.png')

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
    grass.draw(400, 30)
    #Cookie2_Run
    #character.clip_draw(frame * 48, 0, 48, 100, x, 90)
    #frame = (frame + 1 ) % 3

    # Cookie2_Dead
    #character.clip_draw(frame * 60, 0, 60, 100, x, 90)
    #frame = (frame + 1 ) % 2

    # Cookie2_Jump
    #character.clip_draw(frame * 52, 0, 52, 100, x, 90)
    #frame = (frame + 1 ) % 3

    # Cookie2_Slide
    #character.clip_draw(frame * 70, 0, 70, 100, x, 90)
    #frame = (frame + 1 ) % 2
    update_canvas()
    x += 10
    delay(0.05)
    handle_events()

close_canvas()


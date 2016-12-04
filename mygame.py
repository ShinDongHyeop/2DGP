from pico2d  import *
import game_framework
import start_state
import title_state
import result_state
open_canvas(sync = True)

game_framework.run(result_state)
import GameFrameWork
from pico2d import *

import StartState

name = "EvolutionState"

time = None
black = None

def enter():
    global time, black
    time = 0

    if black == None:
        black = load_image("resource/black.png")
        black.opacify(0.3)

def exit():
    pass

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameFrameWork.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            GameFrameWork.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            GameFrameWork.pop_state()
        else:
            if StartState.eevee.evolution(event):
                GameFrameWork.pop_state()

def update(frame_time):
    global time
    time += frame_time

    if time > 3:
        GameFrameWork.pop_state()

def draw(frame_time):
    global black

    clear_canvas()

    StartState.drawObject(frame_time)

    black.draw(300, 300)

    StartState.eevee.draw()
    StartState.ui.draw_evolution()

    update_canvas()
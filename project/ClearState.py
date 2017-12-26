import GameFrameWork
from pico2d import *

import StartState
import TitleState

name = "ClearState"

time = None
image = None

def enter():
    global time, image

    image = load_image("resource/clear.png")
    time = 0


def exit():
    global image

    #del(image)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameFrameWork.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            GameFrameWork.quit()
        elif event.type == SDL_KEYDOWN:
            GameFrameWork.pop_state()
            GameFrameWork.change_state(TitleState)

def update(frame_time):
    StartState.update(frame_time)

def draw(frame_time):

    clear_canvas()

    StartState.drawObject(frame_time)

    image.draw(300, 300)

    update_canvas()

def pause():
    pass

def resume():
    pass
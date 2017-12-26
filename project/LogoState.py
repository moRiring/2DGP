import GameFrameWork
from pico2d import *

import TitleState

name = "ClearState"

time = None
image = None

def enter():
    open_canvas(600, 600)

    global time, image
    time = 0
    image = load_image("resource/logo.png")

def exit():
    global image

    del(image)

    pass

def handle_events(frame_time):
    pass

def update(frame_time):
    global time
    time += frame_time

    if time > 1:
        GameFrameWork.change_state(TitleState)

def draw(frame_time):
    clear_canvas()

    if time % 0.5 > 0.25:
        image.clip_draw(0, 0, 600, 600, 300, 300)
    else:
        image.clip_draw(600, 0, 600, 600, 300, 300)

    update_canvas()

def pause():
    pass

def resume():
    pass
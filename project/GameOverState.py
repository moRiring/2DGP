import GameFrameWork
from pico2d import *

import StartState
import TitleState

name = "GameOverState"

time = None
image = None
black = None

def enter():
    global time, image, black
    time = 0
    image = load_image("resource/gameover.png")
    black = load_image("resource/black.png")

def exit():
    global image, black
    del (image)
    del(black)
    pass

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameFrameWork.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            GameFrameWork.quit()
        elif event.type == SDL_KEYDOWN and time >= 3:
            GameFrameWork.pop_state()
            GameFrameWork.change_state(TitleState)

def update(frame_time):
    global time, image, black
    time += frame_time

    if time > 3:
        time = 3

    image.opacify(time / 3)
    black.opacify(time / 3 / 2)

    StartState.update(frame_time)

def draw(frame_time):

    clear_canvas()

    StartState.drawObject(frame_time)

    black.draw(300, 300)
    image.draw(300, 300)

    update_canvas()

def pause():
    pass
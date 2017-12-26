import GameFrameWork
from pico2d import *

import StartState

from BackGround import BackGround
from Grass import Grass

name = "TitleState"

title = None
act = None
y = None
dir = None
black = None
background = None
grass = None
to_start = None
frame = None

music = None

def enter():
    global act, title, y, dir, black, background, grass, to_start, frame, music
    act = 0
    dir = -1
    y = 800
    frame = 0

    background = BackGround(150)
    grass = Grass(150)

    to_start = load_image("resource/to_start.png")
    title = load_image("resource/title.png")
    black = load_image("resource/black.png")

def exit():
    global act, title, y, dir, black, background, grass, to_start
    del (act)
    del(title)
    del (y)
    del (dir)
    del(black)
    del(background)
    del(grass)
    del(to_start)

def handle_events(frame_time):

    global music

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameFrameWork.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            GameFrameWork.quit()
        elif event.type == SDL_KEYDOWN and act > 7:
            GameFrameWork.change_state(StartState)

def update(frame_time):
    global y, dir, act, frame

    frame = (frame + (frame_time * 2)) % 4

    background.update(frame_time)
    grass.update(frame_time)

    y += dir * frame_time * 500
    y += -1 * frame_time * 200

    if dir == 1 and y > 600 -  act * 50:
        y = 600 - act * 50
        dir = -1 * dir

    if y < 400:
        y = 400
        act += 1
        dir = -1 * dir



def draw(frame_time):
    global title, black, to_start

    clear_canvas()

    black.draw(300,750)

    background.draw()
    grass.draw()

    title.draw(300, y - 50)
    if(act>7):
        to_start.clip_draw(0, ((int)(to_start.h // 4) * (int)(frame)) ,(int)(to_start.w), (int)(to_start.h) // 4 , 300, 250)

    black.draw(300, -150)

    update_canvas()
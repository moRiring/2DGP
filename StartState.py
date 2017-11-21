import GameFrameWork

from pico2d import *

from Eevee import Eevee
from BackGround import BackGround
from Grass import Grass

name = "StartState"

eevee = None
background = None
grass = None

def enter():
    global eevee, background, grass

    open_canvas(600, 600)

    eevee = Eevee()
    background = BackGround()
    grass = Grass()


def exit():
    global eevee, background, grass

    del(eevee)
    del(background)
    del(grass)


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameFrameWork.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            GameFrameWork.quit()
        else:
            eevee.handle_event(event, frame_time)


def update(frame_time):
    background.update(frame_time)
    grass.update(frame_time)
    eevee.update(frame_time)


def drawObject(frame_time):
    background.draw()
    grass.draw()
    eevee.draw()

def draw(frame_time):
    clear_canvas()
    drawObject(frame_time)
    update_canvas()
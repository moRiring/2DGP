from BackGround import BackGround
from pico2d import *
import collision

import GameFrameWork
from Eevee import Eevee
from Grass import Grass
from Map import Map
from  UI import UI

name = "StartState"

eevee = None
background = None
grass = None
map = None
ui = None

ITEM, MONSTER = 0, 1

def enter():
    global eevee, background, grass, map, ui

    open_canvas(600, 300)

    eevee = Eevee()
    background = BackGround()
    grass = Grass()
    map = Map()
    ui = UI()


def exit():
    global eevee, background, grass, map, ui

    del(eevee)
    del(background)
    del(grass)
    del(map)
    del(ui)


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
    map.update(frame_time)
    eevee.update(frame_time)

    for data in map.map:
        if collision.collide(eevee, data):
            if data.object_TYPE == ITEM:
                if data.state == data.NONE:
                    eevee.get_item(data.type)
                    data.get()


def drawObject(frame_time):
    background.draw()
    grass.draw()
    map.draw()
    eevee.draw()
    ui.draw(eevee)


def draw(frame_time):
    clear_canvas()
    drawObject(frame_time)
    update_canvas()
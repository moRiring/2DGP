import GameFrameWork
from pico2d import *

import EvolutionState

import collision

from BackGround import BackGround
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

    ui.set_eevee(eevee)

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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a and eevee.state == eevee.RUN:
            GameFrameWork.push_state(EvolutionState)
        else:
            eevee.handle_event(event, frame_time)


def update(frame_time):
    background.update(frame_time)
    grass.update(frame_time)
    map.update(frame_time)
    eevee.update(frame_time)

    for data in map.map:
        data.update(frame_time)
        if collision.collide(eevee, data):
            if data.object_TYPE == "ITEM":
                if data.state == data.NONE:
                    eevee.get_item(data.type)
                    data.get()
            if data.object_TYPE == "MONSTER":
                if data.state != data.DIE:
                    if eevee.state == eevee.ATTACK:
                        data.die()
                    else:
                        eevee.hit()


def drawObject(frame_time):
    background.draw()
    grass.draw()
    map.draw()
    #map보다 object
    eevee.draw()
    ui.draw()
    #eevee의 레퍼런스는 바뀌지 x, ui 내부에 get_eevee(eevee)함수 구현


def draw(frame_time):
    clear_canvas()

    drawObject(frame_time)

    update_canvas()


def pause():
    pass


def resume():
    pass
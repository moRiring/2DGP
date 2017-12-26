import GameFrameWork
from pico2d import *

import EvolutionState
import ClearState
import GameOverState

import collision
from animation import Animation

from BackGround import BackGround
from Eevee import Eevee
from Grass import Grass
from Map import Map
from  UI import UI
from Boss import Boss

name = "StartState"

animation = None

eevee = None
down_background = None
down_grass = None
up_background = None
up_grass = None
map = None
ui = None
boss = None

ITEM, MONSTER = 0, 1

def enter():
    global eevee, up_background, up_grass, map, ui, animation, boss, down_background, down_grass

    eevee = Eevee()
    down_background = BackGround(0)
    down_grass = Grass(0)
    up_background = BackGround(300)
    up_grass = Grass(300)
    map = Map()
    ui = UI()
    animation = Animation()
    boss = Boss()

    ui.set_eevee(eevee)
    boss.set_eevee(eevee)

    up_background.music.repeat_play()

def exit():
    global eevee, up_background, up_grass, map, ui, down_background, down_grass

    del(eevee)
    del(up_background)
    del(up_grass)
    del (down_background)
    del (down_grass)
    for data in map.map:
        del(data)
    del(map.map)
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
        elif eevee.state != eevee.CLEAR:
            eevee.handle_event(event, frame_time)


def update(frame_time):
    down_background.update(frame_time)
    up_background.update(frame_time)
    down_grass.update(frame_time)
    up_grass.update(frame_time)
    map.update(frame_time)
    if(eevee.update(frame_time)):
        GameFrameWork.push_state(ClearState)
        up_background.music.stop()

    for data in map.map:
        data.update(frame_time)
        if eevee.skill.on == 1 and collision.collide(eevee.skill, data):
            if data.object_TYPE == "MONSTER":
                if data.state == data.ALIVE:
                    data.hit()
        if collision.collide(eevee, data):
            if data.object_TYPE == "ITEM":
                if data.state == data.NONE:
                    eevee.get_item(data.type)
                    data.get()
            if data.object_TYPE == "MONSTER":
                if data.state == data.ALIVE:
                    if eevee.state == eevee.ATTACK:
                        data.hit()
                    elif eevee.hit():
                        GameFrameWork.push_state(GameOverState)
                        up_background.music.stop()

    if eevee.skill.on == 1 and collision.collide(eevee.skill, boss):
        if (boss.hit()):
            eevee.state = eevee.CLEAR
            up_background.music.stop()
            eevee.time = 0

    if collision.collide(eevee, boss):
        if eevee.state == eevee.ATTACK and boss.state != boss.ATTACK2:
            if(boss.hit()):
                eevee.state = eevee.CLEAR
                up_background.music.stop()
                eevee.time = 0
        elif boss.state not in (boss.HIT, boss.DIE):
            if eevee.hit():
                GameFrameWork.push_state(GameOverState)
                up_background.music.stop()

    if boss.state == boss.ATTACK3:
        for attack in boss.attack3:
            if collision.collide(eevee.skill, attack):
                attack.hit()
            if collision.collide(eevee, attack):
                if eevee.state != eevee.ATTACK:
                    if eevee.hit():
                        GameFrameWork.push_state(GameOverState)
                        up_background.music.stop()
                else:
                    attack.hit()

    if eevee.item_num[eevee.KEY] == 1:
        if animation.open_door(frame_time):
            eevee.item_num[eevee.KEY] = 2
    if eevee.item_num[eevee.KEY] != 0:
        boss.update(frame_time)


def drawObject(frame_time):
    up_background.draw()
    up_grass.draw()
    down_background.draw()
    down_grass.draw()
    map.draw()
    #map보다 object
    boss.draw()
    eevee.draw()
    ui.draw()

    if (eevee.item_num[eevee.KEY] != 2):
        animation.draw_door()

def draw(frame_time):
    clear_canvas()

    drawObject(frame_time)

    update_canvas()


def pause():
    pass


def resume():
    pass
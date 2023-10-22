from gameobject import GameObjectManager
from renderer import Renderer
from display import Display
from utils import log
import time


params : dict[str: int] = dict()


def set_params():
    file = open("../Prefs/Prefs.txt", "r")
    lines = file.readlines()

    global params

    for line in lines:
        name, value = line.split(":")
        params[name] = int(value)


def initialize_components():
    width, height = params["width"], params["height"]

    Display.initialize(width, height)
    GameObjectManager.initialize()


def main_loop():
    tickrate = params["tickrate"]
    ticktime = 1/tickrate

    while True:
        init_time = time.time()

        GameObjectManager.update()
        Renderer.update()
        Display.update_display()

        dtime = time.time() - init_time
        if ticktime > dtime :
            time.sleep(ticktime - dtime)


def initialize_engine():
    set_params()
    initialize_components()


if __name__ == "__main__":
    initialize_engine()

    main_loop()

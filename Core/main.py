from gameobject import GameObjectManager, GameObject
from renderer import Renderer, Sprite
from display import Display
from utils import log
import time


params : dict[str: int] = None


def set_params():
    file = open("../Prefs/Prefs.txt", "r")
    width, height, tickrate = file.readlines()

    global params
    params = {"width": int(width),
              "height": int(height),
              "tickrate": int(tickrate)}


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
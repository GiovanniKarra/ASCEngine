from .gameobject import GameObjectManager
from .renderer import Renderer
from .display import Display
#from ui import UIManager
from .prefs import Prefs
from .input import Input
from .utils import log
import time


def initialize_components():
    width, height = Prefs.get_param("width"), Prefs.get_param("height")

    Display.initialize(width, height)
    GameObjectManager.initialize()
    #UIManager.initialize()
    Input.initialize()


def main_loop():
    tickrate = Prefs.get_param("tickrate")
    ticktime = 1/tickrate

    while True:
        init_time = time.time()

        #UIManager.update()
        GameObjectManager.update()
        Renderer.update()
        Display.update()
        Input.update()

        dtime = time.time() - init_time
        if ticktime > dtime :
            time.sleep(ticktime - dtime)


def initialize_engine():
    Prefs.set_params()
    initialize_components()


if __name__ == "__main__":
    initialize_engine()

    main_loop()

from gameobject import GameObjectManager
from renderer import Renderer, Sprite
from display import Display
import time


params : dict[str : int] = None


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

        Display.update_display()
        GameObjectManager.update()
        Renderer.update()

        dtime = time.time() - init_time
        if ticktime > dtime :
            time.sleep(ticktime - dtime)


def initialize_engine():
    set_params()
    initialize_components()


def test():
    sprite1 : Sprite = Renderer.create_sprite_from_string("000\n"\
                                                          "000")
    
    sprite2 : Sprite = Renderer.create_sprite_from_string("§0§\n"\
                                                          "000")
    
    Renderer.draw_sprite(sprite1, (2, 5))
    Renderer.draw_sprite(sprite2, (30, 0))


if __name__ == "__main__":
    initialize_engine()

    test()

    main_loop()
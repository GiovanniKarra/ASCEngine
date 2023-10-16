from gameobject import GameObjectManager
from display import Display


def get_params():
    file = open("C:/Users/super/CodeProjects/ASCEngine/Prefs/Prefs.txt", "r")
    width, height = file.readlines()

    return int(width), int(height)


def initialize_components():
    width, height = get_params()

    Display.initialize(width, height)
    GameObjectManager.initialize()


if __name__ == "__main__":
    initialize_components()
    
    Display.update_display()
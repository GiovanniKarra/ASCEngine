import os
from .utils import log

class Display:

    _width : int
    _height : int
    _screen : list[list[str]]


    @staticmethod
    def initialize(width : int, height : int):
        Display._width = width
        Display._height = height

        Display._screen = [[" " for _ in range(width)] for _ in range(height)]


    @staticmethod
    def update() -> None:
        Display.clear()
        rows = ["".join(r) for r in Display._screen]
        print("\n".join(rows))
        
        Display._screen = [[" " for _ in range(Display._width)] for _ in range(Display._height)]


    @staticmethod
    def set_pixels(value : str, screen_position : (int, int)) -> None:
        x, y = screen_position
        
        if value == "" or value == "§" or x >= Display._width or y >= Display._height:
            return

        Display._screen[y][x] = value


    @staticmethod
    def get_size() -> (int, int):
        return Display._width, Display._height


    @staticmethod
    def clear() -> None:
        os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    Display.initialize(50, 10)
    from time import sleep
    for i in range(30):
        Display.set_pixels("#", (5+i, 5))
        Display.update()
        sleep(0.05)
        
    input()

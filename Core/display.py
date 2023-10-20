import os
from utils import log

class Display:

    _width : int
    _height : int
    _screen : list[list[str]]


    @classmethod
    def initialize(cls, width : int, height : int):
        cls._width = width
        cls._height = height

        cls._screen = [[" " for _ in range(width)] for _ in range(height)]


    @classmethod
    def update_display(cls) -> None:
        cls.clear()
        rows = ["".join(r) for r in cls._screen]
        print("\n".join(rows))


    @classmethod
    def set_pixels(cls, value : str, screen_position : (int, int)) -> None:
        if value == "" or value == "§":
            return

        log(f"pixel draw : {value}")
        x, y = screen_position
        cls._screen[y][x] = value


    @classmethod
    def get_size(cls) -> (int, int):
        return cls._width, cls._height


    @classmethod
    def clear(cls) -> None:
        os.system("clear")


if __name__ == "__main__":
    Display.initialize(50, 10)
    from time import sleep
    for i in range(30):
        Display.set_pixels("#", (5+i, 5))
        Display.update_display()
        sleep(0.05)
        
    input()

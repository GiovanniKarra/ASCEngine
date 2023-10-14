import os

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
    def set_pixels(cls, value : str, x : int, y : int) -> None:
        cls._screen[y][x] = value


    @classmethod
    def clear(cls) -> None:
        os.system("cls")


if __name__ == "__main__":
    Display.initialize(50, 10)
    from time import sleep
    for i in range(30):
        Display.set_pixels("#", 5+i, 5)
        Display.update_display()
        sleep(0.05)
        
    input()

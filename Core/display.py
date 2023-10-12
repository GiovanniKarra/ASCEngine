import os

class Display:

    _width : int
    _height : int
    _screen : list[list[str]]


    @classmethod
    def initialize(cls, width : int, height : int):
        cls._width : int = width
        cls._height : int = height

        cls._screen : list[list[str]] = [["." for _ in range(width)] for _ in range(height)]


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
    Display.set_pixels("#", 5, 5)
    Display.update_display()
    input()
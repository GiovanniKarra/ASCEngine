import os

class display:

    def __init__(self, width, height):
        self._width : int = width
        self._height : int = height

        self._screen : list[list[str]] = [["."] * width] * height


    def update_display(self):
        self.clear()
        rows = ["".join(r) for r in self._screen]
        print("\n".join(rows))


    def set_pixels(self, value : str, x : int, y : int):
        self._screen[y][x] = value


    def clear(self):
        os.system("cls")


if __name__ == "__main__":
    my_display = display(20, 10)
    my_display.set_pixels("#", 5, 5)
    my_display.update_display()
    input()
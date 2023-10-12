import os

class Display:

    def __init__(self, width : int, height : int):
        self._width : int = width
        self._height : int = height

        self._screen : list[list[str]] = [["." for _ in range(width)] for _ in range(height)]


    def update_display(self) -> None:
        self.clear()
        rows = ["".join(r) for r in self._screen]
        print("\n".join(rows))


    def set_pixels(self, value : str, x : int, y : int) -> None:
        self._screen[y][x] = value


    def clear(self) -> None:
        os.system("cls")


if __name__ == "__main__":
    my_display = Display(20, 10)
    my_display.set_pixels("#", 5, 5)
    my_display.update_display()
    input()
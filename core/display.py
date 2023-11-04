import os
from consoledraw import Console


console = Console()


class Display:
    """Class that controls the display"""

    _width : int
    _height : int
    _screen : list[list[str]]


    @staticmethod
    def initialize(width : int, height : int):
        """Initialize the display with a given width and height"""
        Display._width = width
        Display._height = height

        Display._screen = [[" " for _ in range(width)] for _ in range(height)]


    @staticmethod
    def update() -> None:
        """Update the display"""
        #Display.clear()
        console.clear()
        rows = ["".join(r) for r in Display._screen]
        console.print("\n".join(rows))
        console.update()
        
        Display._screen = [[" " for _ in range(Display._width)] for _ in range(Display._height)]


    @staticmethod
    def set_pixels(value : str, screen_position : (int, int)) -> None:
        """Set the pixel at screen_position to value"""
        x, y = screen_position
        
        if value == "" or value == "§" or x >= Display._width or y >= Display._height:
            return

        Display._screen[y][x] = value


    @staticmethod
    def get_size() -> (int, int):
        """Returns the width and height of the display"""
        return Display._width, Display._height


    @staticmethod
    def clear() -> None:
        """Clears the display"""
        os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    Display.initialize(50, 10)
    from time import sleep
    for i in range(30):
        Display.set_pixels("#", (5+i, 5))
        Display.update()
        sleep(0.05)
        
    input()

from dataclasses import dataclass


class SPRITE_TYPE:
    BACKGROUND = 0
    GAMEOBJECT = 1
    UI = 2


class COLOR:
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    YELLOW = "yellow"
    BLACK = "black"
    MAGENTA = "magenta"
    CYAN = "cyan"
    WHITE = "white"
    LIGHT_GREY = "light_grey"
    DARK_GREY = "dark_grey"
    LIGHT_RED = "light_red"
    LIGHT_GREEN = "light_green"
    LIGHT_YELLOW = "light_yellow"
    LIGHT_BLUE = "light_blue"
    LIGHT_MAGENTA = "light_magenta"
    LIGHT_CYAN = "light_cyan"

    BOLD = "bold"
    DARK = "dark"
    UNDERLINE = "underline"
    BLINK = "blink"
    REVERSE = "reverse"
    CONCEALED = "concealed"

    BACKGROUND_COLOR = "on_"


Color = str
CharMatrix = list[list[str]]


class Sprite:
    """a class representing sprites"""

    def __init__(self, sprite : CharMatrix, color : Color, layer : int, type : int) -> None:
        self.sprite : CharMatrix = sprite
        self.color : Color = color
        self.layer : int = layer
        self.type : int = type

    @staticmethod
    def create_sprite_from_string(
        string : str, color : Color = COLOR.WHITE,
        layer : int = 0, type : int = SPRITE_TYPE.GAMEOBJECT) -> "Sprite":
        """Returns a sprite type from a string"""

        lines : list[str] = string.split("\n")
        sprite : list[list[str]] = [list(lines[i]) for i in range(len(lines))]

        return Sprite(sprite, color, layer, type)
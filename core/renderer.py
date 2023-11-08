from dataclasses import dataclass

from termcolor import colored

from .display import Display
from .utils import log
from .prefs import Prefs


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

@dataclass
class Sprite:
    """Dataclass representing sprites"""
    sprite : CharMatrix
    color : Color
    layer : int
    type : int


class Renderer:

    _torender : dict[int: dict[int: list[(Sprite, int, int)]]] = {
        SPRITE_TYPE.BACKGROUND : dict(),
        SPRITE_TYPE.GAMEOBJECT : dict(),
        SPRITE_TYPE.UI : dict()
    }

    @staticmethod
    def create_sprite_from_string(
        string : str, layer : int = 0, type : int = SPRITE_TYPE.GAMEOBJECT) -> Sprite:
        """Returns a sprite type from a string"""

        lines : list[str] = string.split("\n")
        sprite : list[list[str]] = [list(lines[i]) for i in range(len(lines))]

        return Sprite(sprite, layer, type)
    

    @staticmethod
    def draw_sprite(sprite : Sprite, position : (int, int)) -> None:
        """Draws sprite at position"""
        x, y = position
        
        if sprite.layer not in Renderer._torender[sprite.type]:
            Renderer._torender[sprite.type][sprite.layer] = []
        
        Renderer._torender[sprite.type][sprite.layer].append((sprite, x, y))

    
    @staticmethod
    def update() -> None:
        for i in sorted(Renderer._torender):
            for j in sorted(Renderer._torender[i]):
                for sprite, x, y in Renderer._torender[i][j]:
                    Renderer.render(sprite.sprite, (x, y))

        Renderer._torender = {
            SPRITE_TYPE.BACKGROUND : dict(),
            SPRITE_TYPE.GAMEOBJECT : dict(),
            SPRITE_TYPE.UI : dict()
        }


    @staticmethod
    def render(sprite : list[list[str]], position : (int, int)) -> None:
        """DON'T USE"""
        x, y = position

        for i in range(len(sprite)):
            for j in range(len(sprite[i])):
                if x+j >= 0 and x+j < Prefs.get_param("width")\
                        and y+i >= 0 and y+i < Prefs.get_param("height"):
                    
                    Display.set_pixels(sprite[i][j], (x+j, y+i))
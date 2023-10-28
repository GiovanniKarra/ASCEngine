from dataclasses import dataclass
from display import Display
from utils import log
from enum import Enum


BACKGROUND = 0
GAMEOBJECT = 1
UI = 2


@dataclass
class Sprite:
    sprite : list[list[str]]
    layer : int
    type : int = GAMEOBJECT


class Renderer:

    _torender : dict[int: dict[int: list[(Sprite, int, int)]]] = {
        BACKGROUND : dict(),
        GAMEOBJECT : dict(),
        UI : dict()
    }

    @staticmethod
    def create_sprite_from_string(string : str, layer : int = 0) -> Sprite:
        lines : list[str] = string.split("\n")
        sprite : list[list[str]] = [list(lines[i]) for i in range(len(lines))]

        return Sprite(sprite, layer)
    

    @classmethod
    def draw_sprite(cls, sprite : Sprite, position : (int, int)) -> None:
        x, y = position
        
        if sprite.layer not in cls._torender[sprite.type]:
            cls._torender[sprite.type][sprite.layer] = []
        
        cls._torender[sprite.type][sprite.layer].append((sprite, x, y))

    
    @classmethod
    def update(cls) -> None:
        for i in sorted(cls._torender):
            for j in sorted(cls._torender[i]):
                for sprite, x, y in cls._torender[i][j]:
                    cls.render(sprite.sprite, (x, y))

        cls._torender = {
            BACKGROUND : dict(),
            GAMEOBJECT : dict(),
            UI : dict()
        }


    @staticmethod
    def render(sprite : list[list[str]], position : (int, int)) -> None:
        x, y = position

        for i in range(len(sprite)):
            for j in range(len(sprite[i])):
                Display.set_pixels(sprite[i][j], (x+j, y+i))
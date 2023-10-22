from dataclasses import dataclass
from display import Display
from utils import log

@dataclass
class Sprite:
    sprite : list[list[str]]
    layer : int


class Renderer:

    _torender : dict[int: list[(Sprite, int, int)]] = dict()

    @staticmethod
    def create_sprite_from_string(string : str, layer : int = 0) -> Sprite:
        lines : list[str] = string.split("\n")
        sprite : list[list[str]] = [list(lines[i]) for i in range(len(lines))]

        return Sprite(sprite, layer)
    

    @classmethod
    def draw_sprite(cls, sprite : Sprite, position : (int, int)) -> None:
        x, y = position
        width, height = Display.get_size()

        if x >= width or y >= height:
            return
        
        if sprite.layer not in cls._torender:
            cls._torender[sprite.layer] = []
        
        cls._torender[sprite.layer].append((sprite, x, y))

    
    @classmethod
    def update(cls) -> None:
        for i in sorted(cls._torender):
            for sprite, x, y in cls._torender[i]:
                cls.render(sprite.sprite, (x, y))

        cls._torender = dict()


    @staticmethod
    def render(sprite : list[list[str]], position : (int, int)) -> None:
        x, y = position

        for i in range(len(sprite)):
            for j in range(len(sprite[i])):
                Display.set_pixels(sprite[i][j], (x+j, y+i))
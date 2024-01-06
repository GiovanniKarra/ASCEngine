from .display import Display
from .utils import log
from .prefs import Prefs
from .sprite import Sprite, SPRITE_TYPE, CharMatrix


class Renderer:

    _torender : dict[int, dict[int, list[tuple[Sprite, int, int]]]] = {
        SPRITE_TYPE.BACKGROUND : dict(),
        SPRITE_TYPE.GAMEOBJECT : dict(),
        SPRITE_TYPE.UI : dict()
    }
    

    @staticmethod
    def draw_sprite(sprite : Sprite, position : tuple[int, int]) -> None:
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
                    Renderer.render(sprite, (x, y))

        Renderer._torender = {
            SPRITE_TYPE.BACKGROUND : dict(),
            SPRITE_TYPE.GAMEOBJECT : dict(),
            SPRITE_TYPE.UI : dict()
        }


    @staticmethod
    def render(sprite : Sprite, position : tuple[int, int]) -> None:
        """DON'T USE"""
        x, y = position
        char_matrix : CharMatrix = sprite.sprite
        
        width = int(Prefs.get_param("width"))
        height = int(Prefs.get_param("height"))

        for i in range(len(char_matrix)):
            for j in range(len(char_matrix[i])):
                if x+j >= 0 and x+j < width\
                        and y+i >= 0 and y+i < height:
                    
                    Display.set_pixels(char_matrix[i][j], (x+j, y+i))


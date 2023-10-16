from dataclasses import dataclass

@dataclass
class Sprite:
    sprite : list[list[str]]
    layer : int


class Renderer:

    @staticmethod
    def create_sprite_from_string(string : str, layer : int = 0) -> Sprite:
        lines : list[str] = string.split("\n")
        sprite : list[list[str]] = [lines[i].split for i in range(len(lines))]

        return Sprite(sprite, layer)
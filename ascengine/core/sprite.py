from .utils import log

class SPRITE_TYPE:
    BACKGROUND = 0
    GAMEOBJECT = 1
    UI = 2


def colored(text : str, color : int, *parameters : int):
    """
    Returns the colored text.
    The colors and various parameters can be found in the COLOR class
    """

    lines = text.split("\n")
    to_return =\
        ["".join([f"\033[{color}{''.join(f';{param}' for param in parameters)}m"\
         f"{char}" for char in line])\
         + "\033[0m" for line in lines]
    
    return "\n".join(to_return)


class COLOR:

    RESET = 0

    # Colors
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37

    # Attributes
    BOLD = 1
    UNDERLINE = 4

    # Special
    BG = 10 # must be added to the color


CharMatrix = list[list[str]]


class Sprite:
    """a class representing sprites"""

    def __init__(self, sprite : CharMatrix | str, layer : int = 0,
                 type : int = SPRITE_TYPE.GAMEOBJECT) -> None:
        if isinstance(sprite, str):
            sprite = Sprite._separate_characters(sprite)
        self.sprite : CharMatrix = sprite
        self.layer : int = layer
        self.type : int = type


    @staticmethod
    def create_sprite_from_string(
        string : str, layer : int = 0, type : int = SPRITE_TYPE.GAMEOBJECT) -> "Sprite":
        """Returns a sprite type from a string"""

        sprite : CharMatrix = Sprite._separate_characters(string)
        log(sprite)

        return Sprite(sprite, layer, type)
    

    @staticmethod
    def _separate_characters(string : str) -> CharMatrix:
        lines : list[str] = string.split("\n")
        char_matrix = []

        for line in lines:
            pre_process_line = [""]
            post_process_line = []
            char_matrix.append(post_process_line)

            color_mode = False
            for char in line:
                if char == "\x1b":
                    color_mode = True

                pre_process_line[-1] += char

                if color_mode:
                    if char == "m":
                        color_mode = False
                    else:
                        continue

                pre_process_line.append("")
            
            if pre_process_line[-1] == "":
                pre_process_line.pop()

            i = 0
            while i < len(pre_process_line):
                to_append = pre_process_line[i]
                if "\x1b" in to_append:
                    if i == len(pre_process_line)-1:
                        post_process_line[-1] += to_append
                        break
                    else:
                        i += 1
                        to_append += pre_process_line[i]
                
                post_process_line.append(to_append)
                i += 1


        return char_matrix
                
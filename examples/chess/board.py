from ascengine.core import *

class Board(GameObject):
    def __init__(self):
        sprite_str : str = "\n".join([item for pair in
                            zip([((colored("  ", COLOR.BLUE + COLOR.BG)
                            + colored("  ", COLOR.WHITE + COLOR.BG)) * 4)
                            for _ in range(4)],
                            [((colored("  ", COLOR.WHITE + COLOR.BG)
                            + colored("  ", COLOR.BLUE + COLOR.BG)) * 4)
                            for _ in range(4)]) for item in pair])
        
        sprite_str: str = "{BG;BLUE}  {BG;WHITE}  "*4 + "\n" + "{BG;WHITE}  {BG;BLUE}  "*4
        sprite_str = "\n".join([sprite_str for _ in range(4)])
        log(sprite_str)

        
        sprite : Sprite = Sprite(sprite_str)
        super().__init__(0, 0, sprite)
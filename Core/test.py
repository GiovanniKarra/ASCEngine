from renderer import *
from gameobject import *
from main import *
from display import *
from utils import *



if __name__ == "__main__":
    initialize_engine()

    sprite1 : Sprite = Renderer.create_sprite_from_string("000\n"\
                                                          "000")
    
    sprite2 : Sprite = Renderer.create_sprite_from_string("§X§\n"\
                                                          "XXX", 1)

    class G(GameObject):
        def __init__(self):
            super().__init__()
            self.set_sprite(sprite1)
            self.set_position(2, 5)
            self.delta = 0

        def update(self) -> None:
            super().update()
            x, y = self.get_position()
            self.set_position(x+int(not self.delta%10), y)

    class F(GameObject):
        def __init__(self):
            super().__init__()
            self.set_sprite(sprite2)
            self.set_position(60, 0)

        def update(self) -> None:
            super().update()
            x, y = self.get_position()
            offset_x = int(not self.delta%10)
            offset_y = int(not self.delta%60)
            self.set_position(x-offset_x, y+offset_y)

    g = G()
    f = F()

    main_loop()

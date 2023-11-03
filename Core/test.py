from renderer import *
from gameobject import *
from main import *
from display import *
from utils import *
from ui import *
from input import *



if __name__ == "__main__":
    initialize_engine()

    sprite1 : Sprite = Renderer.create_sprite_from_string("000\n"\
                                                          "000")
    
    sprite2 : Sprite = Renderer.create_sprite_from_string("§X§\n"\
                                                          "XXX", 0)

    ui_sprite : Sprite = Renderer.create_sprite_from_string("Ceci est du texte")

    class G(GameObject):
        def __init__(self):
            super().__init__()
            self.set_sprite(sprite1)
            self.set_position(2, 5)
            self.tickcount = 0

        def update(self) -> None:
            super().update()
            x, y = self.get_position()
            dx = int(Input.keypressed(Key.right)) - int(Input.keypressed(Key.left))
            dy = int(Input.keypressed(Key.down)) - int(Input.keypressed(Key.up))
            self.set_position(x+dx, y+dy)


    g = G()

    main_loop()

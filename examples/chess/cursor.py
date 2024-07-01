from ascengine.core import *

class Cursor(GameObject):
    def __init__(self):
        sprite : Sprite = Sprite("X", 1)
        self.last_move = 0
        super().__init__(0, 0, sprite)

    def update(self) -> None:
        dx, dy = 0, 0
        if Input.keypressed(Key.left): dx -= 1
        if Input.keypressed(Key.right): dx += 1
        if Input.keypressed(Key.up): dy -= 1
        if Input.keypressed(Key.down): dy += 1

        if dx != 0 or dy != 0:
            self.get_sprite().layer = 1
            self.last_move = self.tickcount
        
        if self.last_move + 30 < self.tickcount:
            self.get_sprite().layer = 1 - 20 * (self.tickcount%46 > 23)

        x, y = self.get_position()
        self.set_position(x+dx, y+dy)

        super().update()
from ascengine.core import *


if __name__ == "__main__":
	initialize_engine()

	sprite1 : Sprite = Sprite(colored("000\n"\
									  "000", COLOR.RED, COLOR.BOLD))
	
	sprite2 : Sprite = Sprite(colored("X\n"\
											"XXX", COLOR.BLUE, COLOR.BOLD, COLOR.UNDERLINE))

	log (sprite2.sprite)

	ui_sprite : Sprite = Sprite("Ceci est du texte")

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

	class F(GameObject):
		def __init__(self):
			super().__init__()
			self.set_sprite(sprite2)
			self.set_position(2, 5)
			self.tickcount = 0

		def update(self) -> None:
			super().update()
			x, y = self.get_position()
			dx = int(Input.keypressed("d")) - int(Input.keypressed("q"))
			dy = int(Input.keypressed("s")) - int(Input.keypressed("z"))
			self.set_position(x+dx, y+dy)


	g = G()
	f = F()
	uielem = UIElement()
	uielem.set_position(5, 0)
	uielem.set_sprite(ui_sprite)
	main_loop()

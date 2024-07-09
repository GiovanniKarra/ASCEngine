from ascengine.core import *

class Cursor(GameObject):
	def __init__(self):
		sprite : Sprite = Sprite("{BOLD;MAGENTA}X", 1)
		self.last_move = 0
		super().__init__(0, 0, sprite)

		self.click_actions: list[function[int, int]] = []

	def update(self) -> None:

		dx = int(Input.keypressed(Key.right)) - int(Input.keypressed(Key.left))
		dy = int(Input.keypressed(Key.down)) - int(Input.keypressed(Key.up))

		if dx != 0 or dy != 0:
			self.get_sprite().layer = 1
			self.last_move = self.tickcount

		tickrate = int(Prefs.get_param("tickrate"))
		if self.last_move + tickrate < self.tickcount:
			self.get_sprite().layer = 1 - 20 * (self.tickcount%(tickrate*2*0.7) > 0.7*tickrate)

		x, y = self.get_position()
		self.set_position(x+dx, y+dy)

		if Input.keypressed("c"): self.click()

		super().update()


	def click(self) -> None:
		for action in self.click_actions:
			x, y = self.get_position()
			action(x, y)

	
	def add_action(self, func) -> None:
		self.click_actions.append(func)
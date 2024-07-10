from ascengine.core import *
from ascengine.core.renderer import Sprite

from boardobject import BoardObject
from cursor import Cursor


class Tracker(GameObject):
	def __init__(self, track: GameObject):
		self.track = track
		super().__init__(0, 9, Sprite(f"{track.get_position()}"))

	def update(self) -> None:
		super().update()
		self.set_sprite(Sprite(f"{self.track.get_position()}"))


if __name__ == "__main__":
	Prefs.set_param("width", 25)
	Prefs.set_param("height", 10)
	Prefs.set_param("tickrate", 30)

	initialize_engine()

	board = BoardObject()
	cursor = Cursor()

	cursor.add_action(board.select)

	# debug = Tracker(cursor)

	main_loop()
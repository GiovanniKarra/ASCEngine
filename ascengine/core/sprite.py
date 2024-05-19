from .utils import log

class SPRITE_TYPE:
	BACKGROUND = 0
	GAMEOBJECT = 1
	UI = 2


def colored(text : str, color : int, *parameters : int) -> str:
	"""
	Returns the colored text.
	The colors and various parameters can be found in the COLOR class
	"""

	lines = text.split("\n")
	to_return =\
		["".join([f"\033[{color}{''.join(f';{param}' for param in parameters)}m"\
		 f"{char}" + "\033[0m" for char in line])\
		 for line in lines]
	
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

	def __init__(self, sprite : CharMatrix | str = [[""]], layer : int = 0,
				 type : int = SPRITE_TYPE.GAMEOBJECT) -> None:
		if isinstance(sprite, str):
			# if sprite[0] != "\x1b": sprite = f"\033[0m{sprite}\033[0m"

			sprite = Sprite._separate_characters(sprite)

		self.sprite : CharMatrix = sprite
		self.layer : int = layer
		self.type : int = type


	@staticmethod
	def create_sprite_from_string(
		string : str, layer : int = 0, type : int = SPRITE_TYPE.GAMEOBJECT) -> "Sprite":
		"""Returns a sprite type from a string"""

		sprite : CharMatrix = Sprite._separate_characters(string)

		return Sprite(sprite, layer, type)
	

	@staticmethod
	def _separate_characters(string : str) -> CharMatrix:
		new_string = string

		lines : list[str] = new_string.split("\n")
		while lines[0] == "": lines.pop(0)
		while lines[-1] == "": lines.pop()

		char_matrix = [line.split("\033[0m") for line in lines]

		char_matrix = [[char + "\033[0m" for char in line if char != ""]
					   for line in char_matrix]

		return char_matrix

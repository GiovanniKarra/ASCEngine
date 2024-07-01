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
	BG = 10  # must be added to the color

	string_to_id: dict[str, tuple[int]] = {
		"BLACK": (BLACK,),
		"RED": (RED,),
		"GREEN": (GREEN,),
		"YELLOW": (YELLOW,),
		"BLUE": (BLUE,),
		"MAGENTA": (MAGENTA,),
		"CYAN": (CYAN,),
		"WHITE": (WHITE,),
		
		"BOLD": (BOLD,),
		"UNDERLINE": (UNDERLINE,)
	}


CharMatrix = list[list[str]]


class Sprite:
	"""a class representing sprites"""

	def __init__(self, sprite : str = "", layer : int = 0,
				 type : int = SPRITE_TYPE.GAMEOBJECT) -> None:

		self.characters, self.attributes, self.background =\
												self._parse_string(sprite)
		self.layer : int = layer
		self.type : int = type


	def _parse_string(self, string: str):
		characters: list[list[str]] = [[]]
		attributes: list[list[list[int]]] = [[]]
		background: list[list[list[int]]] = [[]]

		current_attributes = [COLOR.RESET]
		current_background = [COLOR.RESET]

		escape = False
		bracket_mode = False
		cumulative_characters = []
		background_mode = False
		
		i = 0
		for char in string:
			if escape:
				characters[i].append(char)
				attributes[i].append(current_attributes.copy())
				background[i].append(current_background.copy())
				escape = False
			elif bracket_mode:
				if char in ("}", ",", ";"):
					bracket_mode = char != "}"
					attribute_string = "".join(cumulative_characters)
					cumulative_characters = []

					attribute = tuple()
					try:
						if attribute_string == "BG":
							current_background = []
							background_mode = True
						elif attribute_string == "FG":
							background_mode = False
						elif attribute_string.isnumeric():
							attribute = (int(attribute_string),)
						else:
							attribute = COLOR.string_to_id[attribute_string]
					except:
						attribute = (COLOR.RESET,)

					for att in attribute:
						if background_mode:
							current_background.append(att)
						elif att == COLOR.RESET:
							current_attributes = []
						else:
							current_attributes.append(att)

				else:
					cumulative_characters.append(char.upper())
			else:
				if char == "\n":
					i += 1
					characters.append([])
					attributes.append([])
					background.append([])
				elif char == "\\":
					escape = True
				elif char == "{":
					bracket_mode = True
				else:
					characters[i].append(char)
					background[i].append(current_background.copy())
					attributes[i].append(current_attributes.copy())

		return (characters, attributes, background)

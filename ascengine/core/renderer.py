from .display import Display
from .utils import log
from .prefs import Prefs
from .sprite import Sprite, SPRITE_TYPE, CharMatrix, COLOR


class Renderer:

	_torender: dict[int, dict[int, list[tuple[Sprite, int, int]]]] = {
		SPRITE_TYPE.BACKGROUND : dict(),
		SPRITE_TYPE.GAMEOBJECT : dict(),
		SPRITE_TYPE.UI : dict()
	}

	_characters: list[list[str]] = None
	_attributes: list[list[list[int]]] = None
	_background: list[list[list[int]]] = None


	@staticmethod
	def draw_sprite(sprite : Sprite, position : tuple[int, int]) -> None:
		"""Draws sprite at position"""
		x, y = position
		
		if sprite.layer not in Renderer._torender[sprite.type]:
			Renderer._torender[sprite.type][sprite.layer] = []
		
		Renderer._torender[sprite.type][sprite.layer].append((sprite, x, y))

	
	@staticmethod
	def update() -> None:
		width, height = Display.get_size()

		Renderer._characters = [[" " for _ in range(width)] for _ in range(height)]
		Renderer._attributes = [[[] for _ in range(width)] for _ in range(height)]
		Renderer._background = [[[] for _ in range(width)] for _ in range(height)]

		for i in sorted(Renderer._torender):
			for j in sorted(Renderer._torender[i]):
				for sprite, x, y in Renderer._torender[i][j]:
					Renderer._render(sprite, (x, y))

		for i in range(height):
			for j in range(width):
				pixel = Renderer._sprite_attributes_to_string(
					Renderer._characters[i][j],
					Renderer._attributes[i][j],
					Renderer._background[i][j].copy()
				)
				Display.set_pixels(pixel, (x+j, y+i))

		Renderer._torender = {
			SPRITE_TYPE.BACKGROUND : dict(),
			SPRITE_TYPE.GAMEOBJECT : dict(),
			SPRITE_TYPE.UI : dict()
		}


	@staticmethod
	def _render(sprite : Sprite, position : tuple[int, int]) -> None:
		x, y = position
		characters: CharMatrix = sprite.characters
		attributes: list[list[list[int]]] = sprite.attributes
		background: list[list[list[int]]] = sprite.background
		
		width, height = Display.get_size()

		for i in range(len(characters)):
			for j in range(len(characters[i])):
				if x+j >= 0 and x+j < width\
						and y+i >= 0 and y+i < height:

					Renderer._characters[y+i][x+j] = characters[i][j]
					Renderer._attributes[y+i][x+j] = attributes[i][j]
					if len(background[i][j]) > 0 and COLOR.RESET not in background[i][j]:
						Renderer._background[y+i][x+j] = background[i][j]


	@staticmethod
	def _sprite_attributes_to_string(character: str,
								  		attributes: list[int], background: list[int]):
		if COLOR.RESET in background:
			background = []
		elif len(background) > 0:
			background[0] += 10

		ret = "\033[" +\
			";".join(map(str, [*attributes, *background])) +\
			"m" + character + "\033[0m"
		
		return ret

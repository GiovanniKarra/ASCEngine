from ascengine.core import *

from constants import *
from piece import Piece


class Board(GameObject):
	def __init__(self):
		sprite_str: str = "{BG;BLUE}  {BG;WHITE}  "*4 + "\n" + "{BG;WHITE}  {BG;BLUE}  "*4
		sprite_str = "\n".join([sprite_str for _ in range(4)])
		
		sprite : Sprite = Sprite(sprite_str)
		super().__init__(0, 0, sprite)

		self.spawn_pieces()


	def spawn_pieces(self):
		positioning = (
			(PIECE_TYPE.PAWN,)*8,
			(PIECE_TYPE.ROOK, PIECE_TYPE.KNIGHT, PIECE_TYPE.BISHOP,
			PIECE_TYPE.QUEEN, PIECE_TYPE.KING,
			PIECE_TYPE.BISHOP, PIECE_TYPE.KNIGHT, PIECE_TYPE.ROOK)
		)

		for i, row in enumerate(positioning):
			for j, type in enumerate(row):
				Piece(j*2, 1-i, type, PLAYERS.WHITE)
		
		for i, row in enumerate(positioning):
			for j, type in enumerate(row):
				Piece(j*2, 6+i, type, PLAYERS.BLACK)
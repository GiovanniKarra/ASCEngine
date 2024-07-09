from ascengine.core import *

from constants import *


class Piece(GameObject):

	def __init__(self, x: int = 0, y: int = 0,
			  type: int = PIECE_TYPE.PAWN, color: int = PLAYERS.WHITE):
		
		sprite = None
		self.move_type = None
		self.color = color
		
		match type:
			case PIECE_TYPE.PAWN:
				sprite = "p"
				self.move_type = (MOVE_TYPE.PAWN,)
			case PIECE_TYPE.ROOK:
				sprite = "R"
				self.move_type = (MOVE_TYPE.LINE,)
			case PIECE_TYPE.KNIGHT:
				sprite = "k"
				self.move_type = (MOVE_TYPE.L,)
			case PIECE_TYPE.BISHOP:
				sprite = "B"
				self.move_type = (MOVE_TYPE.DIAG,)
			case PIECE_TYPE.QUEEN:
				sprite = "Q"
				self.move_type = (MOVE_TYPE.DIAG, MOVE_TYPE.LINE)
			case PIECE_TYPE.KING:
				sprite = "K"
				self.move_type = (MOVE_TYPE.KING,)

		super().__init__(x, y,
				   Sprite("{BOLD;%s}%s" % ("YELLOW" if color == 0 else "RED", sprite)))
from ascengine.core import *

from constants import *
from piece import Piece
from board import Board


class BoardObject(GameObject):
	def __init__(self):
		sprite_str: str = "{BG;BLUE}  {BG;WHITE}  "*4 + "\n" + "{BG;WHITE}  {BG;BLUE}  "*4
		sprite_str = "\n".join([sprite_str for _ in range(4)])
		
		sprite: Sprite = Sprite(sprite_str, type=SPRITE_TYPE.BACKGROUND)
		super().__init__(0, 0, sprite)

		self.selection: Piece = None
		self.possible_moves: set[tuple[int, int]] = set()
		self.red_squares: list[GameObject] = []

		self.board = Board()

		self._update_pieces()


	def _update_pieces(self):
		for i, row in enumerate(self.board.board):
			for j, piece in enumerate(row):
				if piece is None: continue

				dx, dy = self.get_position()
				piece.set_position(2*j+dx, i+dy)


	def _display_selection(self):
		for square in self.red_squares:
			square.destroy()
		self.red_squares.clear()

		for i, j in self.possible_moves:
			x, y = self.get_position()
			square = GameObject(j*2+x, i+y, Sprite("{BG;RED}  "))
			self.red_squares.append(square)
	

	def select(self, x, y):
		xpos, ypos = self.get_position()
		i, j = y-ypos, (x-xpos)//2

		if self.selection is not None and (i, j) in self.possible_moves:
			k = self.selection.get_position()[1]-ypos
			l = (self.selection.get_position()[0]-xpos)//2
			self.board.move((k, l), (i, j))
			self._update_pieces()
			self.selection = None
			self.possible_moves = set()
			self._display_selection()
			return

		self.selection = self.board.board[i][j]
		self.possible_moves = self.board.legal_moves((i, j))
		self._display_selection()
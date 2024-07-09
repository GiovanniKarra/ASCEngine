from ascengine.core import *

from constants import *
from piece import Piece


class Board(GameObject):
	def __init__(self):
		sprite_str: str = "{BG;BLUE}  {BG;WHITE}  "*4 + "\n" + "{BG;WHITE}  {BG;BLUE}  "*4
		sprite_str = "\n".join([sprite_str for _ in range(4)])
		
		sprite: Sprite = Sprite(sprite_str, type=SPRITE_TYPE.BACKGROUND)
		super().__init__(0, 0, sprite)

		self.board: list[list[Piece]] = [[None for _ in range(8)] for _ in range(8)]
		self.selection: Piece = None
		self.possible_moves: set[tuple[int, int]] = set()
		self.red_squares: list[GameObject] = []

		self._spawn_pieces()
		self._place_pieces()


	def _spawn_pieces(self):
		positioning = (
			(PIECE_TYPE.PAWN,)*8,
			(PIECE_TYPE.ROOK, PIECE_TYPE.KNIGHT, PIECE_TYPE.BISHOP,
			PIECE_TYPE.QUEEN, PIECE_TYPE.KING,
			PIECE_TYPE.BISHOP, PIECE_TYPE.KNIGHT, PIECE_TYPE.ROOK)
		)

		for i, row in enumerate(positioning):
			for j, type in enumerate(row):
				p = Piece(j*2, 1-i, type, PLAYERS.WHITE)
				self.board[1-i][j] = p
		
		for i, row in enumerate(positioning):
			for j, type in enumerate(row):
				p = Piece(j*2, 6+i, type, PLAYERS.BLACK)
				self.board[6+i][j] = p
		
		self.board[4][4] = Piece(0, 0, PIECE_TYPE.QUEEN, PLAYERS.WHITE)


	def _place_pieces(self):
		for i, row in enumerate(self.board):
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
			# <move>
			return

		self.selection = self.board[i][j]
		self._generate_moves(self.selection, (i, j))
		self._display_selection()

	def _add_translate_move(self, i, j, iDir, jDir, color):
		di = 0; dj = 0
		while i+di >= 0 and i+di < 8 and j+dj >= 0 and j+dj < 8\
				and ((p := self.board[i+di][j+dj]) is None or\
					(p is not None and p.color != color) or (di, dj) == (0, 0)):
			if (di, dj) == (0, 0):
				di += iDir; dj += jDir
				continue

			self.possible_moves.add(
				(i+di, j+dj)
			)
			if p is not None: break

			di += iDir; dj += jDir

	def _generate_moves(self, piece: Piece, pos: tuple[int, int]):
		self.possible_moves = set()
		if piece is None: return

		i, j = pos

		if MOVE_TYPE.DIAG in piece.move_type:
			for iDir in (-1, 1):
				for jDir in (-1, 1):
					self._add_translate_move(i, j, iDir, jDir, piece.color)

		if MOVE_TYPE.LINE in piece.move_type:
			# for di in range(-7, 8):
			# 	self.possible_moves.add(
			# 		(min(max(0, i+di), 7), j)
			# 	)
			# 	self.possible_moves.add(
			# 		(i, (min(max(0, j+di), 7)))
			# 	)

			for iDir in (-1, 1):
				self._add_translate_move(i, j, iDir, 0, piece.color)
			for jDir in (-1, 1):
				self._add_translate_move(i, j, 0, jDir, piece.color)

		# self.possible_moves.remove((i, j))
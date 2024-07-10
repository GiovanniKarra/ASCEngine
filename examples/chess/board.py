from ascengine.core import *

from constants import *
from piece import Piece


class Board:
	def __init__(self):
		self.board: list[list[Piece]] = [[None for _ in range(8)] for _ in range(8)]

		self._initialize_board()


	def _initialize_board(self):
		positioning = (
			(PIECE_TYPE.PAWN,)*8,
			(PIECE_TYPE.ROOK, PIECE_TYPE.KNIGHT, PIECE_TYPE.BISHOP,
			PIECE_TYPE.QUEEN, PIECE_TYPE.KING,
			PIECE_TYPE.BISHOP, PIECE_TYPE.KNIGHT, PIECE_TYPE.ROOK)
		)

		for i, row in enumerate(positioning):
			for j, type in enumerate(row):
				p = Piece(0, 0, type, PLAYERS.WHITE)
				self.board[1-i][j] = p
		
		for i, row in enumerate(positioning):
			for j, type in enumerate(row):
				p = Piece(0, 0, type, PLAYERS.BLACK)
				self.board[6+i][j] = p
		
		self.board[4][4] = Piece(0, 0, PIECE_TYPE.QUEEN, PLAYERS.WHITE)


	def _add_translate_move(self, i, j, iDir, jDir, color):
		moves_set = set()
		di = 0; dj = 0
		while i+di >= 0 and i+di < 8 and j+dj >= 0 and j+dj < 8\
				and ((p := self.board[i+di][j+dj]) is None or\
					(p is not None and p.color != color) or (di, dj) == (0, 0)):
			if (di, dj) == (0, 0):
				di += iDir; dj += jDir
				continue

			moves_set.add(
				(i+di, j+dj)
			)
			if p is not None: break

			di += iDir; dj += jDir

		return moves_set


	def move(self, init_pos: tuple[int, int], dest_pos: tuple[int, int]):
		i, j = init_pos
		k, l = dest_pos
		if (p := self.board[k][l]) is not None:
			p.destroy()
		self.board[k][l] = self.board[i][j]
		self.board[i][j] = None


	def legal_moves(self, pos: tuple[int, int]):
		possible_moves = set()
		piece: Piece = self.board[pos[0]][pos[1]]
		if piece is None: return possible_moves

		i, j = pos

		if MOVE_TYPE.DIAG in piece.move_type:
			for iDir in (-1, 1):
				for jDir in (-1, 1):
					new_moves = self._add_translate_move(i, j, iDir, jDir, piece.color)
					possible_moves = possible_moves.union(new_moves)

		if MOVE_TYPE.LINE in piece.move_type:
			for iDir in (-1, 1):
				new_moves = self._add_translate_move(i, j, iDir, 0, piece.color)
				possible_moves = possible_moves.union(new_moves)
			for jDir in (-1, 1):
				new_moves = self._add_translate_move(i, j, 0, jDir, piece.color)
				possible_moves = possible_moves.union(new_moves)

		return possible_moves

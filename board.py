class Board:
	def __init__(self):
		self.board = [[0 for col in range(3)] for row in range(3)]
		self.board_score = 0

	def execute_turn(self, symbol, row, col):
		if self.board[row][col] == 0:
			if symbol == 'X':
				self.board[row][col] = 1
				return True
			elif symbol == 'O':
				self.board[row][col] = 2
				return True
			return False
		return False

	def reset(self):
		for row in range(3):
			for col in range(3):
				self.board[row][col] = 0

	def winner(self):
		for row in range(3):
			if self.board[row][0] == self.board[row][1] and self.board[row][1] == self.board[row][2] and self.board[row][0] != 0:
				return True

		for col in range(3):
			if self.board[0][col] == self.board[1][col] and self.board[1][col] == self.board[2][col] and self.board[0][col] != 0:
				return True

		if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != 0:
			return True

		if self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2] and self.board[2][0] != 0:
			return True

		return False

	def current_player(self):
		number_X = self.number_X(self.board)
		number_O = self.number_O(self.board)
		if (number_X + number_O)%2 == 0: #if number of total symbol is even its 'X's turn.Means 'X' starts the game
			return 'X'
		return 'O'						 #otherwise its 'O's turn

	def num_X(self, board):
		num_X = 0
		for row in range(3):
			for col in range(3):
				if self.board[row][col] == 1:
					num_X+=1
		return num_X

	def num_O(self, board):
		num_O = 0
		for row in range(3):
			for col in range(3):
				if self.board[row][col] == 2:
					num_O+=1
		return num_O

	def num_empty(self):
		empty_cells = 0
		for row in range(3):
			for col in range(3):
				if self.board[row][col] == 0:
					empty_cells+=1
		return empty_cells

	def possible_moves(self):
		possible_moves = []
		for row in range(3):
			for col in range(3):
				if self.board[row][col] == 0:
					possible_moves.append((row,col))
		return possible_moves

	def move(self, current_player, row, col):
		board_copy = [element[:] for element in self.board]
		if current_player == 'X':
			board_copy[row][col] = 1
		else:
			board_copy[row][col] = 2
		copy_board = Board()
		copy_board.board = board_copy
		return copy_board

	def calculate_board_score(self):
		for row in range(3):
			if self.board[row][0] == self.board[row][1] and self.board[row][1] == self.board[row][2] and self.board[row][0] != 0:
				if self.board[row][0] == 1:
					return 10
				elif self.board[row][0] == 2:
					return -10

		for col in range(3):
			if self.board[0][col] == self.board[1][col] and self.board[1][col] == self.board[2][col] and self.board[0][col] != 0:
				if self.board[0][col] == 1:
					return 10
				elif self.board[0][col] == 2:
					return -10

		if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != 0:
			if self.board[0][0] == 1:
				return 10
			elif self.board[0][0] == 2:
				return -10

		if self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2] and self.board[2][0] != 0:
			if self.board[2][0] == 1:
				return 10
			elif self.board[2][0] == 2:
				return -10

		return 0
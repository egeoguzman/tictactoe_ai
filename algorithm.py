from board import Board
import numpy as np

def minimizer(board):
	avrg_score = 0.0
	score = board.calculate_board_score()
	if score != 0 or board.num_empty() == 0:
		return score

	for poss_move in board.possible_moves():
		row , col = poss_move
		new_board = board.move('0' , row , col)
		score = maximizer(new_board)
		avrg_score = avrg_score + score
	return avrg_score/len(board.possible_moves())

def maximizer(board):
	highest_score = float('-inf')
	score = board.calculate_board_score()
	if score != 0 or board.num_empty() == 0:
		return score
	for poss_move in board.possible_moves():
		row , col = poss_move
		new_board = board.move('X' , row , col)
		score = minimizer(new_board)
		highest_score = max(highest_score,score)
	return highest_score 

def minimax(board,player):
	best_score = float('inf')
	best_move = None

	if player == 'X':
		best_score = float('-inf')
	for poss_move in board.possible_moves():
		row,col = poss_move
		new_board = board.move(player , row , col)
		if player == 'X':
			score = minimizer(new_board)
			if score > best_score:
				best_score = score
				best_move = (row,col)

		else:
			score = maximizer(new_board)
			if score < best_score:
				best_score = score
				best_move = (row,col)
	return best_move
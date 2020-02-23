Tic Tac Toe AI (Minimax Algorithm)

AI plays tic tac toe with minimax algorithm.

* Create the game:
board.py

- board:3x3
- player:'X' 
- opponent:'O'
- empty cell:' '
- tie:'TIE'
- 'X' = 1
- 'O' = 2
- ' ' = 0

- X wins => +10
- O wins => -10
- Tie => 0

execute_turn():
reset():resets the game
winner():decides the winner of the game according to moves
current_player():calculates the current player who will play next move
num_X():number of player's move
num_O():number of oppenent's move
num_empty():number of empty cells
possible_moves():shows the all possible moves in list of (row,column)
move():shows the moves on the board
calculate_board_score():calculates the player's scores to decide the winner



* Minimax Algorithm:
algorithm.py


- Minimize function
- Maximize function
- Minimax function

* Create Flask App to play game




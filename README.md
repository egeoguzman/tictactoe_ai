Tic Tac Toe AI (Minimax Algorithm)

AI plays tic tac toe with minimax algorithm.

<h3>*Create the game:board.py</h3>

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

<h4>Functions</h4>
<li> 
<ul>execute_turn():Takes in a symbol, a row number and column number, and executes the appropriate move on the current board object</ul>
<ul>reset():resets the game</ul>
<ul>winner():decides the winner of the game according to moves</ul>
<ul>current_player():calculates the current player who will play next move</ul>
<ul>num_X():number of player's move</ul>
<ul>num_O():number of oppenent's move</ul>
<ul>num_empty():number of empty cells</ul>
<ul>possible_moves():shows the all possible moves in list of (row,column)</ul>
<ul>move():shows the moves on the board</ul>
<ul>calculate_board_score():calculates the player's scores to decide the winner</ul>
</li>


<h3>*Minimax Algorithm:algorithm.py</h3>

- Minimize function
- Maximize function
- Minimax function
![lrXqH](https://user-images.githubusercontent.com/32989239/75119317-d4957500-5692-11ea-82f8-251c095efb9f.png)

<h3>*Create Flask App to play game:app.py</h3>
- Install the requirements (requirements.txt)
<br></br>
- Run the app.py




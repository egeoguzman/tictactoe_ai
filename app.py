from flask import Flask,session,request,redirect,render_template,url_for
from board import Board
import jsonpickle
from algorithm import minimax
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'the secret key'



board_current = Board()
human = 'X'
ai = 'O'
difficulty_level = None

@app.route('/')
def root():
	return render_template('side_selection.html')

@app.route('/side_selection', methods=['GET','POST'])
def side_selection():
	session['board_current'] = jsonpickle.encode(Board())
	if request.form['side'] == 'X':
			session['human'] = 'X'
			session['ai'] = 'O'

	else:
		session['human'] = 'O'
		session['ai'] = 'X'

	return redirect(url_for('index'))

@app.route('/index')
def index():
		board_current = jsonpickle.decode(session.get('board_current'))
		ai = session.get('ai')
		if session.get('ai') == 'X':
			ai_row,ai_col = ai_play()
			ai_result = board_current.execute_turn(ai,ai_row,ai_col)
		session['board_current'] = jsonpickle.encode(board_current)
		return render_template('index.html' , board=board_current.board)


@app.route('/turn', methods=['GET','POST'])
def turn():
	row = int(request.form['row'])
	col = int(request.form['col'])
	board_current = jsonpickle.decode(session.get('board_current'))
	ai = session.get('ai')
	human = session.get('human')

	if row >= 1 and row <=3 and col >= 1 and col <=3 and board_current.board[row-1][col-1] == 0:
		if not board_current.winner() and board_current.num_empty() > 0:
			result = board_current.execute_turn(human,row-1,col-1)

		session['board_current'] = jsonpickle.encode(board_current)
		board_current = jsonpickle.decode(session.get('board_current'))
		if not board_current.winner() and board_current.num_empty() > 0:
			ai_row,ai_col = ai_play()
			ai_result = board_current.execute_turn(ai,ai_row,ai_col)
	session['board_current'] = jsonpickle.encode(board_current)
	return render_template('index.html' , board=board_current.board)

def ai_play():
	board_current = jsonpickle.decode(session.get('board_current'))
	ai = session.get('ai')
	return minimax(board_current,ai)

if __name__ == '__main__':
    app.debug=True
    app.run()
from flask import render_template, request, redirect
from app import app
from app.models.game import *
from app.models.player import Player


@app.route('/')
def index():
    return render_template('index.html', title='Rock Paper Scissors')

@app.route('/play-game', methods=['POST'])
def play_game():
        name1 = request.form['name1']
        name2 = request.form['name2']
        choice1 = request.form['choice1']
        choice2 = request.form['choice2']
        player1 = Player(name1, choice1)
        player2 = Player(name2, choice2)
        winner = Game.get_the_winner(player1, player2)

        if winner == None:
            return render_template('result.html', title='result', result="It's a draw")
        else :
            return render_template('result.html', title='result', result=f"{winner.name} wins!")


        

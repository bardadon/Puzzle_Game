from flask import Flask, render_template, request, redirect, url_for
import numpy as np
from puzzle_game import generate_puzzle, generate_question, generate_sequence, solution, check_answer
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


sequence = generate_sequence()
np.random.shuffle(sequence)
puzzle = generate_puzzle(sequence)
sol = solution(sequence, puzzle)
question = generate_question(sol)
np.random.shuffle(sequence)
np.random.shuffle(puzzle)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', sequence = sequence, question = question)

@app.route('/home', methods = ['POST'])
def answer():
    form_data = request.form
    return render_template('solution', form_data=form_data)

    
@app.route('/solution')
def solution():
    return render_template('solution.html', title = 'solution')


@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form["Answer"]

        if check_answer(form_data):
            return render_template('solution.html',form_data = form_data)
        else:
            return render_template('wrong.html',form_data = form_data,sequence = sequence, question = question, s = sol)


@app.route('/rules')
def rules():
    return render_template('rules.html', title = 'rules')

@app.route('/start_game')
def start_game():
    return render_template('start_game.html', title = 'start_game')


if __name__ == '__main__':

    app.run(debug=True)

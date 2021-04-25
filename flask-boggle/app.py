  
from flask import Flask, request, render_template, make_response, redirect, flash, session, jsonify
#from flask_debugtoolbar import DebugToolbarExtension

from boggle import Boggle

boggle_game = Boggle()

my_board = boggle_game.make_board()

app = Flask(__name__)

@app.route("/")
def show_boggle():
    return render_template("base.html", my_board=my_board)

@app.route("/submit")
def submit_word():
    word = request.args["word"]

    response = make_response(
        jsonify({"result": boggle_game.check_valid_word(my_board, word)})
    )

    return response
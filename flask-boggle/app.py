  
from flask import Flask, request, render_template, redirect, flash, session
#from flask_debugtoolbar import DebugToolbarExtension

from boggle import Boggle

boggle_game = Boggle()

app = Flask(__name__)

@app.route("/")
def show_boggle():
    return render_template("base.html", boggle_game=boggle_game)
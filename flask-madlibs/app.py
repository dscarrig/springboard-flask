from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def ask_questions():
    p = story.prompts

    return render_template("questions.html", prompts=p)

@app.route("/story")
def show_story():
    t = story.generate(request.args)

    return render_template("story.html", text=t)
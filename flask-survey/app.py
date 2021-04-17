from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

RESPONSES_KEY = "responses"

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

debug = DebugToolbarExtension(app)

@app.route("/")
def select_survey():
    return render_template("select_survey.html", survey=satisfaction_survey)

@app.route("/begin", methods=["POST"])
def start_survey():
    session[RESPONSES_KEY] = []
    return redirect("questions/0")

@app.route("/answer", methods=["POST"])
def answer_question():
    choice = request.form["answer"]

    responses = session[RESPONSES_KEY]
    responses.append(choice)
    session[RESPONSES_KEY] = responses

    if len(responses) == len(satisfaction_survey.questions):
        return redirect("/complete")
    else:
        return redirect(f"/questions/{len(responses)}")


@app.route("/questions/<int:qnum>")
def display_question(qnum):
    responses = session.get(RESPONSES_KEY)

    if responses is None:
        return redirect("/")
    
    if len(responses) == len(satisfaction_survey.questions):
        return redirect("/complete")

    if len(responses) != qnum:
        flash(f"Invalid question id: {qnum}")

    question = satisfaction_survey.questions[qnum]

    return render_template("question.html", question_num=qnum, question=question)

@app.route("/complete")
def complete():
    return render_template("complete.html")

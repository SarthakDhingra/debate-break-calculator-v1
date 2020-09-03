import sys
import os

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

import ast
from flask import Flask, render_template, request, redirect, url_for
from wtforms import IntegerField, Form, StringField
from wtforms.validators import NumberRange, DataRequired, ValidationError
from Algorithm import Tournament

app = Flask(__name__)

class Breaking(object):
    def __init__(self, message=None):
        self.message=message

    def __call__(self, form, field):
        breaking = int(field.data)
        if form.style is not None:
            if breaking % form.style != 0:
                raise ValidationError(self.message)

class BreakForm(Form):
    rounds = IntegerField('rounds', validators=[NumberRange(min=1,max=9, message="Rounds must be an integer between 1 and 9 inclusive")])
    breaking = StringField('breaking', validators=[Breaking(message="Number Breaking is not divisible by Style")])   

@app.route('/', methods=['POST','GET'])
def root():

    teams = request.form.get("teams", None)
    rounds = request.form.get("rounds", None)
    breaking = request.form.get("breaking", None)
    style = request.form.get("style", None)

    if style is not None:
        style = int(style)

    form = BreakForm(request.form)
    form.style = style

    if teams and rounds and breaking and style and form.validate():   
        tournament = Tournament(style)
        results_best, results_worst = tournament.get_Break(teams=int(teams),rounds=int(rounds),breaking=int(breaking))
        return redirect(url_for('results',best=results_best,worst=results_worst, teams=teams, rounds=rounds, breaking=breaking))

    return render_template('form.html', form=form, teams=teams, rounds=rounds, breaking=breaking)

@app.route('/results', methods=['GET'])
def results():
    results_best = request.args.get("best", None)
    results_worst = request.args.get("worst", None)

    if results_best is not None and results_worst is not None:
        results_best = ast.literal_eval(results_best)
        results_worst = ast.literal_eval(results_worst)
    
    teams = request.args.get("teams", None)
    rounds = request.args.get("rounds", None)
    breaking = request.args.get("breaking", None)
    style = request.args.get("tournament", None)
    
    return render_template('form.html', results_best=results_best, results_worst=results_worst, teams=teams, rounds=rounds, breaking=breaking)


if __name__ == '__main__':
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.run(debug=True)


    


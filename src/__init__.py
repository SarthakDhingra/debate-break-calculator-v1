
import sys
import os
import ast

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

from flask import Flask, render_template, request, redirect, url_for
from Algorithm import Tournament
from wtforms import IntegerField, Form, StringField
from wtforms.validators import NumberRange, DataRequired, ValidationError

def DisibleBy(breaking,style,message):
    if breaking % style != 0:
        raise ValidationError(message)
    


class BreakForm(Form, style):
    rounds = IntegerField('rounds', validators=[NumberRange(min=1,max=9, message="Invalid Rounds. Must be between 1 and 9 inclusive")])
    rounds = IntegerField('rounds', validators=[NumberRange(min=1,max=9, message="Invalid Rounds. Must be between 1 and 9 inclusive")])
    if style is not None:
        breaking = IntegerField('rounds', validators=[DivisbleBy(breaking=,max=9, message="Invalid Rounds. Must be between 1 and 9 inclusive")])

    
app = Flask(__name__)
app.run(debug=True)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# a simple page that says hello
@app.route('/', methods=['POST','GET'])
# @app.route('/home', methods=['POST','GET'])
def hello():

    print("ARGS")
    print(request.args)
    print()

    results_best = request.args.get("best", None)
    results_worst = request.args.get("worst", None)

    if results_best is not None:
        results_best = ast.literal_eval(results_best)
    
    if results_worst is not None:
        results_worst = ast.literal_eval(results_worst)
    
    teams = request.args.get("teams", None)
    rounds = request.args.get("rounds", None)
    breaking = request.args.get("breaking", None)
    style = request.args.get("tournament", None)
    if style is not None:
        style = 2 if style == "Two Teams" else 4

    form = BreakForm(request.args,style)

    if form.validate():
        
        print("SUCCESS")
        
        # get input information

            
        tournament = Tournament(style)
        results_best, results_worst = tournament.get_Break(teams=int(teams),rounds=int(rounds),breaking=int(breaking))
        print()
        print("RESULTS")
        print(results_best)
        print(results_worst)
        print()
        return redirect(url_for('hello',best=results_best,worst=results_worst, teams=teams, rounds=rounds, breaking=breaking))
    
    print("FORM INFORMATION")
    print(form)
    print(form.errors)

    
    return render_template('form.html',results_best=results_best, results_worst=results_worst, teams=teams, rounds=rounds, breaking=breaking, form=form)
    

    


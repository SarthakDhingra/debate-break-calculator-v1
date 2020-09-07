import sys
import os

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

from flask import Flask, render_template, request, redirect, url_for
from wtforms import IntegerField, Form
from wtforms.validators import NumberRange, ValidationError
from Breaker import Tournament

# custom form validator to validate number of teams breaking
class BreakingValidator(object):
    def __init__(self, message=None):
        self.message=message

    def __call__(self, form, field):
        breaking = int(field.data)
        if form.style is not None:
            if breaking % form.style != 0:
                raise ValidationError(self.message)

# form validaton
class BreakForm(Form):
    rounds = IntegerField('rounds', validators=[NumberRange(min=1,max=9, message="Rounds must be an integer between 1 and 9 inclusive")])
    breaking = IntegerField('breaking', validators=[BreakingValidator(message="Number Breaking is not divisible by Style")])   

def create_app():
    app = Flask(__name__)
    app.debug = True

    @app.route('/', methods=['POST','GET'])
    def root():

        teams = request.form.get("teams")
        rounds = request.form.get("rounds")
        breaking = request.form.get("breaking")
        style = request.form.get("style")

        if style is not None:
            style = int(style)

        form = BreakForm(request.form)
        form.style = style

        if teams and rounds and breaking and style and form.validate():   
            tournament = Tournament(style)
            results_best, results_worst = tournament.get_Break(teams=int(teams),rounds=int(rounds),breaking=int(breaking),convert_string=True)
            return redirect(url_for('results',best=results_best,worst=results_worst, teams=teams, rounds=rounds, breaking=breaking))

        return render_template('form.html', form=form, teams=teams, rounds=rounds, breaking=breaking)

    @app.route('/results', methods=['GET'])
    def results():
        results_best = request.args.get("best")
        results_worst = request.args.get("worst")
        teams = request.args.get("teams")
        rounds = request.args.get("rounds")
        breaking = request.args.get("breaking")
        style = request.args.get("tournament")
        
        return render_template('form.html', results_best=results_best, results_worst=results_worst, teams=teams, rounds=rounds, breaking=breaking)
    
    return app


if __name__ == '__main__':
    SECRET_KEY = os.urandom(32)
    app = create_app()
    app.config['SECRET_KEY'] = SECRET_KEY
    app.run(debug=True)


    


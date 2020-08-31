
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

from flask import Flask, render_template, request
from Algorithm import Tournament

app = Flask(__name__)
app.run(debug=True)

# a simple page that says hello
@app.route('/', methods=['POST','GET'])
def hello():
    print("INFORMATION")
    print(request.form)
    teams = request.form.get("teams", None)
    rounds = request.form.get("rounds", None)
    breaking = request.form.get("breaking", None)
    style = request.form.get("tournament", None)
    results_best = None 
    results_worst = None
    if teams and rounds and breaking and style:
        style = 2 if style == "Two Teams" else 4
        tournament = Tournament(style)
        results_best, results_worst = tournament.get_Break(teams=int(teams),rounds=int(rounds),breaking=int(breaking))
        print("RESULTS")
        print(results_best)
        print(results_worst)
    
    return render_template('form.html',results_best=results_best, results_worst=results_worst)
    


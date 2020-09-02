
import sys
import os
import ast

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

from flask import Flask, render_template, request, redirect, url_for
from Algorithm import Tournament

app = Flask(__name__)
app.run(debug=True)

# a simple page that says hello
@app.route('/', methods=['POST','GET'])
# @app.route('/home', methods=['POST','GET'])
def hello():

    print("FORM")
    print(request.form)
    print()
    print("ARGS")
    print(request.args)
    print()

    results_best = request.args.get("best", None)
    results_worst = request.args.get("worst", None)

    if results_best is not None:
        results_best = ast.literal_eval(results_best)
    
    if results_worst is not None:
        results_worst = ast.literal_eval(results_worst)

    # get input information
    teams = request.args.get("teams", None)
    rounds = request.args.get("rounds", None)
    breaking = request.args.get("breaking", None)
    style = request.args.get("tournament", None)

    if teams and rounds and breaking and style:
        style = 2 if style == "Two Teams" else 4
        tournament = Tournament(style)
        results_best, results_worst = tournament.get_Break(teams=int(teams),rounds=int(rounds),breaking=int(breaking))
        print()
        print("RESULTS")
        print(results_best)
        print(results_worst)
        print()
        results_best = (results_best)
        return redirect(url_for('hello',best=results_best,worst=results_worst))
    
    return render_template('form.html',results_best=results_best, results_worst=results_worst)



    # if request.method == "POST":


    #     if teams and rounds and breaking and style:
    #         style = 2 if style == "Two Teams" else 4
    #         tournament = Tournament(style)
    #         results_best, results_worst = tournament.get_Break(teams=int(teams),rounds=int(rounds),breaking=int(breaking))
    #         print()
    #         print("RESULTS")
    #         print(results_best)
    #         print(results_worst)
    #         print()
    #         return redirect(url_for('hello',best=results_best,worst=results_worst))
    

    


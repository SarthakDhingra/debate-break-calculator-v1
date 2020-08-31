
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


    print("TEAMS")
    print(teams)
    return render_template('form.html')


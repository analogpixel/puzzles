

import flask
import json
import os

from puz import *
from constraint import *

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

# https://labix.org/python-constraint

@app.route("/")
def default():
    return render_template("index.html")

@app.route("/solve", methods=['POST'] )
def solve():
	data = json.loads(request.form['puzzleData'])
	puzSize = int(request.form['puzSize'])

	s = solvePuz(puzSize,data)

	#print(data)
	return json.dumps(s.solutions)


if __name__ == "__main__":
    appHost = int(os.environ['APP_HOST']) if 'APP_HOST' in os.environ else '0.0.0.0'
    appPort = int(os.environ['APP_PORT']) if 'APP_PORT' in os.environ else 5002
    app.run(debug=True, host=appHost,port=appPort)

from flask import Flask, render_template,request
from markupsafe import escape
import json
import pandas as pd
from convert import data

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/all')
def alllist():
    return data


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html"), 404

if __name__ == '__main__':
    app.run(debug=True)

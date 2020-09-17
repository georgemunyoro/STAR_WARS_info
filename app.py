from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/user/<path:username>')
def greeting(username):
    return " Hello, {}".format(escape(username))

@app.errorhandler(404)
def page_not_found(error):
    return "not found", 404

if __name__ == '__main__':
    app.run(debug=True)

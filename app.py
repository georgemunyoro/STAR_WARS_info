from flask import Flask, render_template, jsonify, request
from markupsafe import escape
import utils

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

@app.route('/search/')
def search():
    print(dict(request.args))
    if request.args.get('type') == 'characters':
        return {'items': utils.search_characters(**dict(request.args))}
    elif request.args.get('type') == 'vehicle':
        return {'items': utils.search_vehicles(**dict(request.args))}
    elif request.args.get('type') == 'species':
        return {'items': utils.search_species(**dict(request.args))}
    elif request.args.get('type') == 'starships':
        return {'items': utils.search_starships(**dict(request.args))}
    elif request.args.get('type') == 'planets':
        return {'items': utils.search_planets(**dict(request.args))}
    else:
        return {'items': utils.search_all(**dict(request.args))}

@app.errorhandler(404)
def page_not_found(error):
    return "not found", 404

if __name__ == '__main__':
    app.run(debug=True)

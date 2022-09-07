import os
from flask import Flask, render_template, abort, url_for
import json
import html
import random



app = Flask(__name__)

# read file
with open('./data/methods.json', 'r') as json_file:
    data_m = json.load(json_file)
with open('./data/persona.json', 'r') as json_file:
    data_p = json.load(json_file)



@app.route("/")
def index():
    return render_template('index.html')

@app.route('/methods/')
def methods():
    number=random.randint(0, 26)
    return render_template('methods.html', title="page", head= data_m[number]['Méthodes (inspirations) FR'], content = data_m[number]['Contenus Fr'] )


@app.route('/persona/')
def persona():
    number=random.randint(0, 8)
    return render_template('persona.html', title="page", head= data_p[number]['Persona (public)FR'], content = data_p[number]['Contenus FR'] )


if __name__ == '__main__':
    app.run(host='localhost', debug=True)
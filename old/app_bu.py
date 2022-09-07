#app.py
from flask import Flask, render_template
import random
r = random.randint(1,10)
#1 and 10 represent the range for your random value
print(r)

app = Flask(__name__) # name for the Flask app (refer to output)
#defining a route
# <id> allows us to capture corresponding character from the URL
@app.route("/persona/<id>")
def employee_details(id):
	return render_template('index.html', id = id, r = r)

app.run(debug = True)

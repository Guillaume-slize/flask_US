from flask import Flask, render_template

app = Flask(__name__) # name for the Flask app (refer to output)
#defining a route
@app.route("/", methods=['GET','POST','PUT'])#decorator
def home(): #route handler function
	#returning string
	return render_template('index.html',name='guillaume')
app.run(debug = True)

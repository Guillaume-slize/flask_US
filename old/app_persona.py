from flask import Flask, render_template, request
import sqlite3
import random
app = Flask(__name__)
def show_home_page():
    return render_template("home.html")

def get_random_element():
    # <snipped>: Do some sql queries and populate a list called P_LIST
    r = random.randint(0, len(P_LIST)) # This line silently fails.
    r_e = P_LIST[r]  # Never seems to get here
    print("get_random_element", r_e)  # Never prints this line!!
    return r_e

@app.route('/')
def server():
    return show_home_page()

@app.route('/element', methods=['POST', 'GET'])
def element():
    if request.method == 'GET':
        p = request.args.get('q', '')
        print("Request:", p)
        if p == 'random' or p == '':
           p = get_random_element()
           print("Random element:", p)
        else:
           print("Else:", p)
        return render_template('random.html', element=p)
    return show_home_page()

if __name__ == '__main__':
    app.run()
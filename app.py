# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/page2")
def page2():
    return render_template('page2.html')

@app.route("/page3")
def page3():
    return render_template('page3.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
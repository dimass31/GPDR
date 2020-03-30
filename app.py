from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

app.run(debug=True)
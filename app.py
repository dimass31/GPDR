from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        return redirect(url_for('signup', login=login))
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

app.run(debug=True)
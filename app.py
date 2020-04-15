from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print('post')
    if request.method == 'GET':
        print('get')
        try:
            login = request.args['login']
            print(login)
            return render_template('home.html', login=login)
        except:
            return render_template('home.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        return redirect(url_for('index', login=login))
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

app.run(debug=True)
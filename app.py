from flask import Flask, request, redirect, render_template, url_for, make_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        try:
            if (request.cookies.get('login')):
                login = request.cookies.get('login')
                return render_template('home.html', login=login)
            login = request.args['login']
            return render_template('home.html', login=login)
        except:
            return render_template('home.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        file = open('bd.txt', 'r')
        for line in file:
            sub= line.split(' ')
            if (login == sub[0]) & (password == sub[1]):
                res = make_response(redirect(url_for('index', login=login)))
                res.set_cookie('login', login, max_age=60*60*24)
                file.close()
                return res
        file.close()
        return render_template('login.html')
    return render_template('login.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('pass1')
        file = open('bd.txt', 'a')
        file.write('\n'+login+" "+password)
        file.close()
        res = make_response(redirect(url_for('index', login=login)))
        res.set_cookie('login', login, max_age=60*60*24)
        return res
    return render_template('signup.html')

@app.route('/profile')
def profile():
    login = request.cookies.get('login')
    return render_template('profile.html', login = login)

app.run(debug=True)
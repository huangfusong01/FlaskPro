from flask_script import Manager
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

manage = Manager(app=app)


@app.route('/')
def hello_world():
    A = 1
    B = 2
    RESULT = A/B
    return '<h1>Hello World!</h1> %s'%RESULT


@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username']=='admin':
            return redirect(url_for('home',username=request.form['username']))
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)


@app.route('/home')
def home():
    return render_template('home.html', username=request.args.get('username'))

@app.route('/index/')
def index():
    return render_template('index.html')

if __name__ == '__main__':

    # app.run(debug = True)
    manage.run(debug = True)

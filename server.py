from flask import Flask, render_template, redirect, url_for, request, session
from random import randint
import os
import codex
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/')
def index():
    idx = randint(1, 16)
    image = url_for('static', filename=f'images/{idx}.jpg')
    return render_template('index.html', image=image, ind=idx)


@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
    if request.method == 'POST':
        name = request.form['nm']
    else:
        name = request.args.get('nm', None)
    session['name'] = name
    return render_template('test.html', name=session.get('name'))


@app.route('/welcome/speaking', methods=['POST'])
def voice():
    idx = randint(113, 114)
    image = url_for('static', filename=f'images/{idx}.jpg')
    print('call function here')
    if request.method == 'POST':
        name = request.form['q']
    else:
        name = request.args.get('q', None)
        session['name'] = name
    name = codex.func(name)

    return render_template('hello.html', name=name, image=image)


if __name__ == '__main__':
    app.config['SECRET_KEY'] = os.urandom(24)
    app.run(debug=False)

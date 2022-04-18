
from flask import (Flask, make_response, redirect, render_template, request,
                   url_for)

app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']

        if pwd == '12345':  # hardcoded password
            resp = make_response(render_template('success.html'))
            resp.set_cookie('username', uname)
            return resp
        else:
            return redirect(url_for('error'))


@app.route('/error')
def error():
    return "<h1>eror</h1>"


@app.route('/profile')
def profile():
    uname = request.cookies.get('username')
    return render_template('profile.html', username=uname)


if __name__ == '__main__':
    app.run(debug=True)

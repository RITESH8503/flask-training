
from flask import Flask, make_response, redirect, render_template, session, url_for


app = Flask(__name__)
app.secret_key = 'thisIsS@omeVery5ecrsfkskdfksdfsdkfsdkfsdfsdkfkdsfet_sess_key'


@app.route('/')
def home():
    resp = make_response(render_template('home.html'))
    session['my_session'] = 'something about session'
    return resp


@app.route('/session')
def show_session():
    mysess = session['my_session']
    return render_template('show_session.html', mysess=mysess)


@app.route('/remove')
def remove_session():
    session.pop('my_session', None)
    return '<h1>session removed</h1>'


if __name__ == '__main__':
    app.run(debug=True)

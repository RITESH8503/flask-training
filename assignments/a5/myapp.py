from flask import Flask, make_response, redirect, render_template, request

app = Flask(__name__)


@app.route('/register', methods=['GET', 'POST'])
def register():
    resp = make_response(render_template('register.html'))

    error = None
    if request.method == 'POST':
        error = validate_registration_form(request.form)
        if error == None:
            resp.set_cookie('name', request.form['name'])
            resp.set_cookie('username', request.form['username'])
            resp.set_cookie('password', request.form['password'])
            
        else:
            resp = make_response(render_template('register.html', error=error))

    return resp


@app.route('/validate')
def validate_registration():
  return '<h1> Registration successful</h1>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        error = validate_login_form(request.form)
        if error == None:
            if (request.form['username'] == request.cookies.get('username')) and (request.form['password'] == request.cookies.get('password')):
                return redirect('home')
            else:
                error = 'Invalid login'

    return render_template('login.html', error=error)


@app.route('/home')
def home():
    name = request.cookies.get('name')
    if name != '' and name != None:
        return render_template('home.html', name=request.cookies.get('name'))
    else:
        return redirect('login')


def validate_registration_form(form):
    if form['name'] == '' or form['username'] == '' or form['password'] == '':
        return 'Required fields are empty!'

    if form['password'] != form['conf_password']:
        return 'Confirm password does not match'

    return None


def validate_login_form(form):
    if form['username'] == '' or form['password'] == '':
        return 'Required fields are empty!'

    return None


def set_my_cookies(resp, form):
    resp.set_cookie('name', form['name'])
    resp.set_cookie('username', form['username'])
    resp.set_cookie('password', form['password'])


if __name__ == '__main__':
    app.run(debug=True)

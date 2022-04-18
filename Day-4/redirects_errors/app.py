from flask import Flask, abort, redirect, render_template, request, url_for


app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/validate', methods=['POST'])
def validate():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        if uname == 'abbas' and pwd == '123':
            return redirect(url_for('success'))
        else:
            abort(401)
    else:
        abort(405)


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)


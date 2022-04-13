from flask import Flask, render_template


app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/table/<int:num>')
def myapp(num):
    return render_template('table.html', num=num)


@app.route('/action/<int:num>')
def myaction(num):
    a = num > 10
    return render_template('action.html', num=a)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if validate_form(request.form['first_name'], request.form['last_name'], request.form['email'], request.form['phone']):
            return render_template('success.html', res=request.form)
        else:
            return render_template('register.html', error="Invalid form")

    return render_template('register.html')


def validate_form(fname, lname, email, phone):
    return fname != '' and lname != '' and email != '' and phone != ''


if __name__ == '__main__':
    app.run(debug=True)


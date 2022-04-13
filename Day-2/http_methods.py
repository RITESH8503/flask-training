from flask import Flask, render_template, request

app = Flask(__name__)


#Request and response
@app.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        
        uname = request.form['username']
        pwd = request.form['password']
        
        if valid_login(uname, pwd):        
            if uname == 'abbas' and pwd == '1234':
                return 'Hi %s' % uname + ' how are you'
            else:
                return 'invalid login'
        else:
            return 'username and password are needed'

    return render_template('login.html')


def valid_login(username, password):
    return username != '' and password != ''


if __name__ == '__main__':
    app.run(debug=True)

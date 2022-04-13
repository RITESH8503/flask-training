from flask import Flask
from flask_mail import *

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'meanstack21@gmail.com'
app.config['MAIL_PASSWORD'] = 'Kh@dijabegum3#'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


mail = Mail(app)


@app.route('/')
def index():
    msg = Message('My subject', sender='meanstack21@gmail.com',
                  recipients=['mahbubabbas@gmail.com'])
    msg.body = 'hi, how are you doing...'

    mail.send(msg)

    return 'Mail sent. Thanks.'


if __name__ == '__main__':
    app.run(debug=True)

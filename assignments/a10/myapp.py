import random
from smtplib import SMTPException
from flask import Flask, flash, redirect, render_template, request, url_for

from flask_mail import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'akfkfssf sfkasfkafskasfasfkasfk'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'meanstack21@gmail.com'
app.config['MAIL_PASSWORD'] = 'Kh@dijabegum3#'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SECRET_KEY'] = 'ajjfdsjsfjsdfbsdfjsdfjdfjsdfSFSFDSDF'

mail = Mail(app)

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    email = db.Column('email', db.String(200), unique=True, nullable=False)
    password = db.Column('password', db.String(100), nullable=False)
    otp = db.Column('otp', db.String(4), nullable=False)
    verified = db.Column('verified', db.Boolean)

    def __init__(self, email, password, otp, verified):
        self.email = email
        self.password = password
        self.otp = otp
        self.verified = verified


def genOTP():
    return str(random.randint(1000, 9999))


def sendOTP(email, otp):
    msg = Message('Your OTP', sender='meanstack21@gmail.com',
                  recipients=[email])
    msg.body = 'Your OTP is %s' % otp
    mail.send(msg)

    return 'OTP sent to registered email id. Please verify your email.'


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = None
    if request.method == 'POST':
        try:
            otp = genOTP()
            email = request.form['email']
            user = User(email,
                        request.form['password'], otp, False)
            db.session.add(user)
            db.session.commit()

            sendOTP(email, otp)
            flash('Please verify the OTP sent to your email box')
            return redirect(url_for('verify_otp', email=email))
        except:
            db.session.rollback()
            msg = 'Error !'

    return render_template('register.html', msg=msg)


@app.route('/verify_otp/<email>', methods=['GET', 'POST'])
def verify_otp(email):
    msg = None
    if request.method == 'POST':
        otp = request.form['otp']
        student = User.query.filter_by(email=email).first()
        if student.otp == otp:
            student.verified = True
            db.session.commit()

            return '<h1>Registration successful</h1>'
        else:
            msg = 'Invalid OTP'

    return render_template('verify_otp.html', email=email, msg=msg)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

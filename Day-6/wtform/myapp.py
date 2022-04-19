
from flask import Flask, flash, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField, validators

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = 'ajafj@SFA61_jfsAQskjfsds@#kssd19FAFjsfXasdj_+#smfdksdfASDSD'

app.secret_key = 'ajafj@SFA61_jfsAQskjfsds@#kssd19FAFjsfXasdj_+#smfdksdfASDSD'

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    gender = db.Column('gender', db.String(1))
    class_name = db.Column('class_name', db.String(100))
    roll_no = db.Column('roll_no', db.String(10))

    def __init__(self, name, gender, class_name, roll_no):
        self.name = name
        self.gender = gender
        self.class_name = class_name
        self.roll_no = roll_no


@app.route('/')
def index():
    return render_template('index.html', students=Student.query.all())


class StudentForm(FlaskForm):
    name = StringField(
        'Name', [validators.DataRequired('Please enter student name')])

    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])

    class_name = StringField(
        'Class', [validators.DataRequired('Please enter class')])

    roll_no = StringField(
        'Roll', [validators.DataRequired('Please enter roll')])

    submit = SubmitField('Submit')


@app.route('/add', methods=['GET', 'POST'])
def add():
    msg = None

    form = StudentForm()
    if request.method == 'POST':
        if form.validate() == False:
            msg = 'Invalid input'
        else:
            try:
                student = Student(request.form['name'], request.form['gender'],
                                  request.form['class_name'], request.form['roll_no'])

                db.session.add(student)
                db.session.commit()
                msg = 'Addition successful!'
            except:
                msg = 'Error adding student!'

    return render_template('add.html', form=form, msg=msg)


if __name__ == '__main__':
    db.create_all()

    app.run(debug=True)

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = 'AS62nsfjadsaj_@dfjfsfhbf182sfjdfASFAKSF'


db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    class_name = db.Column(db.String(100))
    roll_no = db.Column(db.String(100))

    def __init__(self, name, class_name, roll_no):
        self.name = name
        self.class_name = class_name
        self.roll_no = roll_no


@app.route('/')
def index():
    return render_template('list.html', students=Student.query.all())


@app.route('/add', methods=['GET', 'POST'])
def add():
    msg = None
    if request.method == 'POST':
        try:
            student = Student(
                request.form['student_name'], request.form['class_name'], request.form['roll_no'])
            db.session.add(student)
            db.session.commit()

            flash('Student addition successful')
            return redirect(url_for('index'))
        except:
            msg = 'Error adding student'

    return render_template('add.html', msg=msg)


@app.route('/delete/<id>')
def delete(id):
    try:
        Student.query.filter_by(id=id).delete()
        db.session.commit()
        flash('Deletion successful')
    except:
        flash('Unable to delete!')

    return redirect(url_for('index'))


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    student = Student.query.filter_by(id=id).first()

    if request.method == 'POST':
        try:
            student.name = request.form['student_name'] 
            student.class_name = request.form['class_name']
            student.roll_no = request.form['roll_no']
            
            db.session.commit()

            flash('Update successful')
        except:
            flash('Error updating student!')

        return redirect(url_for('index'))
    else:
        return render_template('edit.html', student=student)


if __name__ == '__main__':
    db.create_all()

    app.run(debug=True)

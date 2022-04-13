from flask import Flask, render_template, request
from datetime import datetime
import pytz


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def show_time():
    current_time = None
    mytz = None

    if request.method == 'POST':
        mytz = request.form['mytz']
        current_time = calculate_time(mytz)

    return render_template('show_time.html', current_time=current_time, mytz=mytz)


def calculate_time(mytz):
    try:
        myzone = pytz.timezone(mytz)
        return datetime.now(myzone).strftime('%Y:%m:%d %H:%M:%S')
    except:
        return 'Invalid timezone'


if __name__ == '__main__':
    app.run(debug=True)

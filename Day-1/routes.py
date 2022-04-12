from flask import Flask, escape


app = Flask(__name__)


# routes with variable path
@app.route('/user/<username>')
def display_username(username):
    return f"hi {escape(username)}"


@app.route('/usr/<int:id>')
def display_id(id):
    return f"your id is : {escape(id)}"


@app.route('/path/<path:subpath>')
def display_path(subpath):
    return f"subpath {escape(subpath)}"


if __name__ == '__main__':
    app.run(debug=True)

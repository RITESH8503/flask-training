from flask import Flask
app = Flask(__name__)

# hello world
@app.route("/")
def hello_world():
    "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(debug=True)

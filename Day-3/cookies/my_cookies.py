
from flask import Flask, make_response


app = Flask(__name__)


@app.route('/')
def my_cookies():
    resp = make_response('<h1>This is a test for cookie</h1')
    resp.set_cookie('username', 'abbas')
    return resp


if __name__ == '__main__':
    app.run(debug=True)

# to see the cookie in chrome
# chrome://settings/cookies/detail?site=localhost


from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/users', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        data = 'my users'
        return jsonify({'data': data})

    if request.method == 'POST':
        data = 'login successful'
        return jsonify({'user': data})


if __name__ == '__main__':
    app.run(debug=True)

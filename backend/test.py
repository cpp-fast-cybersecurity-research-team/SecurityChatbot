from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

@app.route('/route')
def home():
    data = 'Hello World'
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
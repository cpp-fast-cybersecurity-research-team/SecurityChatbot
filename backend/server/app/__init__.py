from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# app.config.from_object(config)
CORS(app, origins=['http://localhost:3000'])

from .routes import gpt_routes
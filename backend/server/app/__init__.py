from flask import Flask
# from config import Config
from flask_cors import CORS

app = Flask(__name__)
# app.config.from_object(Config)
CORS(app, origins=['http://localhost:3000'])

from .routes import gpt_routes
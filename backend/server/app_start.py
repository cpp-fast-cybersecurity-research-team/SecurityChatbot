import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from app import app, db

# Run app
if __name__ == '__main__':
    app.run(debug=True)
    db.init_app(app)
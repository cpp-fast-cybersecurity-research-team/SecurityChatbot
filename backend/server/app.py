import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

from app import app

if __name__ == '__main__':
    app.run(debug=True)
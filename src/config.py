from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import getenv

load_dotenv()

test_env = getenv("TEST_ENV") == "true"
print(f"Test environment: {test_env}")

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

# Class for remembering toggle status, maybe should be somewhere else
class Toggle:
    def __init__(self):
        self.state = False
    
    def change_state(self):
        self.state = not self.state

    def get_state(self):
        return self.state

toggle = Toggle()
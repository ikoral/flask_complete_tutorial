from flask import Flask

app = Flask(__name__)

# import routes always after app
from app import routes


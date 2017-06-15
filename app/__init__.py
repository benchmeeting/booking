from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


application = Flask(__name__)
application.config.from_object(config)
db = SQLAlchemy(application)

from app import controllers, models

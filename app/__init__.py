from flask import Flask
import config


application = Flask(__name__)
application.config.from_object(config)

from app import controllers

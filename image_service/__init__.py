from flask import Flask
import os

controller = Flask(__name__)
controller.config.from_pyfile('config.json')

from image_service import api

controller.config['SECRET_KEY'] = os.urandom(128)

if __name__ == '__main__':
    controller.run()

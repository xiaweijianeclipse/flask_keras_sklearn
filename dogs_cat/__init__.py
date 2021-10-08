from flask import Flask
from flask_bootstrap import Bootstrap
from dogs_cat import dogsCat
from admin import admin
from Iris import Iris

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'TPmi4aLWRbyVq8zu9v82dWYW1'

    bootstrap = Bootstrap(app)

    app.register_blueprint(dogsCat.dogCatBlueprint)
    app.register_blueprint(admin.adminbp)
    app.register_blueprint(Iris.irisBp)

    return app

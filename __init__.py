import os

from flask import Flask

from server.routes import incomes_bp


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(incomes_bp)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
